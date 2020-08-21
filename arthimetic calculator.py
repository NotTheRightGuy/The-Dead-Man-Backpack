def add():
    x = int(input('Enter your first number: '))
    y = int(input('Enter your second number: '))
    print(x+y)

def sub():
    x = int(input('Enter your first number: '))
    y = int(input('Enter your second number: '))
    print(x-y)

def mul():
    x = int(input('Enter your first number: '))
    y = int(input('Enter your second number: '))
    print(x*y)

def div():
    x = int(input('Enter your first number: '))
    y = int(input('Enter your second number: '))
    print(x/y)

def pow():
    x = int(input('Enter your number: '))
    y = int(input('Raise number to the power of: '))
    print(x**y)

def sqrt():
    x = int(input('Enter your number: '))
    print(x**1/2)

while True:
    print("""
Welcome the calulator 101
You may use Add, Sub, Div, Mul, Pow, sqrt for Addition, Subtraction, Divison, Multiplication, Exponents, and to find square root respectively"
""")
    response = input("Enter your response: ")
    response = response.lower()
    if response == 'add':
        add()
    elif response == 'sub':
        sub()
    elif response == 'mul':
        mul()
    elif response == 'div':
        div()
    elif response == 'pow':
        pow()
    elif response == 'sqrt':
        sqrt()
    else:
        print("Invalid Respone")
        break
