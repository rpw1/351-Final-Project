from mnist import MNIST
import random

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


if __name__ == "__main__":
    data = MnistData()
    print(data.test_images[0])
    print(data.mndata.display(data.test_images[0]))