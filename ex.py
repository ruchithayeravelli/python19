print('hello')
# PROBLEM SLOVING QUEESTIONS
# IF AND ELSE
# 1111111111111111
# Write a program to check if a given number is positive, negative, or zero. 
def check_positive_negative(num):
    return 'Positive' if num > 0 else 'negative' if num < 0 else 'zero'
res =  check_positive_negative(0)
print(res)
#ORRRRR
def check_positive_negative(num):
    if num > 0:
        return 'Positive'
    elif num < 0:
        return 'negative' 
    else:
        return 'Zero'
res =  check_positive_negative(0)
print(res)
# 2222222222222222222
##Determine if a number is odd or even
def odd_even(num):
    if num % 2 == 0:
        return('Its is Even')
    else:
        return('Its is Odd')
num = int(input("Enter a Number:"))
res = odd_even(num)
print(res)
#ORRRRRRRR
def odd_even(num):
    return 'Even' if num % 2 == 0 else 'Odd'
num = int(input('Enter a Numner:'))
res = odd_even(num)
print(res)
# 33333333333333333333
# Check if a person is eligible to vote (age >= 18)
#Check if a person is eligible to vote (age >= 18)
def check_age(age):
    return 'Can you vote' if age >= 18 else 'i can not bye'
age = int(input('Enter The age:'))
res = check_age(age)
print(res)
#ORRRRRRRRR
def check_age(age):
    if age >= 18:
        return 'Can you vote'
    else:
        return('i can not bye')
age = int(input('Enter The age:'))
res = check_age(age)
#ORRRRRRRRR
age = int(input("Enter the age: "))
print("Can you vote" if age >= 18 else "I cannot, bye")
print(res)
#444444444444444444444444444444444
## Write a program to find the greatest of two numbers
def greates_number(a,b,c):
    if  a > b and a > c:
        return f'{a} a is greater than b,c'
    elif b > c :
        return f'{b} is greater than a,c'
    else:
        return f'{c} is greater than b,a'
a = int(input("Enter the number:"))
b = int(input("Enter the number:"))
c = int(input("Enter the number:"))
res = greates_number(a,b,c)
print(res)
#55555555555555555555555555555555555
# Print "Pass" if a student scores more than 40 marks otherwise, print "Fail."  
def student_score(marks):
    return 'Pass' if marks >= 40 else 'Fail'
marks = int(input('Enter the marks:'))
res = student_score(marks)
print(res)
# ORRRRRRRRRR
marks = int(input('Enter the marks:'))
print('pass' if marks >= 40 else 'Fail')
# 66666666666666666666666666
#Write a program to display the day of the week based on a number input (1 for Monday, 2 for Tuesday, etc.).
def week(a):
    if a == 1:
        return ("Monday")
    elif a == 2:
        return ("Tuesday")
    elif a == 3:
        return ("Wednesday")
    elif a == 4:
        return ("Friday")
    elif a ==5:
        return ("Saturday")
    elif a ==7:
        return ("Sunday")
    else:
        return("Invalid") 
a = int(input("Enter the number:"))
res = week(a)
print(res)
# 7777777777777777777777777777
#plement a simple calculator to perform addition,subtraction, multiplication, and division. 
def calculator(op,op1,op2):
    if op == '+':
        return (op1 + op2)
    elif op == '-':
        return (op1 - op2)
    elif op == '*':
        return (op1 * op2)
    else :
        if op2 != 0:
            return (op1 / op2)
        else:
            return 'Cant defined'
op = input('enter the operater:')
op1 = int(input('Enter the number1:'))
op2 = int(input('Enter the number2:'))
res = calculator(op,op1,op2)
print(res)
# 888888888888888888888888888888888
#Write a program to display the name of a month based on the month number (1 for January, 2 for February, etc.). 
def month(a):
    if a == 1:
       return('Jan')
    elif a == 2:
       return('Feb')
    elif  a == 3:
       return('Mar')
    elif  a == 4:
        return('Apr')
    elif a == 5:
        return('May')
    elif a == 6:
        return('Jun')
    elif a == 7:
        return('July')
    elif a == 8:
        return('Aug')
    elif a == 9:
        return('Sep')
    elif a == 10:
        return('Oct')
    elif a == 11:
        return('Nov')
    elif a == 12:
        return('Dec')
    else:
        return('Invalid')
a = int(input('Enter the number(1-12):'))
res = month(a)
print(res)
# MEDIUM questions
# 1111111111111111111111111
# # Write a program to find the greatest of three numbers.
def greter(a,b,c):
    if a > b and a > c:
        return f'{a} is gretaer then b and c'
    elif b > c:
        return f'{b} is gretaer then a and c'
    else:
        return f'{c} is gretaer then b and a'
a = int(input('Enter the Number:'))
b = int(input('Enter the Number:'))
c = int(input('Enter the Number:'))
res = greter(a,b,c)
print(res)
# 2222222222222222222222222
# Check if a year is a leap year. 
def leap(year):
    if year % 400 == 0 or year % 100 != 0 and year % 4 == 0:
        print('It is leap year')
        return
    else:
        print('Non leap year')
        return
year = int(input('Enter the year:'))
res = leap(year)
print(res)
# 333333333333333333333333333
# Write a program to classify a character entered by the user as a vowel, consonant, or neither. 
def vowel(alph):
    if alph in 'aeiou':
        return('Its is vowel')
    elif alph.isalpha():
        return('Its is a constant')
    elif alph.isnumeric():
        return ('Its is a number')
    else:
        return ('Neither anything')
alph = input('Enter a voewl or constant or nither')
res = vowel(alph)
print(res)
# 4444444444444444444444444444
# alculate the grade of a student based on the marks they score: 
# 1.  90-100  : Grade A 
# 2.  80-89  : Grade B 
# 3.  70-79  : Grade C 
# 4.  <70  : Fail. 
def grade(gra):
    if gra >= 90 and gra <= 100:
        return('Grade A')
    elif gra >= 80 and gra <= 89:
        return('Grade B')
    elif gra >= 70 and gra <= 79:
        return('Grade C')
    else:
        return('Fail')
gra = int(input('Enter the Marks:'))
res = grade(gra)
print(res)
# 5555555555555555555555555555555555
# Write a program to check if three sides length form a valid triangle.
def triangle(s1,s2,s3):
    if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
        return('It can form a triangle')
    else:
        return('It can not form a triangle')
s1 = int(input('Enter a Number side1:'))
s2 = int(input('Enter a Number side2:'))
s3 = int(input('Enter a Number side3:'))
res = triangle(s1,s2,s3)
print(res)
# LOOPS
# shorttttttt
# 1111111111111111111111
#  Print all numbers from 1 to 100 using a  for  loop.
def primenumbers(n):
    for i in range(n,101):
        print(i)
n = int(input('Enter the number'))
res = primenumbers(n)
print(res)
# 22222222222222222222222222222
#  Write a program to print the sum of the first  n  natural numbers. (n*n+1/ 2)
def natural(n):
    sum = 0
    for i in range(1,n+1):
        sum = sum + i
    return sum
n =int(input('Enter the n:'))
res = natural(n)
print(res)
# ORRRRRRRRRRRRRRRRR
# Write a program to print the sum of the first  n  natural numbers. 
#   (n*n+1/ 2)
def natural(n):
    for i in range (n,n + 1):
        sum = (n * (n + 1) / 2)
    return int(sum)
n = 4
res = natural(n)
print(res)
# 3333333333333333333333333333333333
# Print all even numbers between 1 and 50 using a  while loop. 
start = 1
while start <= 50:
    if start % 2 == 0:
        print(start,end=" ")
    start += 1
#44444444444444444444444444444444444444
# # Write a program to display the multiplication table of a given number. First 20 
n = 2
print('MULTILICATION TABLE')
for i in range (1,21):
     print(n,'X',i,'=',n * i)
# 555555555555555555555555555555555555555
# # Rverse a number using a  while  loop. 
# 1.  Also can we get the sum of all the digits. 
res = '12345A'   #It is in string so do not convert to string again
#  if string given in int form so convert to string
print((res)[::-1]) 
# ORRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
# Rverse a number using a  while  loop. 
# 1.  Also can we get the sum of all the digits. 
n = int(input('Enter the number:'))
rev,sum = 0 ,0
while n > 0:
    digit = n % 10         # prints last digit
    rev = rev * 10 + digit # prints the last digit 
    sum += digit           # sum the digit
    n //= 10
print(rev)
print(sum)
# 66666666666666666666666666666666666
# 