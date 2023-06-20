# Loop with Lists

l = [[1,2,3],[4,5,6],[7,8,9]]
for x in (l):
    print(x)
[1,2,3]
[4,5,6]
[7,8,9]
------------------------------

l = [[1,2,3],[4,5,6],[7,8,9]]
for x in (l):
    for y in x:
        print(y)
1
2
3
4
5
6
7
8
9
------------------------------
# Break Statement

for x in range(10):
    if x == 4 :
        break
print('HHHHHHHHHH')
0
1
2
3
HHHHHHHHHHH
-------------------------------
# Continue Statement

for x in range(10):
    if x == 4 :
        continue
    print(X)
print('HHHHHHHHHHHH')
0
1
2
3
5
6
7
8
9
HHHHHHHHHHHHHH
--------------------------------
# Pass Statement

for x in range(10):
    pass

print('HHHHHHHH')
HHHHHHHHH
--------------------------------
print('Number\tSquare')
print('--------------')

for x in range(1,11):
    print(x,'\t',x*x)
Number	Square
--------------
1 	 1
2 	 4
3 	 9
4 	 16
5 	 25
6 	 36
7 	 49
8 	 64
9 	 81
10 	 100
--------------------------------
start = int(input('enter start : '))
end = int(input('enter end : '))
print('Number\tSquare')
print('--------------')
for x in range(start,end+1):
    print(x,'\t',x*x)
enter start : 5
enter end : 10
Number	Square
--------------
5 	 25
6 	 36
7 	 49
8 	 64
9 	 81
10       100
-------------------------------
start = int(input('enter start : '))
end = int(input('enter end : '))
for x in range(start):
    print('*'*end)
enter start : 5
enter end : 10
**********
**********
**********
**********
**********
------------------------------
start = int(input('enter start : '))
end = int(input('enter end : '))
for x in range(start):
    for y in range(end):
        print('*',end='')
    print('')
enter start : 5
enter end : 10
**********
**********
**********
**********
**********
-------------------------------

for x in range(1,9):
    print('*'*x)
*
**
***
****
*****
******
*******
********
-------------------------------
