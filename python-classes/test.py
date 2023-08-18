class area:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def prod(self):
        return self.length * self.width

squareArea = area(5, 7)
print(squareArea.prod())