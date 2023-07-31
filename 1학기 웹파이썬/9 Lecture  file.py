with open("./test.txt","w") as f:
    with open("./test2.txt","r") as f1:
        content = f1.read()
        f.write(content)
# with는 iden을 충족해야 한다.
#read와 readlines의 차이는
# read는 str 메소드 사용이 가능하다.
# read는 write에 쓸 수 있다.
# readlines는 list형이므로 위의 활동을 못한다.

f2 = open("./test3.txt","w")
f2.write(content)
f2.close()
#write와 writelines의 차이는 단지
#들어가는 값이 str이냐 list이냐의 차이같다.


# EXercise 1
name = open("./name.txt","w")
name.writelines(["kim\n","123\n"])
name.close
name = open("./name.txt","r")
name1= name.readline()[0:-1]# "kim이 나온다."
name2= name.readline()[0:-1]
if "kim"==name1 and "123"==name2:
    print("correct")
else:
    print("re")

str = "12324124"
print(str[:-3])
# 끝의 -3은 포함되지 않는다.
# 끝의 자리 전까지 슬라이싱이 되는 것이다.
