# sort() method     = used with lists
# sort() function   = used with iterables

students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs"]
# students.sort()
students.sort(reverse=True)
# for i in students: print(i)

# --------------------------------

students2 = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs")
# sorted_students = sorted(students2)
sorted_students = sorted(students2, reverse=True)
# for i in sorted_students: print(i)

# --------------------------------

students3 = [("Squidward", "F", 60),
             ("Sandy", "A", 33),
             ("Patrick", "D", 36),
             ("Spongebob", "B", 20),
             ("Mr.Krabs", "C", 78)]
# students3.sort()
grade = lambda grades: grades[1]
age = lambda ages: ages[2]
# students3.sort(key=grade) # will be sorted by their grades
# students3.sort(key=grade, reverse=True) # will be sorted by their reversed grades
students3.sort(key=age)
# for i in students3: print(i)

# --------------------------------

students4 = (("Squidward", "F", 60),
             ("Sandy", "A", 33),
             ("Patrick", "D", 36),
             ("Spongebob", "B", 20),
             ("Mr.Krabs", "C", 78))
sorted_students2 = sorted(students4, key=age)
for i in sorted_students2: print(i)
