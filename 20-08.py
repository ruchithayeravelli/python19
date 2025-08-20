# LOOPs
# 2 question Sum of first n natural number
int =int(input("entera number"))
sum = 0
for i in range(1,int+1):
    # sum + i
    # updation to sum
    sum = sum + i
    # 0+1=1,1+2=3,3+3=6,6+4=10
    # without decimal
print(sum)
# using mathematical formula fro fastest time  efficinecy 
# withpoint
print((int * (int+1))/2)
# n(n+1(2n+1))/6
# sum = summ+ i**2
# above two comments for sum of n natural numbers
# 3 quation
# even numbers
for i in range(1,51):
    if i % 2 == 0:
        print(i)
#Multiplication table 1-20
num=2
for i in range(1,21):
    print(num,"X",i,"=",num*i)
# 7
# num_1 = int(input("Enter a number:"))
# while num_1 > 0:
#     print("It is postive number")
#     if num_1 <= 0:
#         print("It is negative number")
#         break
#5
# choosing menu and printing
while True:
    print('1.square 2.cube 3.Exit')
    choice = input("Enter the choice")

    if choice == '1' or choice == 'square':
        input_num = int(input('Ente the number'))
        print(input_num ** 2)
        
    elif choice == '2' or choice == 'cube':
        input_num = int(input('Ente the number'))
        print(input_num ** 3)

    else:
        print('No valid option')
        print('----exiting-------')
        break
# TASK 3,4,7----------------------------
# Print all numbers from 1 to 100 that are divisible by 3 and 5 in for loop
# start = 1
# while start <= 100:  
#     if start % 3 == 0 or start % 5 == 0:
#         print(start)
#     start += 1  
for i in range(1,101):
    if i % 3 == 0 or i % 5 == 0:
        print(i)






