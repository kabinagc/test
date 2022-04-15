#i = 1

#while i <= 20:
 #   if i % 2 != 0:
  #      print(i)
   # i += 1

# 


# i = 1
# k = 1
# while i <= 5:
#     j = 1
#     while j <= 1:
#         print("*", end=' ')
#          j += 1
#     print()
#     i += 1
# k = 1
# while k <= 5:
#     print("*",k)
#      k += 1


# #range(start, end , incrementer/decrementer)
# for i  in range(5,1,-1):
#     #print (i)
#     pass

# string = input("Enter a string")
# string = string.lower()
# vowels = 0
# for i in string:
#     if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
#         vowels += 1
# print("number of vowel are:")
# print (vowels)   

# str= "Hello world"
# print(str[0])
# print(str[-1])


# str = input("Enter a string")
# new_str = ''
# for i in range(1 ,len(str)):
#     new_str += str[-i]
# print(new_str)


# print("=========================")
# new_str = ""
# for i in range(len(str)-1,-1,-1):
#     new_str += str[i]
# print(new_str)

# new_str = "".join(reversed(str))
# print(new_str)

#print(str[::-1])

#  string = "ABaBCbGc"
#  counts = {}
#  for c in string.upper():
#      counts[c] = counts.get(c, 0) + 1

#  print(counts)



# num = int(input("Enter a number: "))
# order = len(str(num))
# sum = 0
# temp = num
# while temp > 0:
#    digit = temp % 10
#    sum += digit ** order
#    temp //= 10
# if num == sum:
#    print(num,"is an Armstrong number")
# else:
#    print(num,"is not an Armstrong number")



# num = int(input("Enter a number:"))
# temp = num
# rev = 0
# while(num>0):
#    digit = num % 10
#    rev = rev*10 + digit
#    num = num // 10
# if(temp == rev):
#    print("The number is Palindrome")
# else:
#    print("The number is not a Palindrome")



