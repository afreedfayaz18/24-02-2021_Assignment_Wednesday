from functools import reduce
nlist1 = []
list1=0
list1=int(input("enter the elements :"))
for i in range(list1):
	nlist1.append(int(input("enter the values :")))
print(nlist1)  
result1 = reduce((lambda x, y: x * y), nlist1)
print(result1)
