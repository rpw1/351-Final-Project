import sys, math
from sampleData import SampleData
from sample import MnistData

class Picture:

    grid = None
    classification = None
    points = None

    def __init__(self, grid):
        if grid != None:
            self.grid = grid
            self.points = self.getPoints(grid)
        
    def euclidean_distance(self, point1 : tuple, point2: tuple):
        return math.sqrt(math.pow(point2[0] - point1[0], 2) + math.pow(point2[1] - point1[1], 2))

    def index_to_point(self, index : int):
        """
        Takes an array index and converts it into a tuple (x,y) for the 28 x 28 grid
        """
        return (index/28, index * 28)

    
    def getDistance(self, otherGrid : list):
        distance = 0
        other_points = self.getPoints(otherGrid)
        for picture_point in self.points:
            closest_distance = sys.maxsize
            closest_point = None
            picture_coordinates = self.index_to_point(picture_point)
            for other_point in other_points:
                new_distance = self.euclidean_distance(picture_coordinates, self.index_to_point(other_point))
                if new_distance < closest_distance:
                    closest_distance = new_distance
                    closest_point = other_point
            distance = distance + closest_distance
            if closest_point in other_points:
                other_points.remove(closest_point)
        return distance
                

    def getPoints(self, grid : list):
        """
        This function gets the non whitespace points in the grid
        """
        points_list = list()
        for x in range(len(grid)):
            if grid[x] != 0:
                points_list.append(x)
        return points_list

    def getSamples(self) :
        picture_samples = list()
        s = SampleData()

        picture0 = Picture(s.test_0)
        picture0.classification = 0
        picture_samples.append(picture0)

        picture11 = Picture(s.test_1_type1)
        picture11.classification = 1
        picture_samples.append(picture11)

        picture12 = Picture(s.test_1_type2)
        picture12.classification = 1
        picture_samples.append(picture12)

        picture2 = Picture(s.test_2)
        picture2.classification = 2
        picture_samples.append(picture2)

        picture3 = Picture(s.test_3)
        picture3.classification = 3
        picture_samples.append(picture3)

        picture41 = Picture(s.test_4_type1)
        picture41.classification = 4
        picture_samples.append(picture41)

        picture42 = Picture(s.test_4_type2)
        picture42.classification = 4
        picture_samples.append(picture42)

        picture5 = Picture(s.test_5)
        picture5.classification = 5
        picture_samples.append(picture5)

        picture6 = Picture(s.test_6)
        picture6.classification = 6
        picture_samples.append(picture6)

        picture71 = Picture(s.test_7_type1)
        picture71.classification = 7
        picture_samples.append(picture71)

        picture72 = Picture(s.test_7_type2)
        picture72.classification = 7
        picture_samples.append(picture72)

        picture8 = Picture(s.test_8)
        picture8.classification = 8
        picture_samples.append(picture8)

        picture9 = Picture(s.test_9)
        picture9.classification = 9
        picture_samples.append(picture9)

        return picture_samples
        

if __name__ == "__main__":
    data = MnistData()
    samples = SampleData()
    picture1 = Picture(data.training_images[0])
    # print(data.mndata.display(data.training_images[0]))
    # picture2 = Picture(samples.test_5)
    # print(data.mndata.display(samples.test_5))
    # picture3 = Picture(samples.test_0)
    # print(data.mndata.display(samples.test_0))
    # print(picture2.getDistance(picture1.grid))
    # print(picture2.getDistance(picture3.grid))
    