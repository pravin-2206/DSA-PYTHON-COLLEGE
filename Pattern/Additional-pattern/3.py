num = int(input("Enter the number: "))

arr = []
countEven = 0

for i in range(1, num + 1):
    element = int(input("Enter the Element: "))
    arr.append(element)

for i in range(len(arr)):
    if arr[i] % 2 == 0:
        countEven += 1

print(arr)
print(countEven)