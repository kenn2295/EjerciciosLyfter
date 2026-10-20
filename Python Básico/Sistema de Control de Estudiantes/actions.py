def add_new_student(students_list):
    while True:
        try:
            amount = int(input("\nEnter the number of students: "))
            if amount <= 0:
                print("Please enter a valid number of students.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    for n in range(1, amount + 1):
        while True:
            print(f"\nEnter the student {n}: ")
            full_name = get_valid_name()
            section = get_valid_section()
            if find_student(students_list, full_name, section):              
                print("This student is already registered in this section.")
                continue
            break
        spanish_grade, english_grade, social_grade, science_grade = get_valid_grades()
        new_student = {
            "Full name": full_name,
            "Section": section,
            "Spanish grade": spanish_grade,
            "English grade": english_grade,
            "Social grade": social_grade,
            "Science grade": science_grade
        }
        students_list.append(new_student)
    return students_list


def get_valid_name():
    while True:
        first_name = input("Enter the First name: ").strip().title()
        if not first_name.isalpha():
            print("Please enter a valid First name.")
            continue
        while True:
            middle_name = input("Enter the middle name (optional): ").strip().title()
            if middle_name == "" or middle_name.isalpha():
                break
            print("Please enter a valid middle name.")
        while True:
            last_name = input("Enter the Last name: ").strip().title()
            if not last_name.isalpha():
                print("Please enter a valid Last name.")
                continue
            break
        while True:
            second_last_name = input("Enter the second last name (optional): ").strip().title()
            if second_last_name == "" or second_last_name.isalpha():
                break
            print("Please enter a valid second last name.")
        if middle_name == "" and second_last_name == "":
            full_name = first_name + " " + last_name
        elif middle_name == "":
            full_name = first_name + " " + last_name + " " + second_last_name
        elif second_last_name == "":        
            full_name = first_name + " " + middle_name + " " + last_name
        else:
            full_name = first_name + " " + middle_name + " " + last_name + " " + second_last_name
        return full_name

def get_valid_section():
    while True:
        section = input("Enter the section: ").strip().upper()
        if section[:-1].isdigit() and section[-1].isalpha():
            return section
        else:
            print("Invalid section. Use numbers followed by one letter. For example: 1A, 2B, 3C.")
        
def get_valid_note(subject):
    while True:
        try:
            grade = int(input(f"Enter the {subject} grade: "))
            if grade < 0 or grade > 100:
                print("Please enter a grade between 0 and 100.")
                continue
            return grade
        except ValueError:
            print("Please enter a valid number.")

def get_valid_grades():
    spanish_grade = get_valid_note("Spanish")
    english_grade = get_valid_note("English")
    social_grade = get_valid_note("Social")
    science_grade = get_valid_note("Science")
    return spanish_grade, english_grade, social_grade, science_grade

def calculate_average(student):
    total = 0
    grades = ["Spanish grade", "English grade", "Social grade", "Science grade"]
    for grade in grades:
        total += float(student[grade])
    average = total / len(grades)
    return round(average, 2)

def get_top_three_students(students_list):
    students_list = students_list.copy()
    students_list.sort(key=calculate_average, reverse=True)
    top_three = students_list[:3]
    return top_three

def read_top_three(top_three):  
    if not top_three:
        print("\nNo students found to show top 3.")
        return
    print("\nTOP THREE STUDENTS:")
    for student in top_three:
        print(f"Name: {student['Full name']}")
        print(f"Section: {student['Section']}")
        print(f"Average: {calculate_average(student):.2f}")
        print()

def read_all_students_average(students_list):
    if not students_list:
        print("\nNo students found to show averages.")
        return
    averages = [calculate_average(student) for student in students_list]
    general_average = sum(averages) / len(averages)
    print(f"\nGENERAL AVERAGE: {general_average:.2f}")
    print("\nAVERAGE OF ALL STUDENTS:")
    for student in students_list:
        average = calculate_average(student)
        print(f"Name: {student['Full name']}")
        print(f"Section: {student['Section']}")
        print(f"Average: {average:.2f}")
        print()

def delete_student(students_list):
    if not students_list:
        print("\nNo students found to delete.")
        return
    full_name = input("Enter the student's full name: ").strip()
    section = input("Enter the student's section: ").strip()
    student = find_student(students_list, full_name, section)
    if student is None:
        print(f"\nStudent '{full_name}' from section '{section}' not found.")
        return
    print(f"\nStudent: {student['Full name']}")
    print(f"Section: {student['Section']}")
    confirmation = input(
        "Are you sure you want to delete this student? (y/n): ").strip().lower()
    if confirmation == "y":
        students_list.remove(student)
        print(f"\nStudent '{full_name}' deleted successfully.")
    else:
        print("\nDeletion cancelled.")

def show_failing_students(students_list):
    failing_students = get_failing_students(students_list)
    if not failing_students:
        return
    grades = [
        "Spanish grade",
        "English grade",
        "Social grade",
        "Science grade"
    ]
    print("\nFAILING STUDENTS:")
    for student in failing_students:
        print(f"\nName: {student['Full name']}")
        print(f"Section: {student['Section']}")
        print("Failed subjects:")
        for grade in grades:
            if float(student[grade]) < 60:
                print(f"{grade}: {student[grade]}")
        print()

def show_csv_file(students_list):
    if not students_list:
        print("\nNo students found to show.")
        return
    print("\nSTUDENT'S LIST:")
    for student in students_list:
        for key, value in student.items():
            print(f"{key}: {value}")
        print()

def find_student(students_list, full_name, section):
    for student in students_list:
        if (student['Full name'].lower() == full_name.lower() and student['Section'].lower() == section.lower()):
            return student
    return None

def get_failing_students(students_list):
    if not students_list:
        print("\nNo failing students found.")
        return []
    grades = [
        "Spanish grade",
        "English grade",
        "Social grade",
        "Science grade"
    ]
    failing_students = []
    for student in students_list:
        for grade in grades:
            if float(student[grade]) < 60:
                failing_students.append(student)
                break
    if not failing_students:
        print("\nNo failing students found.")
    return failing_students