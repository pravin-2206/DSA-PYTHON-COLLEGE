n=int(input("Enter the size of an Array:"))
sum=0
arr=[]
for i in range(1,n+1):
        element=int(input("Enter the values:"))
        sum=sum+i
        arr.append(element)
print(arr)
print(f'Sum of Element {sum}')