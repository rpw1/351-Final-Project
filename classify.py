import math
import heapq

class KNN:

    def euclidean_distance(self, point1 : tuple, point2: tuple):
        return math.sqrt(math.pow(point2[0] - point1[0], 2) + math.pow(point2[1] - point1[1], 2))
    
    def get_top_label(self, top_k_labels):
        label_dict = dict()
        classification = None
        class_value = -1
        for label in top_k_labels:
            if label in label_dict:
                label_dict[label] = label_dict[label] + 1
            else:
                label_dict[label] = 1
        for label in label_dict:
            if classification == None:
                classification = label
                class_value = label_dict[label]
            elif class_value < label_dict[label]:
                classification = label
                class_value = label_dict[label]
        return classification

    def classify_point(self, point, training_points, training_labels):
        points_list = []
        label_dict = dict()
        heapq.heapify(points_list)
        counter = 0
        for p in training_points:
            distance = self.calc_euclidean_distance(point, p)
            label_dict[distance] = training_labels[counter]
            counter = counter + 1
            heapq.heappush(points_list, distance)
        k_labels = []
        for x in range(self.k):
            k_labels.append(label_dict[heapq.heappop(points_list)])
        return self.get_top_label(k_labels)
