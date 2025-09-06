# strings
# ############3 count
text = 'banana'
print(text.count('as'))
# startswith
text1= 'banana'
print(text1.startswith('as'))
# endswith
tex = 'ertyuio'
print(tex.endswith('io'))
# count
print(text.count('bana2'))
# replace
v = 'i love coding'
print(v.replace('love','iole'))
# split in listtttttttttttttttttttttttttttttt
# real time usecase(csv file comma spreated values)
# string ----- list
t = 'a,b,c'
print(t.split(','))
h = 'a$b,c'
print(h.split('b'))
# with spaces also will come same as with space
# with space also we can split

num1 = input("enter the number in csv mode").split(',')
print(num1)
# enter the number in csv mode22,33,44,55
# ['22', '33', '44', '55']
# int
list1 =  input("enter the number in csv mode").split(',')
num1, num2 , num3 = map(int, list1)
print(num1,num2,num3)
# num1, num2 , num3 = map(int,  input("enter the number in csv mode").split(','))
# join 
# list - string
li = ['hi','hello','name']
print(','.join(li)) # , is diffrencietaer
print(''.join(li))
###############################################


# ############ set - mutable in set inside set is immuatble
# add(element) -- addd
# remove - if elemnrnt is not theer it through an errorr
# discord - if no element ntg get error
# union
# intersection
# differenece
# symmetric diff - common elements evadhu
# disjoint set - no common point
# /subset
# superset
######################################################################
