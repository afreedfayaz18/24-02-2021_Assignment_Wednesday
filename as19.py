nlist1 = []  
list1=int(input("enter the elements :"))
for i in range(list1):
	nlist1.append(int(input("enter the values :")))
print(nlist1)
for ele in nlist1: 
    if ele % 2 == 0: 
        nlist1.remove(ele)  
print("New list after removing all even numbers: ", nlist1) 