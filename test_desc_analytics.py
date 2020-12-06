import unittest
import pandas as pd
import numpy as np
from Desc_Analytics import descriptive_calc, stat_analysis

class DESC_Analytics_test(unittest.TestCase):
    #Need to comment out destrcutor in descriptive_calc to use test_descriptive_2
    #Need to have destructur on for test_descriptives_1
    
    def test_descritptives_1(self):
        stat_analysis("berkshire.csv", "Open", 1)
    
    def test_descriptives_2(self):
        csv = pd.read_csv("berkshire.csv")
        array = "Open"
        descriptive = descriptive_calc(csv, array)
        np_compare = np.array(csv[array])
        low_quartile = np.percentile(csv[array], 25, interpolation = "midpoint")
        high_quartile = np.percentile(csv[array], 75, interpolation = "midpoint")
        med_quartile = np.percentile(csv[array], 50, interpolation = "midpoint")
        self.assertEqual(descriptive.mean(), np_compare.mean())
        self.assertEqual(descriptive.sd(), np_compare.std())
        self.assertEqual(descriptive.range_(), np_compare.max()-np_compare.min())
        self.assertEqual(descriptive.coef(), np_compare.std()/np_compare.mean())
        self.assertEqual(descriptive.Maximum(), np_compare.max())
        self.assertEqual(descriptive.Minimum(), np_compare.min())
        self.assertEqual(descriptive.lower_quartile("Open"), low_quartile)
        self.assertEqual(descriptive.higher_quartile("Open"), high_quartile)
        self.assertEqual(descriptive.lower_quartile("Open"), med_quartile)

if __name__ == '__main__':
    unittest.main()

#-v to see the tests done on specific unit