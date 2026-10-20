class Student:
    def __init__(self, name):
        self.name = name
        self.__marks = 0

    def set_marks(self, marks):

        if marks < 0 or marks > 100:
            raise ValueError("Marks should be between 0 and 100.")
        self.__marks = marks

    def get_marks(self):
        return self.__marks

    def grade(self):
        if self.__marks >= 90:
            return "A"
        elif self.__marks >= 80:
            return "B"
        elif self.__marks >= 70:
            return "C"
        elif self.__marks >= 60:
            return "D"
        else:
            return "F"



student1 = Student("Suraj")
student1.set_marks(85)
print(f"{student1.name} has scored {student1.get_marks()} marks and received grade: {student1.grade()}")