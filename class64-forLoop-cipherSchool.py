#practice for loop 
#ask user a number like 1256
# calculate sum of digits ---> 1+2+5+6

total = 0 
num = input("enter a number : ")
for i in range (0, len(num)):
    total +=  int(num[i])
print(total)


# practice for loop 
# ask user name and count each character
# "harshit Vashisth"
# H : 1
# a : 2
# r : 1
# s : 3
# h : 3
name = input("enter your name : ")
temp = ""
for i in range (len(name)) :
    if name [i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i]


