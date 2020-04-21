import unittest
from picture import Picture
from sampleData import SampleData

class TestPicture(unittest.TestCase):

    sample = SampleData()

    picture = Picture(sample.test_0)

    def test_index_to_point(self):
        self.assertEqual((1,2), self.picture.index_to_point(30))

if __name__ == "__main__":
    unittest.main()