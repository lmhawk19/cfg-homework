
class Student:

    def __init__(self, name, age, id):

        self.name = name
        self.age = age
        self.id = id
        self.subjects = dict()

class CFGStudent(Student):

  def __init__(self, name, age, id, specialisation):
        super().__init__(name, age, id)
        self.specialisation = specialisation

  def add_subject(self, subject_and_grade):
    self.subjects.update(subject_and_grade)

  def remove_subject(self, subject):
        self.subjects.pop(subject)

  def get_overall_mark(self):
        return sum(self.subjects.values())/len(self.subjects.values())

  def view_all_subjects(self):
    for subject, grade in self.subjects.items():
            print(f"{self.name} grade for {subject} {grade}")


#Students
first_student = CFGStudent("Lucy", 25, 1, "Software")
second_student = Student("Luke", 22, 2)
third_student = Student("Holly", 28, 3)

#Add subject and grade
first_student.add_subject({"APIs": 70})
first_student.add_subject({"MySQL": 60})
first_student.add_subject({"Python Basics": 90})

#Remove subject and grade
first_student.remove_subject("MySQL")

#View all subjects by student
first_student.view_all_subjects()

#Get student’s overall mark
print(first_student.get_overall_mark())


# class CFGStudent(<should inherit from Student>)
#     create new methods that manage student's subjects (add/remove new subject and its grade to the dict)
#     create a method to view all subjects taken by a student
#     create a method (and a new variable) to get student's overall mark (use average)



