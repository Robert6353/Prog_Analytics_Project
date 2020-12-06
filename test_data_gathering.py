import unittest
from Data_Gather import ticker, download_data_csv
import pandas as pd
import os

class test(unittest.TestCase):

    def does_file_exist(self):
        data = ticker("AMZN", "2011-01-01", "2012-01-01", "ama10.csv")
        self.assertEqual(len(data), 252)
        self.assertTrue(os.path.isfile("bloop.csv"))
        bloop_file = pd.read_csv("berkshire.csv")
        self.assertEqual(len(bloop_file), len(data))
    
    def does_validation_work(self):
        #self.assertFail(date_choice("AMZN", "2011-01-01", "2020-01-01", "berkshire.csv"))
        download_data_csv("AMZN")
        
#data_gathering_test().does_file_exist()
test.does_validation_work("st")

if __name__ == '__main__':
    unittest.main()