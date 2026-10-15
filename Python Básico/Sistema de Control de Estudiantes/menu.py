from actions import add_new_student, delete_student, get_top_three_students, read_all_students_average, read_top_three, show_failing_students
from data import read_csv_file,create_csv_file,show_csv_file, export_students, import_students

def main_menu():
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
                reader = read_csv_file("my_students.csv")
                my_students = add_new_student()
                reader.extend(my_students)
                ask_to_save = input("Press ENTER to save changes: ")
                if ask_to_save == '':
                    create_csv_file(reader, "my_students.csv")
                    continue
                else:
                    continue
            elif my_option == 2:
                show_csv_file("my_students.csv")
                input("\nPress ENTER to return to the main menu: ") 
                continue
            elif my_option == 3:
                read_top_three(get_top_three_students("my_students.csv"))
                input("\nPress ENTER to return to the main menu: ") 
                continue                   
            elif my_option == 4:
                read_all_students_average("my_students.csv")
                input("\nPress ENTER to return to the main menu: ") 
                continue
            elif my_option == 5:
                export_students("my_students.csv", "exported_students.csv")
                input("\nPress ENTER to return to the main menu: ") 
                continue
            elif my_option == 6:
                import_students("exported_students.csv", "my_students.csv")
                input("\nPress ENTER to return to the main menu: ") 
                continue
            elif my_option == 7:
                print("Delete student")
                delete_student("my_students.csv")
                input("\nPress ENTER to return to the main menu: ")
                continue
            elif my_option == 8:
                show_failing_students("my_students.csv")
                input("\nPress ENTER to return to the main menu: ")
                continue
            elif my_option == 9:
                print("Exiting the program...")
                break
            else:
                print("Not a valid option try again\n")
                continue
        except ValueError:
            print("Not a valid option try again\n")
            continue