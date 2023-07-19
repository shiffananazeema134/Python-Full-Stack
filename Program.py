# Python Programming

"""
1. One line Programs
2. Pyramid Program
3. Ramdom Password Generate
4. Reverse
5. Palindrome
6. Swap the Value
7. Display Calender
8. Odd or Even
9. Fizz Buzz
10. Fibonacci Series
11. Prime Number

"""
# 1 - One Line Programs
"""

1. Swap two variables
	
a, b = b, a


2. List Comprehension
	
squares = [i*i for i in range(10) if i % 2 == 0]

squares = [i*i for i in range(10) if i % 2 == 0]
print(squares)
[0, 4, 16, 36, 64]


3. If-Else Ternary Operator
	
var = 42 if 3>2 else 99
	
 
4. Print without new line
    
data = [0, 1, 2, 3, 4, 5]
print(*data)
    
    
5. Days left in Year
    
import datetime;
print((datetime.date(2022,12,31)-datetime.date.today()).days)


6. Reversing or Palindrom

a = "level"
print(a[::-1])


7. Multiple Variables Assigning

name, age, language = "Shiffana", 23, "Python"


8. 
"""


# 2 - Star/Pyramid Program
"""
for i in range(1,10):
    print("* " * i)
"""

# 3 - Random Password Generate
'''
import random
lower="abcdefghijklmnopqrstuvwxyz"pyt
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"
symbol="!@#$%^&*(){}[];:<>.,/?"

all=lower+upper+number+symbol
length=10
password= "".join(random.sample(all,length))
print("Password: "+password)
'''

#4 - Reverse
'''
a = 'Shiffana Nazeema A'
rev = "".join(reversed(a))
print(rev)

//

a = input("Enter the Sentence: ")
rev = "".join(reversed(a))
print(rev)
'''

#5 - Palindrome
'''
a = 'madam'
rev = "".join(reversed(a))
if (a == rev):
  print("It is a Palindrome")
else:
    print("It is not a Palindrome")

//

a = input("Enter the Word: ")
rev = "".join(reversed(a))
if (a == rev):
  print("{0} is a Palindrome".format(a))
else:
    print("{0} is not a Palindrome".format(a))
'''

# 6 - Swap the Values
'''
a = input('Please enter value for A:')
b = input('Please enter value for B:')
temp = a
a = b
b = temp
print("The Value of A after Swapping: ",a)
print("The Value of B after Swapping: ",b)
'''

# 7 - Display Calender
'''
import calendar
yy = int(input('Enter Year: '))
mm = int(input('Enter Month: '))
print(calendar.month(yy, mm))
'''

#8 - Odd or Even
'''
num = int(input("Enter a number: "))  
if (num % 2) == 0:  
   print("{0} is Even number".format(num))  
else:  
   print("{0} is Odd number".format(num))  
'''

#9 - Fizz Buzz
'''
import math
import os
import random
import re
import sys
def fizzBuzz(n):
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


if __name__ == '__main__':
    print("Enter the Number")
    n = int(input().strip())

    fizzBuzz(n)
'''

#10 - Fibonacci Series
'''
a, b = 0, 1
while a < 50:
    print(a, end=',')
    a, b = b, a + b
'''

#11 - Prime Number 
'''
num = int(input())
 
for i in range(2, num):
    if num % i  == 0:
        print("No")
        break
    else:
        print("Yes")
'''


Second Last
'''
if __name__ == '__main__':
    records = {}
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records[name] = score
        
    second_largest_value = sorted(set(records.values()))[1]
    for i, j in sorted(records.items()):
        if j==second_largest_value:
            print(i)
'''
