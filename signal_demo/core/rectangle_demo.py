class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        for item in [{'length': self.length}, {'width': self.width}]:
            yield item


    def __repr__(self):
        return f"Rectangle(length={self.length}, width={self.width})"



if __name__ == "__main__":
    rect = Rectangle(10, 5)
    for attr in rect:
        print(attr)
