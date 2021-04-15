"""Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference."""

def difference():
    value = int(input("Input a number: "))
    x = value - 17
    if x > 17:
        result = 2*x
        return result

    else:
        return abs(x)

print(difference())
