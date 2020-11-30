import yfinance as yf
import pandas as pd
from subprocess import Popen 

def ticker(data, start, end, csv):
    data_df = yf.download(data, start = start, end = end)
    data_df.to_csv(csv)
    read = pd.read_csv(csv, sep = "\t")
    Popen(csv, shell = True)
    print(read.head(), read.tail())

