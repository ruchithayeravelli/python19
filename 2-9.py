# list_1 = [1, 2, 3, 4, 5]
# list_1.pop(1)
# list_1.pop()
# print(list_1)
# # remove = 
l =[2, 1, 3, 2, 3, 2]
tar = 2
for i in l:
    l.remove(tar)
print(l)
for i in range(len(l)):
    if l[i] == tar:
        l.pop(i)
print(l)


