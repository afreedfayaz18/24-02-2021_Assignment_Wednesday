lower = int(input("Enter lower range limit:"))
upper =int(input("Enter upper range limit:"))
if upper>150:
    upper=150
for i in range(lower, upper+1):
   if(i%5==0):
      print(i)