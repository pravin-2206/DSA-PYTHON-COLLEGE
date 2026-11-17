def reverseStack(stack):
    temp = []

    # Pop elements and push into temp stack
    while len(stack) > 0:
        element = stack.pop()
        temp.append(element)

    return temp


stack = []

# Push operations
stack.append(10)
stack.append(20)
stack.append(30)
stack.append(40)

print("Original Stack:", stack)

# Reverse stack
result = reverseStack(stack)

print("Reversed Stack:", result)