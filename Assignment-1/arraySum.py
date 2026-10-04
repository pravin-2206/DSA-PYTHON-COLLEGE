n=int(input("How many Intergers add in array: "))

sum=0
arr=[]

for i in range(1,n+1):
        elements=int(input("Enter the Elements:"))
        sum =sum+elements
        arr.append(elements)
print(f'Array Elements: ',arr)
print(f'Sum of Array :',sum)
        
