list1=[]
list2=["1","2","4","5","6"]
list_name = list2[0]
list_win = list2[4]
list_gd = list2[0:3]
list_for=[]
list_for=list_gd # 리스트에서 리스트 안에 넣을 떄는 어펜드를 쓰지말자.
list_for.append(list_name)
list_for.append(list_win)
print(list_for)