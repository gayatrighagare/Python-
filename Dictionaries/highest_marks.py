marks = {
    "A": 85,
    "B": 92,
    "C": 78
}

max_student = max(marks, key=marks.get)

print("Top student:", max_student)