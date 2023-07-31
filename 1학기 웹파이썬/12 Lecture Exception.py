def divide(a, b):
    try:
        c = a / b
    except NameError:
        print("Use a defined variable.")
        return "Return Use a defined variable."
    else:
        print("No error!")
        return "Return No error!"
    finally:
        print("Finally!")
        return "Return Finally!"
#에러 종류 : 
#keyword: dict의 key가 없을 때
#name : 변수가 정의되지 않을 때
#attribute : 데이터 타입에 맞지 않는 메소드를 사용할 때
#zerodivision : 0으로 나눌 때
#value error : type에 맞지 않는 값을 가짐

# 순서 try/ except/else/finally/
#       return finally/ return else

# raise
# 문제가 뜬다면 raise error_name

class OhmygodError(Exception):
        def __init__(self):
            super().__init__("Oh my god")
# init은 그냥 넣는 것 같다.
def mul(a,b):
    try:
        if b== "Python":
              raise OhmygodError
        return a/b# 이 부분이 없다면 계산 결과가 none으로 나온다.
    except OhmygodError as Oh:
        return Oh
print(mul(1,10))
          