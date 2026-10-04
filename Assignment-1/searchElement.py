n=int(input("Enter the how many elements add in array:"))
arr=[]
for i in range (1,n+1):
        element=int(input("Enter the Elements:"))
        arr.append(element)
print(arr)
search=int(input("Search given number in array: "))
for j in range (0,len(arr)):
        if(arr[j]==search):
                print(f'Element Are Present:',search)
                break
else:
        print(f'Element Are not Present:',search)
                

        
        
        