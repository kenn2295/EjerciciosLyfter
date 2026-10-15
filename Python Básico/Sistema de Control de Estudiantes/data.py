import csv

def read_csv_file(path):
    try:
        with open(path,"r",encoding='utf-8',newline='') as file:
            students_list = csv.DictReader(file)
            return list(students_list)
    except FileNotFoundError:
        return []
    
def create_csv_file(students_list, path):
    with open(path, "w", encoding='utf-8', newline='') as file:
        headers = [
            "Full name",
            "Section",
            "Spanish grade",
            "English grade",
            "Social grade",
            "Science grade"
        ]
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        writer.writerows(students_list)
    print("\nFile created successfully\n")

def show_csv_file(path):
    try:
        with open(path, "r", encoding='utf-8') as file:
            students_list = list(csv.DictReader(file))
            if not students_list:
                print("\nNo students found to show.")
                return
            print("\nSTUDENT'S LIST:")
            for student in students_list:
                for key, value in student.items():
                    print(f"{key}: {value}")
                print()
    except FileNotFoundError:
        print("File not found.")

def export_students(source_path, destination_path):
    students_list = read_csv_file(source_path)
    if not students_list:
        print("\nNo students found to export.")
        return
    print(f"EXPORT STUDENTS")
    ask_to_export = input("\nPress ENTER to export the file: ")
    if ask_to_export == '':
        warning_before_export = input("Are you sure you want to export the file (y/n): ")
        if warning_before_export.lower() == 'y':
            create_csv_file(students_list, destination_path)
            print(f"\nStudents exported successfully to {destination_path}\n")
        else:
            print("\nExport cancelled.")
    else:
        print("\nExport cancelled.")


def import_students(source_path, destination_path):
    students_list = read_csv_file(source_path)
    if not students_list:
        print("\nNo students found to import.")
        return
    ask_to_import = input(f"\nPress ENTER to import the file: ")
    if ask_to_import == '':
        warning_before_import = input("Are you sure you want to import the file (y/n): ")
        if warning_before_import.lower() == 'y':
            create_csv_file(students_list, destination_path)
            print(f"\nStudents imported successfully to "f"{destination_path}")
        else:
            print("\nImport cancelled.")
    else:
        print("\nImport cancelled.")
        

def find_student(students_list, full_name, section):
    for student in students_list:
        if (student['Full name'].lower() == full_name.lower()
                and student['Section'].lower() == section.lower()):
            return student
    return None

def get_failing_students(path):
    students_list = read_csv_file(path)
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
    return failing_students

