from mnist import MNIST
import math

class MnistData:

    mndata = None
    training_images = None
    training_labels = None
    test_images = None
    test_labels = None
    
    def __init__(self):

        self.mndata = MNIST('./mnistData')

        self.training_images, self.training_labels = self.mndata.load_training()

        self.test_images, self.test_labels = self.mndata.load_testing()


class KNN:

    def euclidean_distance(self, point1 : tuple, point2: tuple):
        return math.sqrt(math.pow(point2[0] - point1[0], 2) + math.pow(point2[1] - point1[1], 2))
