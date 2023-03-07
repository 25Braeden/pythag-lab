import math
def pythag(a, b):
    c = math.pow(a, 2) + math.pow(b, 2)
    final = math.sqrt(c)
    return final

a = float(input("Enter a value for leg a: "))
b = float(input("Enter a value for leg b: "))
print(f"From those values, leg c is: {pythag(a, b)}")