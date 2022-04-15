a = []
# b = list()
# print (type(a))
# print (type(b))

# for i in range (1,21):
#     if i % 5 == 0:
#         a.append(i)

b =[i for i in range (1,21)  if i % 5 == 0 ]
print(b)
b = [1,2,3]
# b *= 3
# print(b)


#a.extend(b)
a = a + b
print(a)
print(a[1])

print(a[2:4])

print(a[::-1])

# a.remove(10)
del a [2]  #delete value in list
print(a)

#######   set   #######
 
a = [1, True , "hello" , {1,2,3}] #takes any data types
b = {1, 2 , "apple", True}

print(b)
