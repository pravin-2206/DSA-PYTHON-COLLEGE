n=int(input("Enter  the integer :"))

arr=[]
for i in range (1,n+1):
        ele=int(input("Enter the Elements:"))
        arr.append(ele)
print(f'Array Elements:',arr)

odd=0
even=0
for j in range(0,len(arr)):
        if (arr[j]%2==0):
                even+=1
        else:
                odd+=1
print(f'Odd Elements:',odd)
print(f'Even Elements:',even)
