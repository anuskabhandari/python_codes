##Example 5 – Lambda with sorted()
students = [
   ("Ram", 20),
   ("Shyam", 18),
   ("Hari", 22)
]

sorted_students = sorted(students, key=lambda x: x[1])

print(sorted_students)

## convert to uppercase
names = ["ram", "shyam", "hari"]

upper_names = list(map(lambda x: x.upper(), names))
print(upper_names)

## filter students who passed

students = [
   {"name": "Ram", "marks": 80},
   {"name": "Shyam", "marks": 50}
]

passed = list(filter(lambda s: s["marks"] >= 60, students))
print(passed)

