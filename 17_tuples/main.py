student = ("Alex", 21, "male")
print(student.count("Alex"))
print(student.index("male"))

for x in student: print(x)

if "Alex" in student:
    print("Alex is in student")