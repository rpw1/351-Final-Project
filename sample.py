from mnist import MNIST
import random
from sampleData import SampleData

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

class Sample:

    grid = None
    name = None

    def __init__(self, name : str):
        self.grid = list()
        self.name = name

if __name__ == '__main__':
    data = MnistData()
    samples = SampleData()
    # print(data.training_images[0])
    # print(samples.test_0)
    # print(data.mndata.display(data.training_images[random.randint(0,6000)]))
    # print(data.mndata.display(samples.test_0))
    # print(data.mndata.display(samples.test_1_type1))
    # print(data.mndata.display(samples.test_1_type2))
    # print(data.mndata.display(samples.test_2))
    # print(data.mndata.display(samples.test_3))
    # print(data.mndata.display(samples.test_4_type1))
    # print(data.mndata.display(samples.test_4_type2))
    # print(data.mndata.display(samples.test_5))
    # print(data.mndata.display(samples.test_6))
    # print(data.mndata.display(samples.test_7_type1))
    # print(data.mndata.display(samples.test_7_type2))
    # print(data.mndata.display(samples.test_8))
    #print(data.mndata.display(samples.test_9))