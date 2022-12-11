def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

print(greatest(100,40,30))


# function inside function
def new_greatest (a,b,c):
    bigger =greatest(a,b)
    return greatest(bigger,c)
print(new_greatest(1000,200,30))