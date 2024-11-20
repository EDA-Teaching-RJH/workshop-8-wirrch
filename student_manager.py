def add_student(name, age, grade):
    with open("students.txt", "a") as file:
        file.write(f"{name},{age},{grade}\n")

def display_students():
    with open("students.txt", "r") as file:
        lines = file.readlines()
    for line in lines:
        print(line)

def main():
    add_student(input("Enter name: "), input("Enter age: "), input("Enter grade: "))
    display_students()

if __name__ == "__main__":
    main()