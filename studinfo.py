name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

m1 = float(input("Enter Mathematics Marks: "))
m2 = float(input("Enter Science Marks: "))
m3 = float(input("Enter Programming Marks: "))

total = m1 + m2 + m3

def avg(t, s):
    return t / s

a = avg(total, 3)

if a >= 80:
    grade = "A"
elif a >= 60:
    grade = "B"
else:
    grade = "C"

sub = ["Mathematics", "Science", "Programming"]
marks = [m1, m2, m3]

print("\nStudent Details")
print("Name:", name)
print("Roll:", roll)

for i in range(len(sub)):
    print(sub[i], ":", marks[i])

print("Total:", total)
print("Average:", round(a, 2))
print("Grade:", grade)

file = open("student_record.txt", "w")
file.write("Student Information\n")
file.write("Name: " + name + "\n")
file.write("Roll: " + roll + "\n")
file.write("Mathematics: " + str(m1) + "\n")
file.write("Science: " + str(m2) + "\n")
file.write("Programming: " + str(m3) + "\n")
file.write("Total: " + str(total) + "\n")
file.write("Average: " + str(round(a, 2)) + "\n")
file.write("Grade: " + grade)
file.close()

print("\nSaved Successfully")

file = open("student_record.txt", "r")
print(file.read())
file.close()

print("\nAI Libraries")
print("NumPy")
print("Pandas")
print("Matplotlib")
print("Scikit-learn")

print("\nCloud AI")
print("Google Colab")
print("Google Cloud AI")
print("Microsoft Azure AI")