def function01(a):
    if a:
        for i in a:
            sum_n=0
            if i%2==1:
                sum_n+=i
        return sum_n
    else:
        return 0  


def function02(st):
    if st:    
        if st[1:].upper()==st[:-1:-1].upper():
            return True
    else:
        return False
a=function02('level')
print(a)

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def get_uppercase_name(self):
        return self.name.upper()
    def __len__(self):
        return len(self.name)
p1=Person("naai",12)
Name = p1.__len__()
print(Name)
"mro 보려면 일단 init 함수가 필요하다.===>"
"각 함수 내에 함수의 이름이 메서드로 있어야 한다."
class Account:
    def __init__ (self,balance):
        self.balance=balance
A=Account(1000)
print(A.balance)
class mother(Account):
    def __init__(self,balance):
        super().__init__(balance)
class Father(mother):
    def __init__(self,balance):
        super().__init__(balance)
print(Father.__mro__)
print(type("ㅂㅈ")==str)
