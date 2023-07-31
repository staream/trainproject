def function1(value):
    sum=0
    for i in value:
        sum+=i
    return sum
L = [1, 2, 3, 4, 5]
result = function1(L)  # 1 + 2 + 3 + 4  + 5
print(result)

def course_info(**course):
    for key, value in course.items():
        print(f"{key} is {value}.")

course_info(name="Python")
course_info(name="Python", professor="Park")
course_info(name="Python", professor="Park", students=180)
# dict형태 2가지로 되어있다.
a= {"name":"python"}
a={"nae":"py"}
print(a.keys())
