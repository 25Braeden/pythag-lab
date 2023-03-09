import math

def pythagorean_theorem(a: float, b: float) -> float:
    """
    Calculate the length of the hypotenuse (c) given the lengths of the other two sides (a and b).
    """
    c = math.sqrt(a ** 2 + b ** 2)
    return c

while True:
    try:
        a = float(input("Enter a value for leg a: "))
        b = float(input("Enter a value for leg b: "))
        break
    except ValueError:
        print("Invalid input. Please enter a number for both legs.")

c = pythagorean_theorem(a, b)
print(f"From those values, leg c is: {round(c, 2)}")
