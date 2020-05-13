
class ItemQueue:
    """ 
    A class to store distances in a priority queue and labels in a list with maching indices with the distances.
    
    Methods
    -------
    insert(item : int, label : str)
        This function inserts the distance from least to greatest in order in the items list and 
        places the label in the same index in the labels list.

    getItemLabel(index : int)
        This function takes in a index and returns the matching distance from the items list and
        a label from the labels list.

    getMultiple(x : int)
        This function is used to get the first x distances from the items list and 
        labels from the labels list.
    """

    items : list = None
    labels : list = None

    def __init__(self):
        self.items = []
        self.labels = []

    def insert(self, item : int, label : str):
        """
        This function inserts the distance from least to greatest in order in the items list and 
        places the label in the same index in the labels list.

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
        """
        This function takes in a index and returns the matching distance from the items list and
        a label from the labels list.
        """
        if index >= len(self.items) or index < 0:
            raise IndexError
        return self.items[index], self.labels[index]

    def getMultiple(self, x : int):
        """
        This function is used to get the first x distances from the items list and 
        labels from the labels list.
        """
        if x >= len(self.items) or x < 0:
            raise IndexError
        return self.items[0:x], self.labels[0:x]