from _collections import deque
class Stack:

	def __init__(self):
		self.q1 = deque()
		self.q2 = deque()


	def pop(self):
		if self.q1:
			self.q1.popleft()

	def push(self, x):
		self.q2.append(x)
		while (self.q1):
			self.q2.append(self.q1.popleft())
		self.q1, self.q2 = self.q2, self.q1


	def peek(self):
		if (self.q1):
			return self.q1[0]
		return None

	def size(self):
		return len(self.q1)



if __name__ == '__main__':
    s = Stack()
    i = 0
    while i == 0:
        print(f"1.Push\n2.Pop\n3.Peek\n4.Size\n0.Exit")
        n = int(input())
        if (n == 1):
            x = (input("Enter data: "))
            s.push(x)
            print(f"Pushed {x}")
        elif (n == 2):
            s.pop()
            print(f"Popped")
        elif (n == 3):
            a = s.peek()
            print(f"Element at top: {a}")
        elif (n == 4):
            print(f"Size of Stack: {s.size()}")
        elif (n == 0):
            i = 1
        else:
            print("Wrong Input Please try again")
