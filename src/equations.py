from trainingData import TrainingData
from testingData import TestingData
from classify import KNN
from sample import MnistData
from random import randint

class Equations:

    training_data : dict = None
    testing_data : dict = None
    knn : KNN = None
    mnist_data = MnistData()

    args : list = None
    queue : list = None


    def __init__(self):
        self.knn = KNN(6,150)
        self.training_data = self.knn.training_data
        t = TestingData()
        self.testing_data = t.test_data
    
    def getArgs(self, wanted_args):
        images = []
        for arg in wanted_args:
            arg_list = self.testing_data[arg]
            index = randint(0,len(arg_list) - 1)
            print(self.mnist_data.mndata.display(arg_list[index].grid))
            images.append(arg_list[index])
        self.args = []
        for image in images:
            guessed_label, wasRight = self.knn.classify_picture(image, "-1", False)
            self.args.append(guessed_label)
        print()
        print(wanted_args)
        print(self.args)
    
    def setup(self):
        if self.args == None:
            print("There are no arguments")
            return 0
        if len(self.args) == 1:
            value = None
            try:
                value = int(self.args[0])
            except TypeError:
                print("Error: only argument was a function")
                return 0
            return(value)

        self.queue : list = []
        
        for index in range(len(self.args)):
            value = None

            try:
                value = int(self.args[index])
            except:
                self.queue.append(self.args[index])
                continue
            if len(self.queue) == 0 or len(self.queue) % 2 == 0:
                self.queue.append(str(value))
            else:
                x = len(self.queue) - 1
                self.queue[x] = self.queue[x] + str(value)
        return 1

    def solve(self):
        if self.queue == None:
            print("Error: Queue is Null")
            return None
        print(self.queue)
        value = 0.0
        done = False
        index = 0
        while not done:
            max_length = len(self.queue) - 1
            if self.queue[index] == '*':
                value = float(self.queue[index - 1]) * float(self.queue[index + 1])
                del self.queue[index]
                del self.queue[index - 1]
                del self.queue[index - 1]
                index = 0
                if len(self.queue) == 0:
                    return value
            elif self.queue[index] == '/':
                value = value + float(self.queue[index - 1]) / float(self.queue[index + 1])
                del self.queue[index]
                del self.queue[index - 1]
                del self.queue[index - 1]
                index = 0
                if len(self.queue) == 0:
                    return value
            
            if index == max_length:
                done = True
            index = index + 1

        done = False
        index = 0
        while not done:
            if self.queue[index] == '+':
                value = float(self.queue[index - 1]) + float(self.queue[index + 1])
                del self.queue[index]
                del self.queue[index - 1]
                del self.queue[index - 1]
                index = 0
                if len(self.queue) == 0:
                    return value
            elif self.queue[index] == '-':
                value = value + float(self.queue[index - 1]) - float(self.queue[index + 1])
                del self.queue[index]
                del self.queue[index - 1]
                del self.queue[index - 1]
                index = 0
                if len(self.queue) == 0:
                    return value
            
            if len(self.queue) == 0:
                done = True

            index = index + 1

        return value

    def solveEquation(self, wanted_args: list):
        self.getArgs(wanted_args)
        if self.setup():
            return self.solve() 
        else:
            print("Error in setup")
            return None


if __name__ == "__main__":
    e = Equations()
    print(e.solveEquation([str(randint(0,9)), str(randint(0,9)),'+', str(randint(0,9)), str(randint(0,9))]))

            

