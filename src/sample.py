from mnist import MNIST

class MnistData:
    """ This class sets up the testing and training data from the MNIST dataset"""

    mndata = None
    training_images = None
    training_labels = None
    test_images = None
    test_labels = None
    
    def __init__(self):

        self.mndata = MNIST('./mnistData')

        self.training_images, self.training_labels = self.mndata.load_training()

        self.test_images, self.test_labels = self.mndata.load_testing()
