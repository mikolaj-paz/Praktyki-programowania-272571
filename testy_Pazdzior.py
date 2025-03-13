import unittest
from program_Czekiel import *

class TestMethods(unittest.TestCase):
    def test_blank(self):
        self.assertEqual(Add(""), 0)

    def test_colan(self):
        self.assertEqual(Add(","), 0)

    def test_add_single_dig(self):
        self.assertEqual(Add("2,1"), 3)
        self.assertEqual(Add("3,7"), 10)
        self.assertEqual(Add("9,9"), 18)

    def test_add_two_dig(self):
        self.assertEqual(Add("45,21"), 66)
        self.assertEqual(Add("99,11"), 110)
        self.assertEqual(Add("55,55"), 110)

    # def test_to_many_num(self): # blad - za duzo liczb
    #     self.assertEqual(Add("5,3,1"), -1)

    def test_no_num_after(self): # blad - po przecinku brak liczby
        self.assertEqual(Add("2,"), -1)

    def test_no_num_before(self): # blad - przed przecinkiem brak liczby
        self.assertEqual(Add(",2"), -1)

    def test_sum_of_zeros(self):
        self.assertEqual(Add("0,0"), 0)

    def test_zeros_before(self):
        self.assertEqual(Add("00001,002"), 3)
        self.assertEqual(Add("01,30"), 31)

    def test_sum_of_many(self):
        self.assertEqual(Add("1,2,3"), 6)
        self.assertEqual(Add("1,2,3,4"), 10)
        self.assertEqual(Add("1,2,3,5,6"), 17)

    def test_missing_num(self):
        self.assertEqual(Add("1,,,3"), -1)
        self.assertEqual(Add("2,,,3,,,4,,"), -1)

    def test_sum_double_dig(self):
        self.assertEqual(Add("12,12,12"), 36)
        self.assertEqual(Add("30,30,20,20"), 100)

    def test_sum_with_newline(self):
        self.assertEqual(Add("1\n2,6"), 9)
        self.assertEqual(Add("1,\n"), -1)
    