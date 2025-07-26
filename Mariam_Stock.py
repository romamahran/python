import threading

class StockThread(threading.Thread):
    def __init__(self, name, prices):
        super().__init__()
        self.name = name
        self.data = prices
        self.profit = 0

    def run(self):
        for i in range(1, len(self.data)):
            if self.data[i] > self.data[i - 1]:
                self.profit += self.data[i] - self.data[i - 1]


class StockApp:
    def __init__(self):
        self.stocks = {}
        self.threads = []

    def input_data(self):
        try:
            num = int(input("Enter number of stocks: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            return self.input_data()

        for i in range(1, num + 1):
            raw = input(f"Enter prices for stock {i} (space-separated): ")
            try:
                prices = list(map(int, raw.strip().split()))
                if len(prices) < 2:
                    print("At least 2 prices required.")
                    return self.input_data()
                self.stocks[f"stock{i}"] = prices
            except:
                print("Invalid input. Please enter integers only.")
                return self.input_data()

    def analyze(self):
        results = []

        for name, prices in self.stocks.items():
            thread = StockThread(name, prices)
            self.threads.append(thread)
            thread.start()

        for thread in self.threads:
            thread.join()
            results.append((thread.name, thread.data, thread.profit))

        best = max(results, key=lambda x: x[2])
        print("\n=== Stock Profits ===")
        for r in results:
            print(f"{r[0]}: {r[1]} → Profit: {r[2]}")
        print("\n=== Best Performer ===")
        print(f"{best[0]} has the highest profit: {best[2]}")

if __name__ == "__main__":
    app = StockApp()
    app.input_data()
    app.analyze()
