# For each of the following code snippets, first predict the output (what you will see printed to the terminal). Once you've made a prediction, run the code snippet to see if you are correct!


#1
def a():
    return 5
print(a()) 
# output: 5

#2
def a():
    return 5
print(a()+a())
# output: 10

#3
def a():
    return 5
    return 10
print(a())
# output: 5

#4
def a():
    return 5
    print(10)
print(a())
# output: 5

#5
def a():
    print('inside fucn', 5)
x = a()
print('outside func after', x)
print(x)
# output -> 5, None

#6
def a(b,c):
    print(b+c)
# print(a(1,2) + a(2,3))
# 3, 5
# nothing was RETURNED!!!! None + None!!!

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
print(type(a(2,5))) # string
# "2"+"5" -> "25"

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
      return 10
    return 7
print(a())
# 100
# 10

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
# 7
# 14
# 21

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
# 500
# 500
# 300
# 500

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
# 500
# 500
# 300
# 500

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
# 500
# 500
# 300
# 300

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
# 1
# 3
# 2

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
# 1
# 3
# x = 5
# 5
# y =10
# 10