
fname = str(input('Enter your First Name: '))
lname = str(input('Enter your Last Name: '))
age = int(input('Enter your Age: '))
fullname = fname + ' ' +lname
print(' ')

print('Full Name:' , fullname)
print('Sliced Name:', (fullname[:4]))
print('Greeting Message:','Hello,', (fullname[:4])+'!','Welcome. You are', age , 'years old.' )