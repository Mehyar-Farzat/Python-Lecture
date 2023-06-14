Type of Variables
x = 9          # integer
y = 'Adam'     # string
z = 3.2        # float
s = True,False # Boolean
d = [2 , 'john'] # list
a = (8 , 5 , 2 ) # tuple
u = {name : 'Ahmed' , age : '20'} # dictionary
-----------------------------------------------
Creatign Variables
x = 3
y = "Adam"
print(x)
print(y)
3
Adam
-----------------------------------------------
we can specify the data type of a variable
x = str(6)   # x will be '6'
y = int(4)   # y will be  4
z = float(2) # z will be 2.0
-----------------------------------------------
we can get data type of a variable with the type() function
a = 1
s = 'Adam'
print(type(a))
print(type(s))
<class 'int'>
<class 'str'>
-----------------------------------------------
Variable names are case-sensitive
f = 3
F = "Ahmed"
print(f)
print(F)
# F will not overwrite f
3
Ahmed
-----------------------------------------------
with python we can assign values to multiple variables in one line
x, y, z = 'Red', 'Blue', 'Black'
print(x)
print(y)
print(z)
Red
Blue
Black
----------------------------------------------
we can assign the same value to multiple variables in one line
x = x = z = 'Banana'
print(x)
print(y)
print(z)
Banana
Banana
Banana
----------------------------------------------
we can create a tuple with one value by adding (,) after the value
x = (3 ,)
print(type(x))
<class 'tuple'>
y = ('ahmed' ,)
print(type(y))
<class 'tuple'>
----------------------------------------------




