import random
import math
from school import School
class Person:
    def __init__(self,name) -> None:
        self.name=name


class Teacher(Person):
    def __init__(self, name) -> None:
        super().__init__(name)
         


    def teach(self):
        pass
    def __str__(self) -> str:
         return f'{self.name}'
    
    def evaluate_exam(self):
        marks= random.randint(0,100)
        return marks
           #Todo : set marks for the subject for each student


class student(Person):
    def __init__(self, name,classroom) -> None:
        super().__init__(name)
        self.classroom=classroom
        self.__id =None
        self.marks = {}
        self.subject_grade={}
        self.grade =None


    def final_grade(self):
        total =0
        for grade in self.subject_grade.values():
           
            point =School.grade_to_value(grade)
            total +=point
            print(self.name , grade,point)
        point_average=total/len(self.subject_grade)
        self.grade =School.value_to_grade(point_average)
        print(f'{self.name} Final Grade :{self.grade} with average point : {(round(point_average,2))}')

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,value):
        self.__id= value