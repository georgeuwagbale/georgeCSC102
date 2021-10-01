class Student:
    def __init__(self, name, age, department, date_of_admission, program_of_study):
        self.name = name
        self.age = age
        self.date_of_admission = date_of_admission
        self.department = department
        self.program_of_study = program_of_study

    @staticmethod
    def gpa_calculator():
        courses = {
            "MATH":3,
            "GST105":2,
            "GST102":3,
            "GST104":2,
            "CSC102":3,
            "PHY102":3
        }
        point = 0
        total_course_unit = 0
        for keys in courses.keys():
            total_course_unit += courses[keys]
            letter_grade = str(input(f"Input letter grade for {keys}: "))
            if letter_grade.upper() == "A":
                point += courses[keys] * 5
            elif letter_grade.upper() == "B":
                point += courses[keys] * 4
            elif letter_grade.upper() == "C":
                point += courses[keys] * 3
            elif letter_grade.upper() == "D":
                point += courses[keys] * 2
            elif letter_grade.upper() == "F":
                point += courses[keys] * 0
            else:
                flag = 2
                while flag:
                    print("Incorrect input, letter grades are from A - F")
                    alphabet_grade = str(input(f"Input letter grade for {keys}: "))
                    if alphabet_grade.upper() == "A":
                        point += courses[keys] * 5
                        flag = False
                    elif alphabet_grade.upper() == "B":
                        point += courses[keys] * 4
                        flag = False
                    elif alphabet_grade.upper() == "C":
                        point += courses[keys] * 3
                        flag = False
                    elif alphabet_grade.upper() == "D":
                        point += courses[keys] * 2
                        flag = False
                    elif alphabet_grade.upper() == "F":
                        point += courses[keys] * 0
                        flag = False
                    else:
                        flag -= 1

        grade = point / total_course_unit
        gpa = round(grade, 2)
        return gpa


student = Student().gpa_calculator()
print(student)
