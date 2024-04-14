
"""
This is a staircase of size:
   #
  ##
 ###
####
Its base and height are both equal to n. It is drawn using # symbols and spaces.
The last line is not preceded by any spaces.
Write a program that prints a staircase of size n.
"""

def staircase_to_right(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '#' * i)
def staircase_to_middle(n):
    for i in range(1,n+1):
        print(' ' * (n//2 - i//2) + '#' * i)
def staircase_to_left(n):
    for i in range(1, n+1):
        print("#" * i)

def print_stairs(n):
    staircase_to_right(n)
    print("")
    staircase_to_middle(n)
    print("")
    staircase_to_left(n)
    print("")

print_stairs(4)
print_stairs(int(input("How many steps do you want?\n")))