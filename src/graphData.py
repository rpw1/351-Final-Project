from classify import KNN
from picture import Picture
from sample import MnistData
from random import randint
from time import time

def getErrorAndTime(knn, data, tests = 100):
    """
        This function returns the runtime and accuracy for a classifier trying two different distance formulas.

        Parameters
        ----------
        knn : KNN
            This is the classifier that getErrorAndTime is using to test runtime and accuracy
        
        data : MnistData
            This object contains the testing and training data used to test the inputted knn
        
        tests : int
            This is the amount of testing data the function will test the classifier with

        Returns
        -------
        tuple - > ((time, time), (accuracy, accuracy))
            This tuple contains two tuples containing stats on runtime and accuracy for the classifier.
            The first time and accuracy in the tuples uses the picture.getDistace method to compare images
            The second time and accuracy in the tuples uses the picture.grayscaleDistance method to compare images
        
    """
    count = 0
    start_time = time()
    for x in range(tests):
        index = randint(0, len(data.test_images) - 1)
        guessed_label, wasRight = knn.classify_picture(Picture(data.test_images[index]), data.test_labels[index], True)
        count = count + wasRight
    end_time = time()
    first_accuracy = count / tests
    first_time = end_time - start_time

    count = 0
    start_time = time()
    for x in range(tests):
        index = randint(0, len(data.test_images))
        guessed_label, wasRight = knn.classify_picture(Picture(data.test_images[index]), data.test_labels[index], False)
        count = count + wasRight
        end_time = time()
    second_accuracy = count / tests
    second_time = end_time - start_time
    return (first_time, second_time), (first_accuracy, second_accuracy)

if __name__ == "__main__":
    data = MnistData()
    accuracy_file = open('./TechnicalPaper/accuracyData.txt', 'w')
    time_file = open('./TechnicalPaper/timeData.txt', 'w')

    for i in range(10):
        print(i)
        knn = KNN(k=3, training_count=(i+1)*10)
        for j in range(3):
            knn.k = (j+1)*3
            time_tuple, accuracy = getErrorAndTime(knn, data)
            time_file.write(str(time_tuple[0]) + ',' + str(time_tuple[1]) + ',')
            accuracy_file.write(str(accuracy[0]) + ',' + str(accuracy[1]) + ',')
        accuracy_file.write('\n')
        time_file.write('\n')
    accuracy_file.close()
    time_file.close()
    print("Done")