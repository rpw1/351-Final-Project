import classify, unittest

class TestKNN(unittest.TestCase):
    
    def test_euclidean_distance(self):
        knn = classify.KNN()
        point1 : tuple = (3, 1)
        point2 : tuple = (6, 5)
        result = knn.euclidean_distance(point1, point2)
        self.assertEqual(result, 5)

if __name__ == '__main__':
    unittest.main()

