import sys, math
from sampleData import SampleData

class Picture:

    grid = None
    classification = None

    def __init__(self, grid):
        self.grid = grid

    def index_to_point(self, index : int):
        """
        Takes an array index and converts it into a tuple (x,y) for the 28 x 28 grid
        """
        return (int(index/28), int(index % 28))
    
    def getPoints(self, white_space, otherPicture = None):
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

    def euclidean_distance(self, point1 : tuple, point2: tuple):
        return math.sqrt(math.pow(point2[0] - point1[0], 2) + math.pow(point2[1] - point1[1], 2))

    def getDistance(self, white_space, otherPicture):
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