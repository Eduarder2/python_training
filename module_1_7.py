students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Auron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3],
          [5, 5, 5, 4, 5]]
students_ordered = list(students)
students_ordered.sort()
average_rating = {student: sum(grades_of_student) / len(grades_of_student)
                  for student, grades_of_student in zip(students, grades)}
print(average_rating)