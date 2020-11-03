# -*- coding: utf-8 -*-
"""
Created on Tue Nov  3 08:29:35 2020

@author: rober
"""
#import numpy as np
#import matplotlib as plt
#import pandas as pd
#import scipy as sp
#import datetime
#import math
import sys


def menu():
    print("Press 1 for Gathering data")
    print("Press 2 for Stock analysis")
    print("Press 3 for Help")
    print("Press ank key to exit")
    user_input = input("> ")
    if user_input == "1":
        gather_data()
    if user_input == "2":
        stock_analysis()
    if user_input == "3":
        Help
    else:
        sys.exit()

def gather_data():
    pass

def stock_analysis():
    pass

def Help():
    print("Welcome to Robs stock analyser 2.0")

def main():
    #diplay menu
    menu()
    #ask user for choice
    #process choice

if __name__ == "__main__":
    main()