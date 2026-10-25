class Queue:
        def __init__(self):
                self.values=[]
        def enqueue(self,x):
                self.values.append(x)
        
        def dequeue(self):
                front=self.values[0]
                self.values=self.values[1:]
                return front
q=Queue()
print("list of Queues")
q.enqueue(1) # add 1 in queue
q.enqueue(2)
q.enqueue(3)
print(q.values) # display list of elements in queue

print("dequeue operations:")

print(q.dequeue())  # delete first element of queue

print(q.values)  # remainig values display

