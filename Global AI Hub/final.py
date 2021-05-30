
num3 = input("1st int: ")
num4 = input("2nd int: ")

try:
    num3_int = int(num3)
    num4_int = int(num4)
    print(num3_int, "/", num4_int, "=", num3_int/num4_int)

except (ValueError, ZeroDivisionError):
    print("Error")


import numpy as np
dm3 = ("Global AI Hub", 5, 8, "september")
dm3.index("september")


x = [[1,8,3],
     [6,5,4],
     [7,2,9]]

y = [[9,2,7],
     [4,5,6],
     [5,10,5]]

res = [[0,0,0],
     [0,0,0],
     [0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        res[i][j] = x[i][j] + y[i][j]

for r in res:
    print(r, end=" ")



tup = (4,3,2,1,0)
lst = [0,1,2,3,4]

def main(tup, lst):
    if tup.index(2) == lst[-3]:
        return True
    else:
        return False
print(main(tup, lst))



t = np.array([[[1,2],
              [3,4],
               [5,6]]])
print(t[[0,0,0], [1,0,1]])



a = np.array([9,10])
b = np.array([11,12])
print(np.dot(a,b))


t = np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])
print(t.shape)


s5 = np.eye(4)
print(s5)



tra = np.array([[20,15,20,29,13],
                [14,5,19,7,10],
                [17,2,4,5,3],
                [6,24,26,13,28]])
print(tra)



c = np.array([[1,2,3,4],
              [5,6,7,8]])
print(c.ravel())


rawInp1 = input()
rawInp2 = input()

try:
    print(len(rawInp1) / len(rawInp2), end=" ")
except:
    print("cannot.", end=" ")
finally:
    print("done")



def myLoop(x, y):
    print('start loop:', x, y)
    while x > y:
        x -= 4
        y += 3
    print('end loop:', x, y)
    return x

x = 15
y = 8
y = myLoop(x, y)
print('after 1st call:', x, y)
myLoop(y, x)
print('after 2nd call:', x, y)


from random import *
def randPass(numOfLetters):
    capitals = "ABCDEFJKLMNOPQRSTUVWXYZ"
    letters = capitals.lower()
    digits = "0123456789"
    symbols = "!#?%&/*_"
    randNum = randint(0, len(capitals)-1)
    password = capitals[randNum]

    for i in range(int(numOfLetters)):
        randNum = randint(0, len(letters)-1)
        password += letters[randNum]

    randNum = randint(0, len(digits) - 1)
    password += digits[randNum]
    randNum = randint(0, len(symbols) - 1)
    password += symbols[randNum]
    print(password)
    return password



ndarray = np.array([[1,3,5,7], [2,4,6,8], [1,4,9,16]])
print(ndarray)
print("------")
print(ndarray[:2, 1:3])


x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)
print(np.subtract(x, y))
print(np.multiply(x, y))

assessments_and_grades = {"midterm1": 95, "midterm2": 85, "final": 90, "quiz": 85, "project": 75}
def final_score (assessments_and_grades):
    score = 0

    for i in assessments_and_grades:
        score += assessments_and_grades[i]

    score = score/len(assessments_and_grades)
    return score

score = final_score(assessments_and_grades)
print(score)


np_arr = np.array([[1,2,3,4],[5,6,7,8]])
s = np_arr.size()
print(s)

x = 7
y = 10
z = x % (y+2)
k = (y+3) % (x+y)
t = x * y % y
print(z, "*", k, "%", t)



a = np.array([1, 7, 5, 4, 8, 0, 9])
s = a.shape
print(s)


a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 2, 7])
a.reshape(3,4)
a.reshape(4,3)
a.reshape(6,2)


x = np.array([1,2,3,7,8,9,4,5,6])
s = np.split(x, [3,7])
print(s)


arr1 = np.linspace(20,80,5)
arr2 = np.arange(20,80,5)
print(arr1)
print(arr2)