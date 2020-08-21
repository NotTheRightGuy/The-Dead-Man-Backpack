Pass By Reference
def updateList(list1):
    print(list1)
    list1 += [10]
    print(list1)

n = [50, 60]
print(n)
updateList(n)
print(n)

Pass by Value
def updateNumber(n):
    print(n)
    n += 10
    print(n)

b = 5
print(b)
updateNumber(b)
print(b)



# Function with parameter with return
def add (x, y):
    z = x + y
    return z

print('Hello')
a = int(input('Enter a:'))
b = int(input('Enter b:'))
c = add(a,b)
print('The result is',c)
print('Bye')



# Function with parameter with return
def sub(x, y):
    z = x - y
    return z
