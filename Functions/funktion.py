# Functions

def mysum(x,y):
    print(x+y)
mysum(3,2)
mysum(4,6)
5
10
-----------------

def divby(x,y):
    for n in range(1,101):
        if n%x==0 and n%y==0 :
            print(n)

divby(5,10)
10
20
30
40
50
60
70
80
90
100
--------------------

def mysum1(x,y):
    return x+y
def mysum2(x,y):
    print(x+y)

a = mysum1(2,2)
print(a)
b = mysum2(10,10)
print(b)
4
20
None
-------------------
def mysum(x,y):
    return x+y
g = mysum(y=2,x=3)
print(g)
5
--------------------- 
def mysum(x=0,y=0):
    return x+y
g = mysum(5,5)
print(g)
10
---------------------
mysum = lambda x,y : x+y
print(mysum(5,10))
15
---------------------
# scope
f = 0
print(f)

def do():
    f = 5
    print(f)
do()
print(f)
0
5
0
--------------------
f = 0
print(f)

def do():
    global f
    f = 5
    print(f)
do()
print(f)
0
5
5
---------------------
    


