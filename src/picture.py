import math

class Picture:
    """
        This class is used to compare two different 28 x 28 pixel images represented as 784 length lists.

        Methods
        -------
        index_to_point(index : int) - > tuple (x, y)
            Takes a 784 length list index and converts it into a tuple (x,y) for a 28 x 28 grid.
        
        getPoints(white_space : int, otherPicture : Picture) -> (list, list)
            This function returns points represented as (x,y) on a 28 by 28 grid.
            It goes through the object's grid and the otherPicture's grid.
            It counts an index as a point if it is greater than the white_space value.
            It creates a point by converting the index to (x, y) on a 28 by 28 grid.
            
        euclidean_distance(point1 : tuple, point2: tuple) -> int
            Takes in two points and returns the euclidean distance between them
        
        getDistance(white_space : int, otherPicture : Picture) -> int
            Finds the distance between two pictures by using the nearest euclidean distance for each point on the picture.

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
            A 784 length array representing a 28 x 28 image with grayscale values.
        """
        self.grid = grid

    def index_to_point(self, index : int) -> tuple:
        """
        Takes a 784 length list index and converts it into a tuple (x,y) for a 28 x 28 grid.

        Parameters
        -----------
        index : int
            This is an integer representing the current index of the class variable grid.

        Returns
        --------
        (int, int)
            The index is converted to a point (x,y) on  28 x 29 grid.

        """
        return (int(index/28), int(index % 28))
    
    def getPoints(self, white_space : int, otherPicture) -> tuple:
        """
            This function returns points represented as (x,y) on a 28 by 28 grid.
            It goes through the object's grid and the otherPicture's grid.
            It counts an index as a point if it is greater than the white_space value.
            It creates a point by converting the index to (x, y) on a 28 by 28 grid.

            Parameters
            ----------
            white_space : int
                This is a natural number used as a maximum value not considered noise in the picture.

            otherPicture : Picture
                A second picture that this function also gets points for.

            Returns
            -------
            (list, list)
                A tuple of lists.
                The first list is the points from the object's grid variable
                The second list is the points from otherPicture
            
        """
        first_points : list = []
        second_points : list = []
        for index in range(len(self.grid)):
            if self.grid[index] > white_space:
                first_points.append(self.index_to_point(index))
            if otherPicture.grid[index] > white_space:
                second_points.append(self.index_to_point(index))
        return first_points, second_points

    def euclidean_distance(self, point1 : tuple, point2: tuple) -> int:
        """Takes in two points and returns the euclidean distance between them"""
        return math.sqrt(math.pow(point2[0] - point1[0], 2) + math.pow(point2[1] - point1[1], 2))

    def getDistance(self, white_space : int, otherPicture) -> int:
        """
        Finds the distance between two pictures by using the nearest euclidean distance for each point on the picture.

        Paraneters
        ----------
        white_space : int
            This is a natural number used as a maximum value not considered noise in the picture.

        otherPicture : Picture
            This is the picture the function finds the distance to.

        Returns
        -------
        int
            The sum of the closest distance for each point in the object's grid compared to otherPicture's points

        """
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
            Gets the sum of the euclidean distance between the same index on two pictues using its grayscale values
            
            This is not our function. Author is Priya Viswanathan.
            http://shyamalapriya.github.io/digit-recognition-using-k-nearest-neighbors/
            https://github.com/anandsekar/datashakers-digitrecognizer/blob/master/python/classify.py

            Parameters
            ----------
            otherPicture : Picture
                This is the picture the function finds the distance to.

            Returns
            -------
            int
                The sum of the euclidean distance comparing grayscale values at each index of both pictures.

        """
        distance = 0
        for x in range(0, len(self.grid)):
            distance = distance + math.pow(self.grid[x] - otherPicture.grid[x], 2)
        number = math.sqrt(distance)
        return number