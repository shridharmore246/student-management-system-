# Student Management System

students = []

def add_student():
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")

    student = {
        "name": name,
        "roll_no": roll_no
    }

    students.append(student)
    print("Student added successfully!")

def display_students():
    if not students:
        print("No students found.")
    else:
        print("\nStudent Records:")
        for student in students:
            print(student)

def main():
    while True:
        print("\n1. Add Student")
        print("2. Display Students")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_students()
        elif choice == "3":
            print("Thank you!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
