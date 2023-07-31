#왜 이건 가능하지??;;;;

def func(msg,**k):
    return msg, k,k["name"],k["age"]
print(func("hi", name = "park", age=20))

#밑에 있는 것이 오류임 ;;;;;
#def func(msg, **students):
#    return students[name]
#print(func("hi", name="park", age=20))


a= dict()
a["product"]="salad"
s=a.get("product")
print(s)

s="hamer boom".split(" ")
print(s)