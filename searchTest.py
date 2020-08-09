import unittest
from search import linear_search, binary_search

class TestSearch(unittest.TestCase):

    def test_search(self):
        data = [1, 2, 3, 5, 6, 12, 7, 4, 8]
        sorted_data = sorted(data)

        #test for Linear Search
        self.assertEqual(linear_search(data, 6), 4)
        self.assertEqual(linear_search(data, 10),  -1)

        #test for Binary Search
        self.assertEqual(sorted_data[binary_search(sorted_data,0, len(data)-1, 6)], 6)
        self.assertEqual(binary_search(sorted_data,0, len(data)-1, 10), -1)

    def test_searchChar(self):
        data = ['t', 'a', 'b', 'l', 'e']
        sorted_data= sorted(data)

        #test for Linear Search
        self.assertEqual(linear_search(data, 'a'), 1)
        self.assertEqual(linear_search(data, 'j'), -1)

        #test for binary search
        self.assertEqual(sorted_data[binary_search(sorted_data,0, len(sorted_data)-1, 't')], 't')
        self.assertEqual(binary_search(sorted_data,0, len(sorted_data)-1, 'j'), -1)


if __name__ == "__main__":
    unittest.main()