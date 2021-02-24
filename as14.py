nlist1=[]
list1=0
list1=int(input("enter the elements :"))
for i in range(list1):
	nlist1.append(int(input("enter the values :")))
print(nlist1)
nlist2=[]
list2=0
list2=int(input("enter the elements :"))
for i in range(list2):
	nlist2.append(int(input("enter the values :")))
print(nlist2)
nlist2.reverse()
for (a,b) in zip(nlist1,nlist2):
     print(a, b)