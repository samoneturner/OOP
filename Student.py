import StudentClass as sc

studentid = 1001
name = "John"
dob = "10/15/2001"
classification = "junior"

student1 = sc.Student(studentid, name, dob, classification)

student1.calc_age()

student1.register()

print("Student age is:", student1.return_age)

print("student can register between:", student1.__register)
