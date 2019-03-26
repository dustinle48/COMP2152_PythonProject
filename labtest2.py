import os
PATH = os.path.dirname(os.path.realpath(__file__))
FILENAME = "out.txt"

def add_student():
    studentid = input("Please enter student ID: ")
    firstname = input("Please enter first name: ")
    lastname = input("Please enter last name: ")
    major = input("Please enter major: ")
    phone = input("Please enter phone: ")
    gpa = input("Please enter gpa: ")
    birth = input("Please enter date of birth: ")
    student = [studentid + " ", firstname + " ", lastname + " ", major + " ", phone + " ", gpa + " ", birth]
    with open(FILENAME, "a") as file:
        for n in student:
            file.write(n)
        file.write("\n")

def read_student():
    id = input("Please enter the ID of the student you are looking for: ")
    student = []
    with open(FILENAME, "r") as file:
        for line in file:
            line = line.replace("\n", "")
            student.append(line)
    matching = [s for s in student if id in s]
    print(matching)

def action():
    print("Welcome to Student Manager 1.0")
    print("------------------------------")
    print("Use Add command to add student.")
    print("Use Read command to read student information.")
    print("Use Exit command to exit.")
    print("------------------------------")

def main():
    action()
    while True:
        command = input("Please enter a command: ")
        if command.lower() == "add":
            add_student()
        elif command.lower() == "read":
            read_student()
        elif command.lower() == "exit":
            break
        else:
            print("Invalid command")
    print("------------------------------")
    print("Bye!")

if __name__ == "__main__":
    main()
