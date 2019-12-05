import unittest


def multiply(a, b):
    return a*b


class MyUnitTest(unittest.TestCase):
    def setUp(self):
        pass

    def test_numbers_5_3(self):
        self.assertEqual(multiply(5, 3), 15)

    def test_strings_A_5(self):
        self.assertEqual(multiply('A', 5), 'AAAAA')


if __name__ == "__main__":
    unittest.main()
