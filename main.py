students = []

# Load data from file at start
try:
    file = open("students.txt", "r")

    for line in file:
        data = line.strip().split(",")

        if len(data) == 4:
            student = {
                "name": data[0],
                "roll": data[1],
                "branch": data[2],
                "marks": data[3]
            }
            students.append(student)

    file.close()

except FileNotFoundError:
    # If file not exists, create empty list
    students = []


# Add Student
def add_student():
    name = input("Enter Name: ")
    roll = input("Enter Roll Number: ")
    branch = input("Enter Branch: ")
    marks = input("Enter Marks: ")

    # check duplicate roll
    for s in students:
        if s["roll"] == roll:
            print("Roll Number already exists!")
            return

    student = {
        "name": name,
        "roll": roll,
        "branch": branch,
        "marks": marks
    }

    students.append(student)

    file = open("students.txt", "a")
    file.write(name + "," + roll + "," + branch + "," + marks + "\n")
    file.close()

    print("Student Added Successfully")


# View Students
def view_students():
    if len(students) == 0:
        print("No Students Found")
        return

    print("\n--- All Students ---")
    for s in students:
        print("----------------")
        print("Name:", s["name"])
        print("Roll:", s["roll"])
        print("Branch:", s["branch"])
        print("Marks:", s["marks"])


# Search Student
def search_student():
    roll = input("Enter Roll Number: ")

    for s in students:
        if s["roll"] == roll:
            print("\nStudent Found")
            print("Name:", s["name"])
            print("Branch:", s["branch"])
            print("Marks:", s["marks"])
            return

    print("Student Not Found")


# Delete Student
def delete_student():
    roll = input("Enter Roll Number to Delete: ")

    for s in students:
        if s["roll"] == roll:
            students.remove(s)
            print("Student Deleted Successfully")
            save_file()
            return

    print("Student Not Found")


# Update Student
def update_student():
    roll = input("Enter Roll Number to Update: ")

    for s in students:
        if s["roll"] == roll:
            print("Leave blank if you don't want to change")

            name = input("New Name: ")
            branch = input("New Branch: ")
            marks = input("New Marks: ")

            if name != "":
                s["name"] = name
            if branch != "":
                s["branch"] = branch
            if marks != "":
                s["marks"] = marks

            save_file()
            print("Student Updated Successfully")
            return

    print("Student Not Found")


# Save all data to file
def save_file():
    file = open("students.txt", "w")

    for s in students:
        file.write(s["name"] + "," + s["roll"] + "," + s["branch"] + "," + s["marks"] + "\n")

    file.close()


# Menu System
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Update Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        update_student()

    elif choice == "6":
        print("Program Exited")
        break

    else:
        print("Invalid Choice")