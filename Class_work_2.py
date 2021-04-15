"""Write a Python program to calculate the sum of three given numbers,if the values are equal then return thrice of their sum."""

def sum_of_three_numbers():
    a = int(input("Input a number: "))
    b = int(input("Input a second number: "))
    c = int(input("Input a third number: "))
    if a==b==c:
        result = (a + b + c) *3
        return result
    else:
        result = a + b + c
        return result

print(sum_of_three_numbers())


