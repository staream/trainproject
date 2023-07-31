try:
    c = 1 / 0
except NameError:
    print("Use a defined variable.")
except ZeroDivisionError:
    print("zero")    
finally:
    print("Done")

try:
    c = 2 / 0
except NameError:
    print("Use a defined variable.")
else:
    print("No error!")
finally:
    print("Done")
# 위의 부분에서 except zerodivision이 없으니 다음단계로 못넘어간다.

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
        #return "Return Finally!"
a424=divide(1,2)
print(a424)

""" raise as 는 에러의 설명을 들으수 있다."""

