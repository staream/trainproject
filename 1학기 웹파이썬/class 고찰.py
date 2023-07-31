students={}

students["2023123199"] = {
    "name": {"family": "Song", "first": "hyekyo"},
    "department": {"Global"}, "grade": 1, "score": 10.0
}
s= " ".join(students["2023123199"]["name"])
# s에는 name dict에서 그것의 key값만을 할당한다.
s1= " ".join(students["2023123199"]["name"].values())


class Student:
    name = None
    student_no = None
    department = None
    grade = 1
    score = 0.0

student001 = Student()

Student.score = None  
# It was 0.0, but None from now/ 할당하는 것임

student001 = Student()

student001.name = {"family": "Park", "first": "Sangkeun"}
student001.student_no = "2023123001"
student001.department = {"Software"}
student001.grade = 1  # Optional: 1 was already assigned
student001.score = 20.0
""" __init__의 사용으로 이렇게 바뀌는 것임
def __init__(self, name, std_no, dept, grade, score):
student001 = Student({"family": …}, "2023123001", {"Software"}, 1, 20.0)
"""
## class내의 함수를 다루기 위한 할달하는 법
student001 = Student(
    {"family": "Park", "first": "Sangkeun"}, "2023123001", 
    dept={"Software"}, grade=1, score=20.0
) 
fullname = Student.get_fullname(student001)
fullname = student001.get_fullname()  
#매직메소드를 이용해서 나타낸 것
print(student001 == student002)  # False
print(student001.__eq__(student002))  # False
print(Student.__eq__(student001, student002))  # False.
