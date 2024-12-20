#! python3
"""
Have the user enter a username and password.
Repeat this until both the username and password match the 
following:

username: admin
password: 12345
(2 marks)

inputs:
str (username)
str (password)

outputs:
Access granted
Access denied

example:
Enter username: fred
Enter password: password
Access denied
Enter username: admin
Enter password: password
Access denied
Enter username: admin
Enter password: 12345
Access granted


"""

username = False
password = False


while not username and not password:
    eu = input("enter username: ")
    ep = input("enter password: ")
    if eu != "admin" or ep != "12345":
        print("access denied")
    else:
        username = True
        password = True

print("access granted")