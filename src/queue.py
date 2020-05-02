
class ItemQueue:
    """ A class to store distances in a priority queue and labels in a list with maching indices with the distances
    
    Methods
    -------
    insert(item : int, label, str)
        Takes a item represented by distance and a label represented by a string
        This function inserts the distance in order of the queue and places the label in the same index in a differnet list

    getItemLabel(index : int)
        This function takes in a queue index and returns the matching distance and label

    getMultiple(x : int)
        This function is used to get the first x items and labels from the queue
    """

    items : list = None
    labels : list = None

    def __init__(self):
        self.items = []
        self.labels = []

    def insert(self, item : int, label : int):
        """
        Takes a item represented by distance and a label represented by a string
        This function inserts the distance in order of the queue and places the label in the same index in a differnet list
        """

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
        """This function takes in a queue index and returns the matching distance and label"""
        if index >= len(self.items) or index < 0:
            raise IndexError
        return self.items[index], self.labels[index]

    def getMultiple(self, x : int):
        """This function is used to get the first x items and labels from the queue"""
        if x >= len(self.items) or x < 0:
            raise IndexError
        return self.items[0:x], self.labels[0:x]