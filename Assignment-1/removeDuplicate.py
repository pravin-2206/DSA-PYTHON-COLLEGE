n=int(input("how many element add in array:"))
arr=[]

for array in range(1,n+1):
        elements=int(input("Enter the elements:"))
        arr.append(elements)
print(f'Before Array:',arr)

new=[]
for i in range(0,len(arr)):
        if arr[i] not in new:
                new.append(arr[i])
print(f'After Array',new)
