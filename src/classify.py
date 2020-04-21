from picture import Picture
from sample import MnistData
from trainingData import TrainingData
from queue import ItemQueue
import random, math

class KNN:

    k : int = None
    white_space : int = None
    training_data : dict = None

    def __init__(self, k = 5, white_space = 10):
        self.k = k
        self.white_space = white_space
        t = TrainingData(100)
        self.training_data = t.training_data

    def classify_picture(self, picture : Picture, label : int):
        distances : ItemQueue = ItemQueue()
        for key in self.training_data:
            for training_picture in self.training_data[key]:
                current_distance = picture.oddDistance(training_picture) # picture.getDistance(self.white_space, training_picture)
                distances.insert(current_distance, key)
        k_distances, k_labels = distances.getMultiple(self.k)
        guessed_label = self.getLabel(k_labels)
        # print("Guessed: " + str(guessed_label))
        # print("Actual: " + str(label))
        return guessed_label == label


    def getLabel(self, labels : list):
        max_value = -1
        classification = -1
        counts : dict() = dict()
        for label in labels:
            if label in counts:
                continue
            count = labels.count(label)
            counts[label] = count
            if count > max_value:
                max_value = count
                classification = label
        return classification
        

if __name__ == "__main__":
    data = MnistData()
    knn = KNN()
    ran_index = random.randint(0, len(data.test_images))
    range_max = 100
    count = 0
    counter = 0
    for x in range(range_max):
        counter = counter + 1
        print(counter)
        index = random.randint(0, len(data.test_images))
        count = count + knn.classify_picture(Picture(data.test_images[index]), data.test_labels[index])
    print(count/range_max)