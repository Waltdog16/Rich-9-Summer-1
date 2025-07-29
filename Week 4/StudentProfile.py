student = {}
studentName = input("Enter your students name: ")
student["Name"] = studentName
print(student)
student_profile = {}
student_profile["Age"] = int(input("Enter your age: "))
student_profile["Grade"] = input("Enter your grade: ")
hobbies = []
num_hobbies = int(input("How many hobbies do you want to enter? "))
for i in range(num_hobbies):
    hobby = input(f"Enter hobby #{i + 1}: ")
    hobbies.append(hobby)
student_profile["Hobbies"] = hobbies
print("\nStudent Profile:")
print(student_profile)









