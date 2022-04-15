a = [1,2,3,4,5]
b = [1,21]
#print (b in a)

for i in b:
    if i in a:
        check = True
    else:
        check = False
        break
if (check == True):
    print("B is subset of A")
else:
    print("B is not subset of A")


######################### using set
a = set([1,2,3,4,5])
b = set([1,21])

print(b.issubset(a))



newSet = a.union(b)   ### a | b

#a = [8,9,7,1,2,3,4,5]
#a.sort()
#a = sorted(a)
#a.sort(reverse=True)
a = ["apple","ball","cat","a"]
a.sort()
print(a)

