n=int(input("Enter the n integer number:"))

arr=[]

for i in range (1,n+1):
        elements=int(input("Enter the Elements:"))
        
        arr.append(elements)
print(f'Array Elements Are: ',arr)

# temp=arr[0]
# sort=[]
# print(temp)

# for j in range (1,len(arr)-1):
#         for k in range(j+1,len(arr)-1):
#                 if(j>=k):
#                         sort.append(j)
# print(sort)

arr.sort()
print(f'Sorted Array:',arr)

print(f'smallest element in array',arr[0])
print(f'Second Smallest element in array',arr[1])

print(f'Largest element in array:',arr[len(arr)-1])
print(f'Second Largest element in Array:',arr[len(arr)-2])
