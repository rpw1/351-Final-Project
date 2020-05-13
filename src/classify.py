from picture import Picture
from trainingData import TrainingData
from queue import ItemQueue

class KNN:
    """
        This class is used to create a KNN classifier for the handwritten images

        Methods
        -------
        
        classify_picture(picture : Picture, label : str, euclidean_distance : bool) -> tuple
            This function takes a Picture and classifies it by comparing the given picture to training images.

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
            This is used for declaring what K the K-NN the classifier will be.
            k = 5 -> 5-NN

        training_count: int
            This is used for how much training data the user would like for each number (0-9).
            training_count = 100 -> 100 training images for 0, 100 training images for 1, ... 100 training images for 9

        white_space : int
            This is used to set a value in which any gray scale value that is equal to or lower is counted as noise in the picture.
            white_space = 200 -> [100, 200, 201, 0] only indices 1, 2 and 4 would count as noise
            This would mean that indices 1, 2 and 4 wouldn't be classified as a point in picture.getPoints
        """
        self.k = k
        self.white_space = white_space
        t = TrainingData(training_count)
        self.training_data = t.training_data

    def classify_picture(self, picture : Picture, label : str, euclidean_distance : bool) -> tuple:
        """
            This function takes a Picture and classifies it by comparing the given picture to training images. 

            Parameters
            ----------
            picture : Picture
                This is an object from the picture.Picture class.
                It represents a 784 array containing grayscale values for the given image.

            label : str
                This represents the label or classification of the picture parameter.

            euclidean_distance : boolean
                This is used for choosing which distance formula to compare the picture parameter.
                euclidean_distance = True -> uses picture.getDistance
                euclidean_distance = False -> uses picture.grayscaleDistance

            Returns
            -------
            (str, boolean)
                The return value is a tuple containing the classification created by the classifier and
                a boolean checking if the classification matched the inputted label parameter.

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


    def getLabel(self, labels : list, actual_label : str) -> str:
        """
        This function gets the most frequent label from the given list of labels.

        Parameters
        ----------
        labels : list
            This is a list of strings that represent possible classifications for the given actual_label
        
        actual_label : str
            This is a string representing the label that the parameter labels is trying to return

        Returns
        -------
        str
            The most frequent label in the parameter labels

        """
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

