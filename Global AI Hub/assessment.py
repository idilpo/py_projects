def adder(*num):
    summ = 0

    for n in num:
        summ = summ + n

    print("Sum:", summ)

adder(1,2,3,4,5,6)


x = lambda a, b, c: a + b + c
print(x(5,6,2))


def f1(z=1, y=2):
    z = z + y
    y += 1
    print(z, y)
f1(y = 2, z = 1)


counter = 1
def doStuff():
    global counter

    for i in (1,2,3):
        counter += 1

doStuff()
print(counter)

''' 
def main():
    try:
        func()
        print("print")
    except ZeroDivisionError():
        print("zero")
    except:
        print("an exc")

def func():
    print(1/0)

main()
'''

def randF(m,k,l):
    m = k+l
    k = m+l
    l = k+m
    return m,k,l

o,p,r =randF(k=5, l=3, m=6)
print(o,p,r)

'''
while True:
    try:
        x = int(input("enter num: "))
        print(x)
        break
    except ValueError:
        print("oops")
'''


def mul1(*args):
    result = 1
    for i in args:
        result *= i
    print(result)
mul1(9,3,0,4)
