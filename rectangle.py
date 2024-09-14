class Rectangle:
    def __init__(self, leng: int, widt: int):
        self.leng = leng
        self.widt = widt
    
    def __iter__(self):
        yield {'length': self.leng}
        yield {'width': self.widt}


rect = Rectangle(20, 8)

for dimension in rect:
    print(dimension)
