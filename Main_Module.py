import sys
import pandas as pd
from Descriptive_Metrics import stat_analysis
from Data_Gathering import ticker
from DataViz import raw_time_series
#from Graphics import graphics
#from GUI import tkint
#from New_Descriptive_metrics import metric_choice

#def t_and_c():
#    agreement = input('''Press Y if you agree to Robs Terms and conditions
#Press N if do not Agree to Robs Terms and Conditions(will result in exiting application"")
#Press V if you wish to view Robs Terms and Conditions
#> ''')
#    while agreement == "Y" or agreement == "N" or agreement == "V":
#        if agreement == "Y":
#            menu(user_input())
#        elif agreement == "N":
#
#            sys.exit()
#        elif agreement == "V":
#            print("\n")
#            for line in open("terms.txt"):
#                print(line, end = "")
#                print("\n")
#                t_and_c()
#    else:
#       print("\nPlease choose a valid option")
#       t_and_c()

def user_input():
    print("Welcome to Robs fresh new stock analyser")
    print("1. Gather data\n2. Descriptive analysis\n3. DataViz\n4. Help")
    print("Press any other key to exit")
    choice = input("> ")
    menu(choice)

def menu(choice):
    while choice in ["1", "2", "3", "4", "5"]:
        if choice == "1":
            Gather_data()
        elif choice == "2":
            CSV()
        elif choice == "3":
            data_viz_menu()
        elif choice == "4":
            predictive_analytics()
        elif choice == "5":
            Help()
    else:
        sys.exit()
    choice = user_input()

def Gather_data():
    print('''1. Online stock analysis in csv form
2. Online sotck analysis in command line
3. Offline sotck analysis''')
    online_input = input("> ")
    while online_input == "1":
        if online_input == "1":
            download_data_csv()
       # elif online_input == "2":
            #download_data_Yahoo()
    else:
        print("Must choose a valid input\n please press 1 or 2")

def download_data_Yahoo():
    print("nothing for now")

#Need to encode Try and except into here
def download_data_csv():
    data = input("what is the ticker symbol you want")
    start = input("when to start?")
    end = input("When to end?")
    csv = input("what will you name the csv?")
    #option = input("Do you want to open the csv?")
    ticker(data, start, end, csv)
    menu(user_input())

def CSV():
    sample_csv = input("what is the name of csv? ")
    csv = pd.read_csv(sample_csv)
    print(csv.head(), csv.tail())
    print("Is this the file you were looking for? ")
    print("Press N if it is not, Press any other key to continue")
    confirmation = input("> ")
    if confirmation != "N":
        descriptive_analysis(csv)
    else:
        CSV()

def descriptive_analysis(csv):
    desc_visual = input("What do you want to see? ")
    while desc_visual in ["1", "2"]:
        if desc_visual == "1":
            csv.memory_usage()
            stat_analysis(csv)
            menu(user_input())
#        if desc_visual == "2":
#            tkint(csv)
    else:
        descriptive_analysis(csv)

def data_viz_menu():
    csv = pd.read_csv("berkshire.csv")
    array = input("What array do you want? ")
    print('''
1. Line plot with trend line
2. Scatter plot with trend line
3. Line plot without trned line
4. Scatter plot with trend line ''')
    ind = input("> ")
    raw_time_series(csv, array, ind)
    user_input()
    
def predictive_analytics():
    print("This is where Im going to do models and that")
    
def Help():
    print("Welcome to Robs stock analyser 2.0")
    menu(user_input())

def show_descriptives():
    symbol = input("Please input the ticker symbol: ")
    values = [10, 11, 12] #values should be imported from pandas
    print(symbol, values)
    print(values)
    print(sum/values, len/values, max(values))#change to numpy

def main():
    #terms and conidtions
#    t_and_c()
    #diplay menu
    menu(user_input())
    #ask user for choice
    #process choice

#print(ystockquote.get_price_book("GOOGL"))

if __name__ == "__main__":
    main()