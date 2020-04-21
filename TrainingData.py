from sample import MnistData
from picture import Picture

class TrainingData:

    mnist_data : MnistData = MnistData()

    training_data : dict = dict()

    def __init__(self, max_length=6):

        zeros : list = []
        ones : list = []
        twos : list = []
        threes : list = []
        fours : list = []
        fives : list = []
        sixes : list = []
        sevens : list = []
        eights : list = []
        nines : list = []

        for x in range(len(self.mnist_data.training_labels)):
            label = self.mnist_data.training_labels[x]

            if label == 0 and len(zeros) < max_length:
                zeros.append(Picture(self.mnist_data.training_images[x]))

            elif label == 1 and len(ones) < max_length:
                ones.append(Picture(self.mnist_data.training_images[x]))

            elif label == 2 and len(twos) < max_length:
                twos.append(Picture(self.mnist_data.training_images[x]))

            elif label == 3 and len(threes) < max_length:
                threes.append(Picture(self.mnist_data.training_images[x]))
                
            elif label == 4 and len(fours) < max_length:
                fours.append(Picture(self.mnist_data.training_images[x]))
                
            elif label == 5 and len(fives) < max_length:
                fives.append(Picture(self.mnist_data.training_images[x]))
                
            elif label == 6 and len(sixes) < max_length:
                sixes.append(Picture(self.mnist_data.training_images[x]))
                
            elif label == 7 and len(sevens) < max_length:
                sevens.append(Picture(self.mnist_data.training_images[x]))
                
            elif label == 8 and len(eights) < max_length:
                eights.append(Picture(self.mnist_data.training_images[x]))
                
            elif label == 9 and len(nines) < max_length:
                nines.append(Picture(self.mnist_data.training_images[x]))
        
        self.training_data[0] = zeros
        self.training_data[1] = ones
        self.training_data[2] = twos
        self.training_data[3] = threes
        self.training_data[4] = fours
        self.training_data[5] = fives
        self.training_data[6] = sixes
        self.training_data[7] = sevens
        self.training_data[8] = eights
        self.training_data[9] = nines


    def displayTrainingData(self, key : int):
        for picture in self.training_data[key]:
            print(self.mnist_data.mndata.display(picture.grid))
    