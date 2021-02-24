nlistt=[]
print(nlistt)
nlist1=[]
list1=int(input("enter the elements :"))
for i in range(list1):
	nlist1.append(int(input("enter the values :")))
print("list:",nlist1)

def convert(list): 
    return tuple(nlist1)   
print("converted to tuple", convert(nlist1)) 