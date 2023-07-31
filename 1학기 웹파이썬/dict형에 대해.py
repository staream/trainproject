def get_best_seller(a):
    selling_num={}
    for product in a:
        if product not in selling_num.keys():#keys
            #넣어야 할 곳이 selling이므로
            selling_num[product]=1
        else:
            selling_num[product] +=1
    sell_num = sorted(selling_num.values())
    most_num = sell_num[-1]
    best_seller=""
    for keys,num in selling_num.items(): #method
        if num == most_num:
            best_seller+=keys
            break
        else:
            pass
    return best_seller

b1 = get_best_seller(("book", "pen", "pen", "phone", "laptop", "phone", "phone", "laptop", "laptop", "laptop"))
print(b1)

