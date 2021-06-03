
class Student:
     studentLevel = 'first year computer science 2020/2021 session'
     studentCounter = 0
     registeredCourses = ["CSC102"]

     def __init__(self, thename, thematricno, thesex, hostelname, age, csc102examscore):
         self.name = thename
         self.matricno = thematricno
         self.sex = thesex
         self.hostelname = hostelname
         self.age = age
         self.csc102examscore = csc102examscore
         Student.studentCounter +=1

     def getName(self):
         return  self.name

     def setName(self, thenewName):
             self.name = thenewName

     def age_above_16(self):
        if self.age > 16:
            return "Student is older than 16"
        else:
            return "Student is younger than 16"

     def passed_csc102(self):
         if self.csc102examscore > 45:
             return "You passed CSC102 examination"

         else:
             return "You failed the CSC102 examination, you would have to enroll for the next year"


     @classmethod
     def registered_courses(cls):
         print("Registered Course is ", end=" ")

         for courses in cls.registeredCourses:
             return f"{cls.registeredCourses[0]}"

     @classmethod
     def display_studentCounter(cls):
         return f"Number of students: {cls.studentCounter}"


     @staticmethod
     def PAUNanthem():
        print('Pau, here we come, Pau, here we come ')

     @staticmethod
     def even_odd(number):
         if number % 2 == 0:
            return f"{number} is even"

         elif number % 2 == 1:
            return f"{number} is odd"

     def __str__(self):
         return f"""Name: {self.name} Matric NO: {self.matricno} \nSex: {self.sex} Age: {self.age} \nCSC102 Examination Score: {self.csc102examscore} """





studendt1 = Student('James Kaka', '021074', 'M',"Cooperative",17,80)
print(studendt1.getName())
studendt1.setName('James Gaga')
print(studendt1.getName())
print(studendt1.passed_csc102())
print(Student.display_studentCounter())
print(Student.registered_courses())

Student.PAUNanthem()
print(Student.even_odd(5))
print(studendt1.age_above_16())
print(studendt1)
