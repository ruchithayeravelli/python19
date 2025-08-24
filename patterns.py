# ###########################
# *
# * *
# * * *
# * * * *
# * * * * *
n = 5 
for  i in range(1,n + 1):
    for j in range(1,i-1):
        print("*",end="")
    print()
# ORRRRRRRRRRRRRRRRRRRR
n = 5
for i in range(1,n + 1):
    print("*"* i)
# ###################################
# revrsing the code
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 
n = 5 
for  i in range(1,n + 1):
    for j in range(1,n-i+2):
        print("*",end="")
    print()
# ###################
n = 5
for i in range(n,0,-1):
    print("*"* i)
#     When i = 1: range(1, 6) → j runs 1..5 → prints 5 stars
# When i = 2: range(1, 5) → j runs 1..4 → prints 4 stars
# When i = 3: range(1, 4) → j runs 1..3 → prints 3 stars
# When i = 4: range(1, 3) → j runs 1..2 → prints 2 star
# When i = 5: range(1, 2) → j runs 1..1 → prints 1 star
# ✅ Output pattern:
n = 5
for i in range(1,n + 1):
    print("*",* i)
# #####################################
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
n = 5
for i in range(1,n + 1):
    for j in range(1,n + 1):
        print("*",end = " ")
    print()
# ###################
# * * * * * 
# *       *
# *       *
# *       *
# * * * * *
n = 5 
for  i in range(1,n + 1):
    if i == 1 or i == 5:
        print("* "* n)
    else:
        print("* "+"  "*(n-2)+"*") 
# "* " step-1
# This prints one star at the beginning.
# Notice there is a space after * so the stars look neat.
# " "*(n-2) step -2
# " " is two spaces.
# Multiplying it by (n-2) means → print empty space between first and last star.
# Example: if n = 5, then " "*(5-2) = " "*3 → 6 spaces.
# "*" step-3
# Adds the last star at the end of the line.