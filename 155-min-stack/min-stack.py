class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        if not self.st:
            self.st.append([val,val])

        else:
            mini=self.st[-1][1] 
            self.st.append([val,min(mini,val)])

        

    def pop(self) -> None:
        return self.st.pop()

    def top(self) -> int:
        pp = self.st[-1]
        return pp[0]

    def getMin(self) -> int:
        return self.st[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()