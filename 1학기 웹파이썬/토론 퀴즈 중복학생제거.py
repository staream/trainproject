def function1(a):
    s=""
    for i in a:
        
        if i !=" ":
            s+=i
        else:
            pass
    return s
def function2(a):
    s=0
    L=[]
    for i in range(a+1):
        if i%3==0 or i%5==0:
            s+=i
            L.append(i)
    return s

def function3(a):
    t=[]
    s=""
    z=0
    for i in a:
        if i.isnumeric():
            s+=i
        elif s:    # 내가 전에 else를 넣었는데 이렇게 되니 아무 조건이나 다 들어가는 것이다.
            t.append(int(s))
            s=""
        else:
            pass
    for i in t:
        z+=i
    return z
print(function3("3123wrqfq2fe355wef"))
d= {1:2,"we":5,"rer":1}
f=sorted(d.values())
f1 = d.items() #item에 변수를 두개 할당하는 것은 불가능
#아마도 함수에서 return이 복수일때만 가능한 것 같다.
print(f1)

def function4(a):
    name_list={}
    best_name=[]
    for i in a:
        if i not in name_list:
            name_list[i]=1  #모든 값에는 초기값을 넣어줘야한다.
        elif i in name_list:
            name_list[i]+=1
        else:
            pass
    sell_num = list(name_list.values())#items는 나눌수 있다.
    sell_list = sorted(sell_num)
    for i in name_list.keys():
        if sell_num[-1]== name_list[i]:
            best_name.append(i)
        else:
            pass
    return best_name
print(function4(("book", "pen", "pen", "phone", "laptop", "phone", "phone", "laptop", "laptop", "laptop")))

def function5(a):
    f=0
    for i in a:
        if i.isdigit():
            f+= int(i)
        else:
            pass
    return f


def function6(a:int,b:int):
    digit_list=[]
    all_sum=0
    for i in range(101):
        if i%a==0 or i%b==0:
            if i%(a*b) !=0:
                digit_list.append(i)
            else: 
                pass
        else:
            pass
    for j in digit_list:
        all_sum+=j
    return all_sum

def function7(a):
    for i in range(len(a)):# in 다음에 len만을 넣으면 순서가 없는 숫자만 달랑 나온다. 그래서 순서를 넣을 수 있는 range를 이용했다.
        if a[i]==a[i+1]: #[i]를 넣으면 안 된다 왜냐고 지금 i는 str임 슬라이싱은 int가 들어가야함
            return True
        else:
            pass
    else:                 #반복문의 else도 기억해야할 것이다.
        return False
print(function7("apple"))

def get_unique_students(a:tuple):
    setting_name=set()
    total_num=0
    for i in a:
        s=i.upper()#add라는 메소드를 만든 이유를 생각해보기
        setting_name.add(s) ###setting_name=set(s) 내가 저지른 오류 {s1},{s2}등의 형식으로 만든 거임 
        # #upper 같은 것이 return인지 아닌지에 대해 생각하고 답을 쓰기
    for j in setting_name:
        total_num+=1
    return total_num
print(get_unique_students(("KIM", "kim", "Lee", "Park")))

def is_prime_number(a):
    for i in range(a):
        if a%(i+1)!=0:
            pass
        elif a%(i+1)==0:
            if i ==0:
                pass
            else:
                return False
    return True
print(is_prime_number(15))
def get_bad_students(a,b):
    c=a.difference(b) #a>b여야 한다.
    return c
print(get_bad_students({1234, 2345, 3456, 4567}, {1234, 2345, 3456}))

#슬라이싱으로 할당을 할 때에 목적지에 있는 수 전까지만 바꾼다.

d3={123:124,1353:124354,}
for i,j in d3.items():
    print(i,j)

s4= (123,54,63,14)#"fefddfwef"
s5=(123.5345,314)
Al=s4+s5
print(Al)
print(d3.values())
s={}
for i in d3.keys():
    if i not in s:  #-------------------------------->>>>>>여기에선
        s[i]=1                  #i+=400
    else:
        s[i]+=1
print(s)                  #print(i)
#여기에선 not in을 넣을 때는 key값을 만을 적어야만 한다.!!!!!!!!!!!!!!!!!!!!즉 d[i]는 할 수없다는 말이다.
#1. dict는 언제든지 value와 key를 분리해서 계산할 수 있다.
