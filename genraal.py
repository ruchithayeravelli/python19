#  for printing  abc pattern
text = 'ABCDEFGHIJKLMNO'
index = 0
for i in range(1,6):
    for j in range(i):
        if index < len(text):
            print(text[index], end=" ")
            index += 1
    print()
    # output
# A 
# B C 
# D E F 
# G H I J 
# K L M N O 
# A * * * *
# B C * * * 
# D E F * *
# G H I J *
# K L M N O 
n = 5
# ch = 65
for i in range(1,n+1):
    for j in range(i):
        print('*', end =" ")
        # ch += 1
    print()
n = 5
ch = 65
for i in range(1,n+1):
    for j in range(i):
        print(chr(ch), end =" ")
        ch += 1
    print()
# ########################################
# def gcd(a, b):
#     gcd_value = 1
#     for i in range(1, min(a, b) + 1):
#         if a % i == 0 and b % i == 0:
#             gcd_value = i
#     return gcd_value

# print("GCD of 56 and 78 is:", gcd(56, 78))
# ######################33
import math
a = 12
b = 22
print((a * b)// math.gcd(a,b))
