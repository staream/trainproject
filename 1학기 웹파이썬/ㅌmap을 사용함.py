L=[1,2,4,5,6]
def func(a):
    return a+1
s = map(func,L)
print(list(s))
#print할 때엔 list로 바꾸어야한다./ map에는 list나 tuple만 넣기 dict는 안된다.

dict1 ={"123":1243,"12456":34,"124556":535}
dict2 ={"1254":"215535","12456":"13556611","154352":"4657674"}
s=0#s=[]
t=""
s1=set()
#print(dict1)  dict1 자체를 복사한다.
for i in dict1:
    print(i)   #dict1의 key를 print
#    print(dict1[i])
    #s+=dict[i]   #dict[i]+=1 둘다 에러가  error임
       #s+=1


# 1.dict에서 값을 가지고 놀려면 values를 이용해야 한다. dict[1]는 정해지지 않은 값이다.
for i in dict1.values(): 
    #s+=i  #s가 0이라는 int면 계속 더한다. 세번째엔 3개의 value가 더해진 값이 나온다.
   # s.append(i) #s.append(dict.values()) in dict였을 때 가능하지 않았다.
    print(i)


for i in dict2.values(): #문장은 넣기 바로 간응
    t+=i

for i in dict1:#dict or dict.keys()가능
    s1.add(i)
print(s1)

for i in dict1:
    print(dict1[i])

# 1.dict에서 값을 가지고 놀려면 values를 이용해야 한다. dict[1]는 정해지지 않은 값이다.
#2. for과 같은 조건문 밑에 codeblock은 절대 혼자 두지 말기
#3. 수를 원할 때는 lens()를 이용한다.
def func123(a):
    s=0
    s+=a
    return s
t123=func123(dict1["123"])#dict의 key를 뽑을 때는 ""을 넣기
print(t123)

def func(a, b):
    a = a + 1
    b = b + 2
    print(a, b, c)  # 2 4 3
    return b - a

a, b, c = 1, 2, 3
d = func(a, b)
print(a, b, c, d)  # 1 2 3 2

s1="'park'"
s4= [i for i in s1 if i!="p"]
print(s4)
# 변수가 간추려진 반복문에서는 3개가 들어가야 한다.

def square(n):
    if type(n) != int:
        return None
    return n*n

print(square, 10)  # 100
