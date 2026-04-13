 class Student:
  4     def int(self, name, marks):
  5         self.name = name
  6         self.marks = marks
  7     def calculate_total(self):
  8         return sum(self.marks)
  9     def calculate_average(self):
 10         if not self.marks:
 11             return 0
 12         return self.calculate_total() / len(self.marks)
 13     def display_details(self):
 14         print("Student Name:",(self.name))
 15         print("Marks:",(self.marks))
 16         print("Total Marks:", (self.calculate_total()))
 17         print("Average Marks:",(self.calculate_average()))
 18 student1 = Student("Rohit kumar", [85, 90, 92, 88])
 19 student2 = Student("Swathy", [78, 82, 80, 76])
 20 student3 = Student("Anu", [95, 98, 91, 94])
 21 students_list = [student1, student2, student3]
 22 highest_mark_holder = max(students_list, key=lambda student:
 23 student.calculate_total())
 24
 25 print("\nDetails of the student with the highest total marks:\n")
 26 highest_mark_holder.display_details()
 27 print("\n---STUDENT DETAILS---")
 28 print("\nstudent 1...")
 29 print(student1.display_details())
 30 print("\nstudent 2...")
 31 print(student2.display_details())
 32 print("\nstudent 3...")
 33 print(student3.display_details())
