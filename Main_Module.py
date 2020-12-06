import sys
import pandas as pd
from Desc_Analytics import stat_analysis
from DataViz import raw_time_series
from Predictive_analytics import predictive_analytics_menu
from Data_Gather import validate_csv, company_list, validate_date

#Inital function, shows the menu and gives the user a choise of their first
#Course of action
def user_input():
    print("Welcome to Robs fresh new stock analyser")
    print("1. Gather data\n2. Descriptive analysis\n3. DataViz\n4. \
Predictive Analytics \n5. Help, \n6. Terms and conditions")
    print("Press any other key to exit")
    choice = input("> ")
    menu(choice)

#Use array menu to choose the proper array for each class
#Option 1 allows you to download a csv with finacial data on a compnay of your
#choosing between selected dates
#Option 2, 3, and 4 all give you the option to select your own csv, 
#filter data and choose what array you want to use
def menu(choice):
    while choice in ["1", "2", "3", "4", "5", "6"]:
        if choice == "1":
            company_list()
            user_input()
        elif choice == "2":
            stat_analysis(CSV(), array_menu())
            user_input()
        elif choice == "3":
            data_viz_menu(CSV(), array_menu())
        elif choice == "4":
            pred_analytics_menu(CSV(), array_menu())
        elif choice == "5":
            Help()
        elif choice == "6":
            t_and_c()
    else:
        sys.exit()
    choice = user_input()

#Identify the correct CSV and ensure proper user input, validate input
def CSV():
    sample_csv = input("what is the name of csv? ")
    try:
        #See Data_Gatheirng for details on validate_csv
        validate_csv(sample_csv)
    except:
        print("unable to validate csv input")
        user_input()
    try:
        csv = pd.read_csv(sample_csv)
    except Exception:
        print("Unable to open CSV, could not find a csv with that name")
        user_input()
    #User is shown CSV where they are given option to try again
    print(csv.head(), csv.tail())
    print("Is this the file you were looking for? ")
    print("Press N if it is not, Press any other key to continue")
    confirmation = input("> ")
    if confirmation == "N":
        user_input()
    #User is given the option to filter the data in the csv
    print("Press Y if you want to filter the data, press any other key if you dont ")
    filtering = input("> ")
    if filtering == "Y":
        csv = data_filter(csv)
        return csv
    else:
        return csv
 
#Filter the available data and ensure proper user input
def data_filter(csv):
    Date = pd.to_datetime(csv["Date"])
    start_date = input("What will the start date be? please input in the from YYYY-MM-DD")
    try:
        validate_date(start_date)
    except:
        print("Please input a valid date")
        user_input()
    #Need to ensure month is less than 13 and days are less than 31
    if int(start_date[5:7]) > 13 or int(start_date[8:]) > 31:
        print("Please input a valid start date, Please input in the form YYYY-MM-DD")
        user_input()
    #See Data_Gathering for details on validate_date
    end_date = input("What will the end date be? ")
    try:
        validate_date(end_date)
    except:
        print("Pleas input a valid date")
        user_input()
    if int(end_date[5:7]) > 13 or int(end_date[8:]) > 31:
        print("Please input a valid end date, Please input in the form YYYY-MM-DD")
        user_input()
    after_start_date = Date >= start_date
    before_end_date = Date <= end_date
    between = after_start_date & before_end_date
    filtered_csv = csv.loc[between]
    print(filtered_csv.head(), filtered_csv.tail())
    #print(csv.head(), csv.tail())
    return filtered_csv

#Need to overhaul array menu
def array_menu():
    print("1. Open\n2. High\n3. Low\n4. Close\n5. Adj Close\n6. Volume, or press any other key to exit to main menu")
    array_input = input("What array do you want? ")
    while array_input in ["1", "2", "3", "4", "5", "6"]:
        if array_input == "1":
            array = "Open"
        elif array_input == "2":
            array = "High"
        elif array_input == "3":
            array = "Low"
        elif array_input == "4":
            array = "Close"
        elif array_input == "5":
            array = "Adj Close"
        elif array_input == "6":
            array = "Volume"
        return array
    else:
        user_input()

#Links to Data_Viz module, gives range of options for what graphs to use
def data_viz_menu(csv, array):
    print('''What type of plot do you want? 
1. Line plot with trend line
2. Scatter plot with trend line
3. Line plot without trned line
4. Scatter plot with trend line
5. Simple Moving Average
6. Weighted Moving Average
7. Exponential Moving Average
8. Moving Average Convergence Divergence ''')
    ind = input("> ")
    raw_time_series(csv, array, ind)
    user_input()
  
#Links to Predictive_analytics module, gives rane of options for preditive analytics
def pred_analytics_menu(csv, array):
    print("1. Linear Regression")
    print("2. K-Nearest Neighbours")
    print("3. Bonus - Arima Model")
    print("note cant use Volume with arima model")
    type_model = input("> ")
    predictive_analytics_menu(csv, array, type_model)
    user_input()
   
def Help():
    print("Welcome to Robs stock analyser 2.0")
    
#Reads the terms and conditions from beginning to end
def t_and_c():
    agreement = input('''Press Y if you agree to Robs Terms and conditions
Press N if do not Agree to Robs Terms and Conditions(will result in exiting application"")
Press V if you wish to view Robs Terms and Conditions
> ''')
    while agreement == "Y" or agreement == "N" or agreement == "V":
        if agreement == "Y":
            menu(user_input())
        elif agreement == "N":

            sys.exit()
        elif agreement == "V":
            print("\n")
            for line in open("terms.txt"):
                print(line, end = "")
                print("\n")
                t_and_c()
    else:
       print("\nPlease choose a valid option")
       t_and_c()

def main():
    user_input()
    menu()
    #choice 1 = Data_gathering2.user_input()
    #choice 2 = Desc_analytics.stat_analysis()
    #choice 3 = DataViz.raw_time_series()
    #choice 4 = Predictive_analytics()
    #choice 5 = Help()
    #chocie 6 = t_and_c()

if __name__ == "__main__":
    main()