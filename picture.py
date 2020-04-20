import sys, math
from sampleData import SampleData

class Picture:
    #increase threshold for point
    grid = None
    classification = None

    def __init__(self, grid):
        if grid != None:
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
        return int(distance)


    # def getSamples(self) :
    #     picture_samples = list()
    #     s = SampleData()

    #     picture0 = Picture(s.test_0)
    #     picture0.classification = 0
    #     picture_samples.append(picture0)

    #     picture11 = Picture(s.test_1_type1)
    #     picture11.classification = 1
    #     picture_samples.append(picture11)

    #     picture12 = Picture(s.test_1_type2)
    #     picture12.classification = 1
    #     picture_samples.append(picture12)

    #     picture2 = Picture(s.test_2)
    #     picture2.classification = 2
    #     picture_samples.append(picture2)

    #     picture3 = Picture(s.test_3)
    #     picture3.classification = 3
    #     picture_samples.append(picture3)

    #     picture41 = Picture(s.test_4_type1)
    #     picture41.classification = 4
    #     picture_samples.append(picture41)

    #     picture42 = Picture(s.test_4_type2)
    #     picture42.classification = 4
    #     picture_samples.append(picture42)

    #     picture5 = Picture(s.test_5)
    #     picture5.classification = 5
    #     picture_samples.append(picture5)

    #     picture6 = Picture(s.test_6)
    #     picture6.classification = 6
    #     picture_samples.append(picture6)

    #     picture71 = Picture(s.test_7_type1)
    #     picture71.classification = 7
    #     picture_samples.append(picture71)

    #     picture72 = Picture(s.test_7_type2)
    #     picture72.classification = 7
    #     picture_samples.append(picture72)

    #     picture8 = Picture(s.test_8)
    #     picture8.classification = 8
    #     picture_samples.append(picture8)

    #     picture9 = Picture(s.test_9)
    #     picture9.classification = 9
    #     picture_samples.append(picture9)

    #     return picture_samples

    