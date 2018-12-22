from collections import OrderedDict
d=OrderedDict()
for i in range(int(input())):
    item=input();quantity=1
    d[item]=d.get(item,0)+quantity
print(len(d))
for items,quantity in d.items():
    print(quantity,end=" ")
    