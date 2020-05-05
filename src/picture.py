import math

class Picture:
    """
        This class is used to compare two different 28 x 28 pixel images represented as 784 length lists

        Methods
        -------
        index_to_point(index : int) - > tuple (x, y)
            Takes an array index and converts it into a tuple (x,y) for the 28 x 28 grid
        
        getPoints(white_space : int, otherPicture : Picture) -> (list of points for self, list of points for other picture)
            Gets the points in a 28 x 28 grid from the 784 length image array.
            Takes in a whitespace value that classifies a spot on the grid array if the gray scale value is greater
            Either can get the points of one picture or two (default is one)

        euclidean_distance(point1 : tuple, point2: tuple) -> int
            Takes in two points and returns the euclidean distance between them
        
        getDistance(white_space : int, otherPicture : Picture) -> int
            Gets the sums of the distances of the points for the picture compared to the given picture

        grayscaleDistance(otherPicture : Picture) -> int
            Gets the sum of the euclidean distance between the same index on two pictues using its gray scale values
            This is not our function. Author is Priya Viswanathan.
            http://shyamalapriya.github.io/digit-recognition-using-k-nearest-neighbors/
            https://github.com/anandsekar/datashakers-digitrecognizer/blob/master/python/classify.py
    """

    grid = None

    def __init__(self, grid):
        """
        Parameters
        ----------
        grid : list
            A 784 length array representing the 28 x 28 image with gray scale values
        """
        self.grid = grid

    def index_to_point(self, index : int) -> tuple:
        """
        Takes an array index and converts it into a tuple (x,y) for the 28 x 28 grid
        """
        return (int(index/28), int(index % 28))
    
    def getPoints(self, white_space : int, otherPicture = None) -> tuple:
        """
            Gets the points in a 28 x 28 grid from the 784 length image array.
            Takes in a whitespace value that classifies a spot on the grid array if the gray scale value is greater
            Either can get the points of one picture or two (default is one)
        """
        first_points : list = []
        second_points : list = []
        if otherPicture != None:
            for index in range(len(self.grid)):
                if self.grid[index] > white_space:
                    first_points.append(self.index_to_point(index))
                if otherPicture.grid[index] > white_space:
                    second_points.append(self.index_to_point(index))
            return first_points, second_points
        for index in range(len(self.grid)):
            if self.grid[index] > white_space:
                first_points.append(self.index_to_point(index))
        return first_points

    def euclidean_distance(self, point1 : tuple, point2: tuple) -> int:
        """Takes in two points and returns the euclidean distance between them"""
        return math.sqrt(math.pow(point2[0] - point1[0], 2) + math.pow(point2[1] - point1[1], 2))

    def getDistance(self, white_space : int, otherPicture) -> int:
        """Gets the sums of the distances of the points for the picture compared to the given picture"""
        first_points, second_points = self.getPoints(white_space, otherPicture)
        distance = 0
        for self_point in first_points:
            lowest_distance = None
            for other_point in second_points:
                current_distance = self.euclidean_distance(self_point, other_point)
                if lowest_distance == None:
                    lowest_distance = current_distance
                elif current_distance < lowest_distance:
                    lowest_distance = current_distance
            distance = distance + lowest_distance
        return distance


    def grayscaleDistance(self, otherPicture) -> int:
        """
            Gets the sum of the euclidean distance between the same index on two pictues using its gray scale values
            
            This is not our function. Author is Priya Viswanathan.
            http://shyamalapriya.github.io/digit-recognition-using-k-nearest-neighbors/
            https://github.com/anandsekar/datashakers-digitrecognizer/blob/master/python/classify.py

        """
        distance = 0
        for x in range(0, len(self.grid)):
            distance = distance + math.pow(self.grid[x] - otherPicture.grid[x], 2)
        number = math.sqrt(distance)
        return number