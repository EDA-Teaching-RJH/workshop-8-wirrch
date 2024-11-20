def main():
    write_to_csv()

def write_to_csv():
    with open("data.csv", "w") as file:
        number_of_students = int(input("Enter number of students: "))
        data = []

        for student_index in range(number_of_students):
            student_name = input(f"Enter student {student_index} name: ")
            student_age = input(f"Enter student {student_index} age: ")
            student_grade = input(f"Enter student {student_index} grade: ")

            temp_dict = {
                "name": student_name,
                "age": student_age,
                "grade": student_grade
                }

            data.append(temp_dict)

        file.write(str(data))

def read_from_csv():
    

if __name__ == "__main__":
    main()
