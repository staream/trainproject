def cal(a):
    b=4
    def minus(a=2):
        b=5
        print(a,b)
    minus(a)
    print(a,b)
a,b=1,2
cal(a)
print(a,b)

def cal(a):
    global b
    b=4
    def minus(a=2):
        b=5
        print(a,b)
    minus(a)
    print(a,b)
a,b=1,2
cal(a)
print(a,b)

def cal(a):
    global b
    b=4
    def minus(a=2):
        b=5
        print(a,b)
    minus(a)
    print(a,b)
a,b=1,2
cal(a)
print(a,b)

def cal(a):
    b=4
    def minus(a=2):
        global c
        c=1
        b=5
        print(a,b,c)
    minus(a)
    print(a,b,c)
a,b,c=1,2,3
cal(a)
print(a,b)

def cal(a):
    b=4
    c=3
    
    
    def minus(a=2):
        nonlocal c
        c=1
        b=5
        print(a,b,c)
    minus(a)
    print(a,b,c)
a,b,c=1,2,3
cal(a)
print(a,b)


# 재귀함수
def func(n):
    if n>1:
        return n*func(n-1)
    else:
        return 1

factorial = func(3)
print(factorial)