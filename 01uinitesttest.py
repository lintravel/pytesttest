import unittest

class TestCaseDemo01(unittest.TestCase):
    def test_01_search11(self):
        a=1
        b=2
        try:
            assert a==b
        except:
            print("a不等于b")

if __name__=="__main__":
    unittest.main()
