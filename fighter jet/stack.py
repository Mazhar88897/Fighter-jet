class mystack:
    def __init__(self):
        self.elements = list()
    def push(self,value): 
        self.elements.append(value)
    def pop(self):
        assert not len(self.elements) == 0,"Empty stack!"
        x = self.elements.pop()
        return(x)
    def multy(self,x):
        for i in x:
            self.elements.append(i)
    def clear(self):
        self.elements = list()        

