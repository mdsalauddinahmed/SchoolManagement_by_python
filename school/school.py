class School:
    def __init__(self,name,address) -> None:
         self.name=name
         self.address=address
         #composition
         self.teachers={}
         self.classrooms = {}

    def add_classroom(self,classroom):
         self.classrooms[classroom.name]=classroom

    def add_teacher(self,subject,teacher):
         self.teachers[subject]=teacher

    def student_admission(self,student):
        className =student.classroom.name

        if className in self.classrooms:
              #TODo :set student id ,(roll,id) at the time of adding the student
              self.classrooms[className].add_student(student)
        else:
              print(f'No classes as named {className}')


    @staticmethod
    def calculate_grade(marks):
         if 80<=marks<= 100:
              return 'A+'
         elif 70 <=marks<=80:
              return 'A'
         elif 60<=marks<=70:
              return 'A-'
         elif 50<=marks<=60:
              return 'B'
         elif 40<=marks<=50:
              return 'C'
         elif 33<=marks<=40:
              return 'D'
         else:
              return'F'
    @staticmethod
    def value_to_grade(value):
         if 4.5<=value<= 5.00:
              return 'A+'
         elif 3.5 <=value<=4.5:
              return 'A'
         elif 3.00<=value<=3.5:
              return 'A-'
         elif 2.50<=value<=3.0:
              return 'B'
         elif 2.00<=value<=2.50:
              return 'C'
         elif 1.0<=value<=2.0:
              return 'D'
         else:
              return'F'
         

    @staticmethod
    def grade_to_value(grade):
         grade_map = {
              'A+': 5.00,
              'A': 4.00,
              'A-': 3.50,
              'B': 3.00,
              'C': 2.00,
              'D': 1.00,
              'F': 0.00,
         }
         return grade_map[grade]
    def __repr__(self) -> str:
         print('--------All classrooms------')
         for key,value in self.classrooms.items():
              print(key)

         print("-----students-----")
         eight = self.classrooms['eight']
         print(len(eight.students))

         for student in eight.students:
              print(student.name)

         print('---Subjects---')

         for subject in eight.subjects:
              print(f'Subject: {subject.name}  Teachers : {subject.teacher}')
         print('---students Exam marks-----')
         for student in eight.students:
              for key,value in eight.students[0].marks.items():
                print(f'{student.name} ,Subject :{key},Marks :{value}, grade : {student.subject_grade[key]}')
              print("----------finished------")
         return ' '
    
class classroom:
    def __init__(self,name) -> None:
          self.name = name
          self.students = []
          self.subjects = []


    def add_student(self,student):
        serial_id = f'{self.name}--{len(self.students)+1}'
        student.id= serial_id
     
        self.students.append(student)

    def add_subject(self,subject):
         self.subjects.append(subject)
    
    def semister_final(self):
         for subject in self.subjects:
              subject.exam(self.students)


        #calculate final grade
         for s in self.students:
              s.final_grade()
         
    def __str__(self) -> str:
         return f'{self.name}-{len(self.students)}'
    #Todo sort student by grade

    def get_top_students(self):
         pass
    

class Subject:
     def __init__(self,name,teacher) -> None:
          self.name = name
          self.teacher= teacher
          self.max_marks= 100
          self.pass_marks =33


     def exam(self,students):
          for student in students:
               mark = self.teacher.evaluate_exam()
               student.marks[self.name]=mark
               student.subject_grade[self.name]=School.calculate_grade(mark)

               

         