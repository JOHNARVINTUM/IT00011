import csv

records = []
filename = ""

def open_file():
    global records, filename
    filename = input("Enter filename: ")
    try:
        with open(filename, newline='') as file:
            reader = csv.reader(file)
            records = [tuple(row) for row in reader]
        print("File opened successfully.")
    except FileNotFoundError:
        print("File not found.")

def save_file():
    if not filename:
        print("No file loaded.")
        return
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for record in records:
            writer.writerow(record)
    print("File saved.")

def save_as_file():
    global filename
    filename = input("Enter new filename: ")
    save_file()

def show_all_records():
    for record in records:
        print(record)

def order_by_lastname():
    global records
    records.sort(key=lambda x: x[1])
    show_all_records()

def order_by_grade():
    global records
    records.sort(key=lambda x: (float(x[2]) * 0.6 + float(x[3]) * 0.4), reverse=True)
    show_all_records()

def show_student_record():
    student_id = input("Enter Student ID: ")
    for record in records:
        if record[0] == student_id:
            print(record)
            return
    print("Student not found.")

def add_record():
    student_id = input("Enter Student ID: ")
    first_name = input("Enter First Name: ")
    last_name = input("Enter Last Name: ")
    class_standing = input("Enter Class Standing: ")
    major_exam = input("Enter Major Exam Grade: ")
    records.append((student_id, first_name, last_name, class_standing, major_exam))
    print("Record added.")

def edit_record():
    student_id = input("Enter Student ID to edit: ")
    for i in range(len(records)):
        if records[i][0] == student_id:
            first_name = input("Enter new First Name: ")
            last_name = input("Enter new Last Name: ")
            class_standing = input("Enter new Class Standing: ")
            major_exam = input("Enter new Major Exam Grade: ")
            records[i] = (student_id, first_name, last_name, class_standing, major_exam)
            print("Record updated.")
            return
    print("Student not found.")

def delete_record():
    student_id = input("Enter Student ID to delete: ")
    global records
    records = [record for record in records if record[0] != student_id]
    print("Record deleted.")

def menu():
    while True:
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Records")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")
        choice = input("Enter choice: ")
        if choice == '1':
            open_file()
        elif choice == '2':
            save_file()
        elif choice == '3':
            save_as_file()
        elif choice == '4':
            show_all_records()
        elif choice == '5':
            order_by_lastname()
        elif choice == '6':
            order_by_grade()
        elif choice == '7':
            show_student_record()
        elif choice == '8':
            add_record()
        elif choice == '9':
            edit_record()
        elif choice == '10':
            delete_record()
        elif choice == '11':
            break
        else:
            print("Invalid choice.")

menu()
