from picture import Picture
from sample import MnistData
from sampleData import SampleData

class KNN:
    
    def classifyPicture(self, picture : Picture, label : int, samples : list) :
        """
        Takes in a picture and a list of list of sample pictures
        """
        data = MnistData()
        lowest_distance = None
        classification = None
        for sample in samples:
            new_distance = picture.getDistance(sample.grid)
            if lowest_distance == None:
                lowest_distance = new_distance
                classification = sample.classification
            elif new_distance < lowest_distance:
                lowest_distance = new_distance
                classification = sample.classification
        return classification == label
        

    def classifyDataset(self, list_of_grids, list_of_labels, samples):
        length = len(list_of_grids)
        rate = 0
        count = 1
        for x in range(length):
            print(count)
            rate = rate + self.classifyPicture(Picture(list_of_grids[x]),list_of_labels[x],samples)
            count = count + 1
        print(rate / length)

if __name__ == "__main__":
    nonePicture = Picture(None)
    data = MnistData()
    knn = KNN()
    #knn.classifyPicture(Picture(data.test_images[0]), data.test_labels[0], nonePicture.getSamples())
    knn.classifyDataset(data.test_images, data.test_labels, nonePicture.getSamples())
