def check_triangle(num,num1,num2):
    if num + num1 > num2 and num1 + num2 > num and num2 + num > num1:
        print ('its can form a triangel')
        if num == num1 == num2:
            print('It is a equilateral Triangle')
        elif num == num1 or num1 == num2 or num2 == num:
            print('it is a  Isosceles Triangle')
        else:
            print ('It is a Scalene Triangle')
        if (num**2 + num1**2 == num2**2) or  (num1**2 + num2**2 == num**2) or (num2**2 + num1**2 == num1**2):
            print('Is is a right angle triangle')
        else:
            print('Is is not right angle triangle')
    else:
        print('it can not from a  triangle')
num  = int(input("Enter a Number: "))
num1 = int(input("Enter a Number: "))
num2 = int(input("Enter a Number: "))
check_triangle(num,num1,num2)
