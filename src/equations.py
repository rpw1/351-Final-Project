from testingData import TestingData
from classify import KNN
from random import randint

class Equations:
    """
        This class is used to setup and solve math equations

        Methods
        -------

        getArgs(wanted_args : list of strings) -> list of strings
            This function takes a list of labels, gives each label a corresponding testing image,
            classifies the label based on the testing image, and 
            returns a list of classifications corresponding the the inputted labels.

        setup() -> int
            This function is used to combine the individual classifications into an equation.
            Returns 1 if successful else returns 0
        
        solve() -> int
            This function solves the equation created by the setup() method.
        
        solve_equation(wanted_args : list) -> int
            This function called getArgs(wanted_args), setup() and returns the return value for solve().
    """

    training_data : dict = None
    testing_data : dict = None
    knn : KNN = None

    args : list = None
    queue : list = None


    def __init__(self):
        """
        Attributes
        ----------
        knn : KNN
            This is used to classify the the arguments of the equation.
            It is set for a 6-NN using the picture.grayscaleDistance and having 150 training images for each 1 digit number.

        training_data : dict
            This is the training images created from the KNN object.
            
        testing_data : dict
            This is testing images created from the TestingData object.
            This data is used to represent the arguments passed by the user in getArgs.

        """
        self.knn = KNN(6,150)
        self.training_data = self.knn.training_data
        t = TestingData()
        self.testing_data = t.test_data
    
    def getArgs(self, wanted_args : list) -> list:
        """
            This function takes a list of labels, gives each label a corresponding testing image,
            classifies the label based on the testing image, and 
            returns a list of classifications corresponding the the inputted labels.

            Parameters
            ----------
            wanted_args : list
                This is a list of labels represented as string.
                It represents the equation the user wants to be solved.

            Returns
            -------
            list
                The return value is a list of labels.
                Each label in the list of labels was created by putting wanted_args through the knn classifier.
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
        print("Predicted Arguments: " + str(self.args))
        print()
    
    def setup(self) -> int:
        """
            This function is used to combine the individual classifications into an equation.
            Ex: ['3', '0', '+', '5'] -> ['30', '+', '5']

            Returns
            --------
            int
                This function 1 if successful else returns 0.
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
            This function solves the equation created by the setup() method.

            Returns
            -------
            int
                The value of the solved equation.

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
            This function calls getArgs(wanted_args), setup() and returns the return value for solve().

            Parameters
            ----------
            wanted_args : list
                This is a list of labels represented as string.
                It represents the equation the user wants to be solved.

            Returns
            --------
            The value of the solved the equation or None if an error occurred.


        """
        self.getArgs(wanted_args)
        if self.setup():
            return self.solve() 
        else:
            print("Error in setup")
            return None

