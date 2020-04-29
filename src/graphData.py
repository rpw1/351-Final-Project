from classify import KNN
from picture import Picture
from sample import MnistData
import random, time

def getErrorAndTime(knn, data, tests = 100):
    count = 0
    start_time = time.time()
    for x in range(tests):
        index = random.randint(0, len(data.test_images) - 1)
        guessed_label, wasRight = knn.classify_picture(Picture(data.test_images[index]), data.test_labels[index], True)
        count = count + wasRight
    end_time = time.time()
    first_accuracy = count / tests
    first_time = end_time - start_time

    count = 0
    start_time = time.time()
    for x in range(tests):
        index = random.randint(0, len(data.test_images))
        guessed_label, wasRight = knn.classify_picture(Picture(data.test_images[index]), data.test_labels[index], False)
        count = count + wasRight
        end_time = time.time()
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