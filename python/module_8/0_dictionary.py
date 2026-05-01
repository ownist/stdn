# introduce dictionary
student = {"name": "Shahed", "age": 17, "occupation": "student"}
print(student)


# ---------- get the value ----------
print(student["name"])
print(student["age"])

print(student.get("name"))
print(student.get("occupation"))

# key na thakle err dibe nh.. none dibe. which mean's program crash korbe nah
print(student.get("major"))
