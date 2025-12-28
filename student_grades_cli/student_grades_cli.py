N = int(input("How many students are you going to enter? "))

students = []
exam1 = []
exam2 = []

for i in range(N):
    students.append(input("Please enter student's name: "))
    exam1.append(float(input("Please enter exam 1: ")))
    exam2.append(float(input("Please enter exam 2: ")))

combined = list(zip(students, exam1, exam2))

average_grade = list(
    map(lambda item: (item[0], (item[1] + item[2]) / 2), combined)
)

approved_students = list(
    filter(lambda grade: grade[1] >= 7.0, average_grade)
)

messages = list(
    map(lambda student: f"{student[0]} passed with average {student[1]:.1f}", approved_students)
)

print(messages)
