##### Problem 1
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:
username: admin
password: 12345
If they guess more than 3 times, they are not allowed to guess
any more and the program will end.
(2 marks)

inputs:
str username
str password

outputs:
Access granted
Access denied

example:
example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 1234
Access denied
Too many failed attempts. Access denied.
"""

username = False
password = False
count = False
x = 0

while not username and not password and not count:
    eu = input("enter username: ")
    ep = input("enter password: ")
    x = x+1
    if x >= 3:
        print("Too many failed attempts. Access denied")
        count = True
    else:
        if eu != "admin" or ep != "12345":
            print("access denied")
        else:
            username = True
            password = True
            print("access granted")

