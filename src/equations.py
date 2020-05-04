from trainingData import TrainingData
from testingData import TestingData
from classify import KNN
from sample import MnistData
from random import randint

class Equations:
    """
        This class is used to setup and solve math equations

        Methods
        -------

        getArgs(wanted_args : list of strings) -> list of strings
            This function takes a list of labels and grabs testing pictures for the corresponding label.
            Then the function classifies the pictures and returns the list of new labels from the classifications

        setup() -> int
            This function is used to combine the individual classifications into an equation
            Returns 1 if successful else returns 0
        
        solve() -> int
            This function solves the equation setup by the setup() function
        
        solve_equation(wanted_args : list) -> int
            This function called getArgs(wanted_args), setup() and returns the return value for solve()
    """

    training_data : dict = None
    testing_data : dict = None
    knn : KNN = None

    args : list = None
    queue : list = None


    def __init__(self):
        self.knn = KNN(6,150)
        self.training_data = self.knn.training_data
        t = TestingData()
        self.testing_data = t.test_data
    
    def getArgs(self, wanted_args : list) -> list:
        """
            This function takes a list of labels and grabs testing pictures for the corresponding label.
            Then the function classifies the pictures and returns the list of new labels from the classifications
        """
        images = []

        print()
        print("Wanted Arguments: " + str(wanted_args))
        print()

        for arg in wanted_args:
            arg_list = self.testing_data[arg]
            index = randint(0,len(arg_list) - 1)
            images.append(arg_list[index])
        self.args = []
        count = 0
        for image in images:
            guessed_label, wasRight = self.knn.classify_picture(image, wanted_args[count], False)
            count = count + 1
            self.args.append(guessed_label)

        print()
        print("Arguments Received: " + str(self.args))
        print()
    
    def setup(self) -> int:
        """
            This function is used to combine the individual classifications into an equation
            Returns 1 if successful else returns 0
        """
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
            self.queue = [value]
            return 1

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
        """
            This function solves the equation setup by the setup() function
        """
        if self.queue == None:
            print("Error: Queue is Null")
            return None
        if len(self.queue) == 1:
            return self.queue[0]
        print("Start")
        print(self.queue)
        print()
        value = 0.0
        done = False
        index = 0
        while not done:
            max_length = len(self.queue) - 1
            if self.queue[index] == '*':
                value = float(self.queue[index - 1]) * float(self.queue[index + 1])
                print(self.queue[index - 1:index + 2])
                print(value)
                del self.queue[index + 1]
                del self.queue[index]
                del self.queue[index - 1]
                self.queue.insert(index - 1, value)
                print(self.queue)
                print()
                index = 0
                if len(self.queue) == 1:
                    return self.queue[0]
            elif self.queue[index] == '/':

                value = float(self.queue[index - 1]) / float(self.queue[index + 1])
                print(self.queue[index - 1:index + 2])
                print(value)
                del self.queue[index + 1]
                del self.queue[index]
                del self.queue[index - 1]
                self.queue.insert(index - 1, value)
                print(self.queue)
                print()
                index = 0
                if len(self.queue) == 1:
                    return self.queue[0]
            
            if index == max_length:
                done = True
            index = index + 1

        done = False
        index = 0
        while not done:
            if self.queue[index] == '+':
                value = float(self.queue[index - 1]) + float(self.queue[index + 1])
                print(self.queue[index - 1:index + 2])
                print(value)
                del self.queue[index + 1]
                del self.queue[index]
                del self.queue[index - 1]
                self.queue.insert(index - 1, value)
                print(self.queue)
                print()
                index = 0
                if len(self.queue) == 1:
                    return self.queue[0]
            elif self.queue[index] == '-':
                value = float(self.queue[index - 1]) - float(self.queue[index + 1])
                print(self.queue[index - 1:index + 2])
                print(value)
                del self.queue[index + 1]
                del self.queue[index]
                del self.queue[index - 1]
                self.queue.insert(index - 1, value)
                print(self.queue)
                print()
                index = 0
                if len(self.queue) == 1:
                    return self.queue[0]
            
            if len(self.queue) == 0:
                done = True

            index = index + 1

        return value

    def solveEquation(self, wanted_args: list) -> int:
        """
            This function called getArgs(wanted_args), setup() and returns the return value for solve()
        """
        self.getArgs(wanted_args)
        if self.setup():
            return self.solve() 
        else:
            print("Error in setup")
            return None


if __name__ == "__main__":
    e = Equations()
    print(e.solveEquation([str(randint(0,9)), str(randint(0,9)),'+', str(randint(0,9)), str(randint(0,9))]))

            

