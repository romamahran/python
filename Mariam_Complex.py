import math

class Complex:
    def __init__(self, real_part, imag_part):
        self.real = real_part
        self.imag = imag_part

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real_val = self.real * other.real - self.imag * other.imag
        imag_val = self.real * other.imag + self.imag * other.real
        return Complex(real_val, imag_val)

    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imag ** 2
        real_val = (self.real * other.real + self.imag * other.imag) / denominator
        imag_val = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real_val, imag_val)

    def mod(self):
        return Complex(math.sqrt(self.real ** 2 + self.imag ** 2), 0)

    def __str__(self):
        real_str = f"{self.real:.2f}"
        imag_str = f"{abs(self.imag):.2f}"
        operator = '+' if self.imag >= 0 else '-'
        return f"{real_str}{operator}{imag_str}i"

def main():
    r1 = float(input("Enter real part of first complex number: "))
    i1 = float(input("Enter imaginary part of first complex number: "))
    r2 = float(input("Enter real part of second complex number: "))
    i2 = float(input("Enter imaginary part of second complex number: "))

    comp1 = Complex(r1, i1)
    comp2 = Complex(r2, i2)

    print(comp1 + comp2)
    print(comp1 - comp2)
    print(comp1 * comp2)
    print(comp1 / comp2)
    print(comp1.mod())
    print(comp2.mod())

if __name__ == "__main__":
    main()
