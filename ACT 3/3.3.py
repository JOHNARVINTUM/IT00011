lname = input('Enter your Last Name: ')
fname = input('Enter your First Name: ')
age = input('Enter your Age: ')
cnum = input('Enter Contact Number: ')
course = input('Enter Course: ')
formatted_info = (
    f"Last Name: {lname}\n"
    f"First Name: {fname}\n"
    f"Age: {age}\n"
    f"Contact Number: {cnum}\n"
    f"Course: {course}\n\n"
)
with open("C:\\Users\\John Arvin\\Downloads\\TECHNICALS\\student.txt", 'a') as openfile:
    openfile.write(formatted_info)
print("Student information has been saved to 'student.txt'.")
