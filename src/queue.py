

class ItemQueue:

    items : list = None
    labels : list = None

    def __init__(self):
        self.items = []
        self.labels = []

    def insert(self, item, label):
        if len(self.items) == 0:
            self.items.append(item)
            self.labels.append(label)
        for x in range(len(self.items)):
            if item < self.items[x]:
                self.items.insert(x, item)
                self.labels.insert(x, label)
                break
            if x == len(self.items) - 1:
                self.items.append(item)
                self.labels.append(label)


    def getItemLabel(self, index : int):
        if index >= len(self.items) or index < 0:
            raise IndexError
        return self.items[index], self.labels[index]

    def getMultiple(self, x):
        if x >= len(self.items) or x < 0:
            raise IndexError
        return self.items[0:x], self.labels[0:x]