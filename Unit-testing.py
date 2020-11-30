import unittest
from Descriptive_Metrics import stat_analysis, mean

class Test_funcs(unittest.TestCase):

    def test_desc_metrics(self):
        #stat_analysis("amazon.csv")
        stat_analysis("amamzon.csv")
        mean("amazon.csv", "3")
        csv = "amazon.csv"
        self.assertEqual((csv["Open"].count()) < 23)
        

if __name__ == '__main__':
    unittest.main() 