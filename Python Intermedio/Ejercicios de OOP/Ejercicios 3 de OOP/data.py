import csv
from actions import Student

def read_csv_file(path):
    try:
        with open(path,"r",encoding='utf-8',newline='') as file:
            students_list = csv.DictReader(file)
            return list(students_list)
    except FileNotFoundError:
        return None
    
def create_csv_file(students_list, path):
    students_dict = []
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
        for student in students_list:
            students_dict.append({
                "Full name": student.full_name,
                "Section": student.section,
                "Spanish grade": student.spanish_grade,
                "English grade": student.english_grade,
                "Social grade": student.social_grade,
                "Science grade": student.science_grade
            })
        writer.writerows(students_dict)
    print("\nFile created successfully\n")

def export_students(students_list, destination_path):
    if not students_list:
        print("\nNo students found to export.")
        return
    print(f"EXPORT STUDENTS")
    ask_to_export = input("\nPress ENTER to export the file: ")
    if ask_to_export == '':
        create_csv_file(students_list, destination_path)
        print(f"\nStudents exported successfully")
    else:
        print("\nExport cancelled.")

def import_students(students_list, source_path):
    imported_students = read_csv_file(source_path)
    if imported_students is None:
        print("\nFile not found.")
        return
    if not imported_students:
        print("\nNo students found to import.")
        return
    ask_to_import = input("\nPress ENTER to import the file: ")
    if ask_to_import == '':
        students_list.clear()
        for student in imported_students:
            my_student = Student(student["Full name"],student["Section"],int(student["Spanish grade"]),int(student["English grade"]),int(student["Social grade"]),int(student["Science grade"])) 
            students_list.append(my_student)
        print("\nStudents imported successfully.")
    else:
        print("\nImport cancelled.")

