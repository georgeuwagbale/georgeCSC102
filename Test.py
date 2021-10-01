import pandas

def sims():
    condition = int(input("Amount of data: "))
    names = []
    departments = []
    levels = []
    matric_numbers = []

    for a in range(condition):
        name = str(input("Input a name: "))
        names.append(name)
        department = str(input("Input department: "))
        departments.append(department)
        level = int(input("Input level: "))
        levels.append(level)
        matric_number = int(input("Input Matric_no: "))
        matric_numbers.append(matric_number)
        print(".......")

    data = {
        "Name": names,
        "Department": departments,
        "Level": levels,
        "Matric Number": matric_numbers
    }

    Data_frame = pandas.DataFrame(data)
    Data_frame.to_excel("Sims.xlsx")
    return Data_frame


class Person:

    def __init__(me, name, sex):
        me.name = name
        me.sex = sex

    def __str__(me):
        return "Name:{}; Gender:{}".format(me.name, me.sex)


p1 = Person("George", "Male")
print(p1)
