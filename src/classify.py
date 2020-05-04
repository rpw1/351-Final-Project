from picture import Picture
from sample import MnistData
from trainingData import TrainingData
from queue import ItemQueue
import random, math, time

class KNN:
    """
        This class is used to classify pictures

        Methods
        -------
        
        classify_picture(picture : Picture, label : str, euclidean_distance : bool) -> guessed_label, guessed_label == label
            This function takes in a picture and tries to classify it as the given label by comparing it to the training data
            The boolean euclidean_distance is used to decide which distance formula to use.

        getLabel(labels : list) -> str
            This function gets the most frequent label from the given list of labels.
    """

    k : int = None
    white_space : int = None
    training_data : dict = None

    def __init__(self, k = 5, training_count = 100, white_space = 200):
        """
        Parameters
        ----------
        k : int
            This is used for declaring what K-NN the classifier will be

        training_count: int
            This is used for how much training data the user would like for each number (0-9)

        white_space : int
            This is used to set a value in which any gray scale value that is equal to or lower is counted as noise in the picture

        """
        self.k = k
        self.white_space = white_space
        t = TrainingData(training_count)
        self.training_data = t.training_data

    def classify_picture(self, picture : Picture, label : str, euclidean_distance : bool) -> tuple:
        """
            This function takes in a picture and tries to classify it as the given label by comparing it to the training data
            The boolean euclidean_distance is used to decide which distance formula to use.

        """
        distances : ItemQueue = ItemQueue()
        for key in self.training_data:
            for training_picture in self.training_data[key]:
                if euclidean_distance:
                    current_distance = picture.getDistance(self.white_space, training_picture)
                else:
                    current_distance = picture.grayscaleDistance(training_picture)
                distances.insert(current_distance, key)
        k_distances, k_labels = distances.getMultiple(self.k)
        guessed_label = self.getLabel(k_labels, label)
        return guessed_label, guessed_label == str(label)


    def getLabel(self, labels : list, actual_label) -> str:
        """This function gets the most frequent label from the given list of labels."""
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
        print("Actual Label: " + str(actual_label) + ' -> ' + str(labels) + ' ->  Predicted Label: ' + str(classification))
        return classification


if __name__ == "__main__":
    data = MnistData()
    knn = KNN()
    ran_index = random.randint(0, len(data.test_images))
    range_max = 100
    count = 0
    counter = 0
    start_time = time.time()
    for x in range(range_max):
        counter = counter + 1
        print(counter)
        index = random.randint(0, len(data.test_images))
        result_label, wasRight = knn.classify_picture(Picture(data.test_images[index]), data.test_labels[index], False)
        count = count + wasRight
    print(count/range_max)
    end_time = time.time()
    print(end_time - start_time)
