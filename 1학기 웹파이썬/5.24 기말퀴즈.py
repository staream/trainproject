def function01(a):
    sum =0
    for i in a:
        if i%2==1:
            sum+=i
        else:
            pass
    return sum

def function02(a):
    a=a.upper()
    L1=[]
    L2=[]
    for i in a[::]:
        L1.append(i)
    for j in a[::-1]:
        L2.append(j)
    return L1 ==L2

def function03(*a):
    sum=0
    for i in a:
        if i%2==0:
            sum+=i
    return sum       
# sum이라는 초기값을 해야하는 이유
def function04(a,b):
    try:
        divi = 0
        divi+=a/b
    except:
        return None
#except의 중요성
class Person():
    name = 'park'
    height=160
    def change_name(self,a):
        self.name =a
        return self.name
    def change_height(self,b):
        self.height = b
        return self.height
class Animal():
    def cry(self):
        return "Cry"
class Dog(Animal):
    def cry(self):
        return "Woof"
class Human():
    age=20
    name="Park"
    def __init__(self, name, age):
        self.name = name
        self.age = age
class Number():
    def __init__(self, a):
        self.number = a
    def __add__(self,other):
        return self.number + other.number
    def __sub__(self,other):
        return   self.number - other.number

class Student():
    def __init__(self,a):
        self.student_number=a
    def __eq__(self,other):
        return self.student_number==other.student_number

class Account():
    def __init__(self,a):
        self.balance=a
    def deposit(self,a):
        self.balance += a
        return self.balance
    def withdraw(self,a):
        self.balance -= a
        return self.balance


# int(i) 라는 것에서 int 다른 함수의 자리라면
#거기에선 int의 효과가 없다.
# DataType은 잘 구별하기
# 문자를 곱하면 갯수가 그만큼 증가하는 것이다.

# and or은 참이 되는 값을 내보낸다.
# True인줄 알았겠지만 True를 대체할 수 있는 다른 것이
#있다면 그것으로 반환한다.
print( (1) and 2)

#f 스트링
num =1234
print(f"my name is{num}")
print("a"in "ave")