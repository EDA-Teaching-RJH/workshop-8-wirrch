def main():
    add_student(input("Enter name: "), input("Enter age: "), input("Enter grade: "))
    display_students()
    print(find_student(input("Enter student to find: ")))

def add_student(name, age, grade):
    with open("students.txt", "a") as file:
        file.write(f"{name},{age},{grade}\n")

def display_students():
    with open("students.txt", "r") as file:
        lines = file.readlines()
    for line in lines:
        print(line)

def find_student(name):
    with open("students.txt", "r") as file:
        lines = file.readlines()
    for line in lines:
        if line.rsplit(",")[0] == name:
            return line


if __name__ == "__main__":
    main()