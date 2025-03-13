from program_Pazdzior import *
import unittest

class Tests(unittest.TestCase):

    def testEmpty(self):
        self.assertEqual(Add(""), 0)
        self.assertEqual(Add(" "), 0)
        self.assertEqual(Add(","), 0)
        self.assertEqual(Add(",,,"), 0)

    def testOne(self):
        self.assertEqual(Add("1"), 1)
        self.assertEqual(Add(",1"), 1)
        self.assertEqual(Add("1,"), 1)
        self.assertEqual(Add("11"), 11)

    def testTwo(self):
        self.assertEqual(Add("1,2"), 3)
        self.assertEqual(Add("1,2,"), 3)
        self.assertEqual(Add(",1,2"), 3)
        self.assertEqual(Add(",1,11"), 12)
    
    def testMany(self):
        self.assertEqual(Add("1,2,3"), 6)
        self.assertEqual(Add("1,2,3,"), 6)
        self.assertEqual(Add(",1,2,3"), 6)
        self.assertEqual(Add("1,11,1"), 13)
        self.assertEqual(Add("1,1,1,1,1,1,1,1"), 8)

    def testWithNewline(self):
        self.assertEqual(Add("1\n"), 1)
        self.assertEqual(Add("1\n2,3,"), 6)
        self.assertEqual(Add(",1,2,3\n"), 6)
        self.assertEqual(Add("1\n11\n1"), 13)

    

if __name__ == "__main__":
    unittest.main()