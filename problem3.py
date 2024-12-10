#! python3
"""
The Fibonacci sequence was created to model how populations
of bunnies increase over time.  It is also used in strategies
that prolong how long you can play Blackjack before you 
eventually lose all your money.
It follows a pattern where the last two number are added 
together to make the next number, starting with 1 1:
Create a program to show the Fibonacci sequence, stopping
after the number in the sequence is greater than 100:
(2 points) 

Example:
1 1 2 3 5 ...
"""

Fibonacci = False
x = 0
y = 1
print (1)

while not Fibonacci:
    z = y+x
    if z > 100:
        break
    print(z)
    x = y+z
    if x > 100:
        break
    print(x)
    y = z + x
    if y > 100:
        break
    print(y)

