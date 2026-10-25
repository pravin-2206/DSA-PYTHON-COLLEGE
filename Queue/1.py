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
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.values)

