# define a function which will take list as a argument and this function 
# will return a reversed list 
# but try to do this with the help of append and pop method
 
# def reverse_list (l):
#     l.reverse()
#     return l

# def reverse_list(l):
#     return l[::-1]

def reverse_list(l):
    r_list = []
    for i in range(len(l)):
        pooped_item = l.pop()
        r_list.append(pooped_item)
    return r_list

numbers = [1,2,3,4]


print(reverse_list(numbers))