from typing import List

def countDroppedRequests(server: List[int]) -> int:
    numThreads = 0
    dropped = 0

    for event in server:
        if event == -1:
            if numThreads > 0:
                numThreads -= 1
            else:
                dropped += 1
        else:
            numThreads += event

    return dropped


def main():
    test_cases = [
        [ -1, -1, -1, -1 ],
        [ 4, -1, -1, -1 ],
        [ 1, -1, 1, -1 ]
    ]

    for i, case in enumerate(test_cases, 1):
        result = countDroppedRequests(case)
        print(f"Test Case {i}: Input = {case} → Dropped Requests = {result}")


if __name__ == "__main__":
    main()
