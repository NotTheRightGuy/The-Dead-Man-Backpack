def linearSearch(L,x):
    for i in L:
        if i == x:
            return True
    return False


l = [45,23,10,20,89,100,43]

a = linearSearch(l,43)
print(a)

b = linearSearch(l,10)
print(b)

print(linearSearch(l,42))
