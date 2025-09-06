# add
# remove - if elemnrnt is not theer it through an errorr
# discord - if no element ntg get error
# pop
# union
# intersection
# differenece
# symmetric diff - common elements evadhu
# disjoint set - no common point
# /subset
# superset
# set{} -- dict empty set
# set(2, 3, 4,)--- set type
# list in side set - not possible
# set inside a set - not passibele
# set loo  forzen set we can
# tuple - immutablee we can set in side tuple
# list - mutable
# set() -- empty set
# duplicate not possible
set133 = {2,3,4,(1,2,3)}
set133.add(2)
print(set133)
# set1.remove(2)
# key error
# incase lekapothye discord error through cheyadhu but remove can throgh an error
# ########## pop
fruits = {"apple", "banana", "cherry", "mango"}
print("Original set:", fruits)
removed = fruits.pop()
print("Removed element:", removed)
print("Set after pop:", fruits)
# pop will give random output but will pop in pattern
#  list loos same will get but not in list
# symmentric  - common elements ravu
set1 = {1,2,3,4,5,6}
set2 = {5,6,7,8,9,10}
print(set1.symmetric_difference(set2))
# union or | -> union of sets
# deff set - set3
# ################################ 
# in membership operater

tup1 = (1,2,3,4)
tup1 += (5,6)
print(tup1)
# tuple reassesment is possible

# append extend insert ->list can possible but tuple does not possbile
# before 3.7 is dict is unoreder after now it is order
# pop last insert chesina key value pairs pothayi
# sholow copt - related
# deep copy not related
keys = ['a','b','a']
values =[1,2,3]
print(dict(zip(keys,values)))
# {'a': 3, 'b': 2}