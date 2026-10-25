class stack:
        def __init__(self):
                self.values=[]
        def push(self,x):
                self.values=[x]+self.values
        def pop(self):
                return self.values.pop(0)
s=stack()
s.push(10)
s.push(20)
print(s.values)
s.push(33)
s.push(40)
print(s.values)
print("remove elements")
print(s.pop())
print(s.values)
s.push(60)
print("add elements")
print(s.values)
print("remove")
print(s.pop())
print(s.values)
