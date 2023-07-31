class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height= height
    def get_area(self):
        s=0.0
        s= self.width*self.height
        return s
    def is_square(self):
        if self.width==self.height:
            return True    
        else:
            return False
    def __eq__(self,rect):
        ## 여기부분이 어떻게 해야 할까?
        if self.width*self.height==:
            return True

rect1 =Rectangle(10,20)
rect2 = Rectangle(10, 10)
rect3 = Rectangle(20, 10)
print(rect1.get_area())  # 200
print(rect1.is_square())  # False
print(rect2.get_area())  # 100
print(rect2.is_square())  # True
print(rect1==rect2)  # False
print(rect1==rect3)

class Circle:
    def __init__(self, radius=1):
        self.r = radius
    def get_area(self):
        return 3.14*self.r*self.r
    def get_circumference(self):
        return 2*3.14*self.r
c = Circle(4)
print(Circle.get_area(c))
print(c.get_area())
print(Circle.get_circumference(c))
print(c.get_circumference())

""" type은 현재 가지고 있는 class에만 관심이 있는 것이다.
isinstance(object,class)는 속한 클래스에서의 instance를 나타내고 있는 지를 보여주면 됨
issubclass(sub_class,super_class)

class Student:
b= Student()   ----> b가 instance이다
"""
class Dog():
    def cry(self):
        return "woof"
a= Dog()
a1=Dog.cry(a)

print(a1)
print(Dog.cry())#ERROR
print(Dog.cry(a))
print(Dog().cry())