class length:
    def __init__(self,items):
        self.items=items
    def __str__(self):
        return str(self.items)
    def __len__(self):
        return len(self.items)

list=[2,3,4]
obj=length(list)
print((obj))
print(len(obj))