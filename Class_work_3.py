"""Write a Python program which wil return true if the two given integer values are equal or their sum or difference is 5."""

def value():
    a = int(input("Input an integer: "))
    b = int(input("Input an integer: "))

    if a == b:
        return True
    elif (a + b) == 5:
        return True
    elif (a - b) == 5:
        return True
   else:
        return False
print(value())
