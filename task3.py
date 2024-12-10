#! python3
"""
Ask the user to enter in a number.
Have them repeat this until the number is an even integer.
(2 marks)


inputs:
    float number

outputs:
    That is an even integer
    That is not an even integer

Examples:
Enter number:1.3
That is not an even integer
Enter number:4
That is an even integer

"""

Integer = False

while not Integer:
    i = input("enter a number: ")
    i = float(i)
    if i%2!=0 or i != int(i):
        print("That is not even integer")
    else:
        Integer = True

print("That is an even integer")