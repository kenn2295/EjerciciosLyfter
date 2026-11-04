from actions import add_new_student, delete_student, get_top_three_students, read_all_students_average, read_top_three, show_failing_students,show_csv_file
from data import export_students, import_students

def main_menu():
    export_file = "exported_students.csv"
    students_list = []
    while True:
        print("Main menu")
        print("1 - Add new student")
        print("2 - show all students")
        print("3 - ranking")
        print("4 - averages")    
        print("5 - export students")
        print("6 - import students")    
        print("7 - delete student")
        print("8 - Failing students")
        print("9 - Exit")
        try:
            my_option = int(input("Select one option: "))
            if my_option == 1:
                add_new_student(students_list)
            elif my_option == 2:
                show_csv_file(students_list)
                input("\nPress ENTER to return to the main menu: ") 
            elif my_option == 3:
                read_top_three(get_top_three_students(students_list))
                input("\nPress ENTER to return to the main menu: ")                                    
            elif my_option == 4:
                read_all_students_average(students_list)
                input("\nPress ENTER to return to the main menu: ")

            elif my_option == 5:
                export_students(students_list, export_file)
                input("\nPress ENTER to return to the main menu: ") 
            elif my_option == 6:
                import_students(students_list, export_file)
                input("\nPress ENTER to return to the main menu: ") 
            elif my_option == 7:
                print("Delete student")
                delete_student(students_list)
                input("\nPress ENTER to return to the main menu: ")
            elif my_option == 8:
                show_failing_students(students_list)
                input("\nPress ENTER to return to the main menu: ")
            elif my_option == 9:
                print("Exiting the program...")
                break
            else:
                print("Not a valid option try again\n")
        except ValueError:
            print("Not a valid option try again\n")