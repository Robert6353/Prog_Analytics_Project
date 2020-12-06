import pandas as pd
from datetime import datetime
import yfinance as yf
from subprocess import Popen
import os
#In this module we are trying to help the user search for the company of their choice
#Our goal is to get a csv of al the stock price details and detials about 
#the volume in on handy csv


#This is used in order to import file of all company stocks
def company_list():
    company_list = pd.read_csv('companylist.csv')
    print(company_list)
    symbol_data(company_list)


def symbol_data(company_list):
    try:
        symbol = input("\nPlease search for the company you want via the ticker \
symbol or company name\n> ")
#Allows user to search for stocks by either name of ticker symbol
#Allows user to filter stuff
        filtered_companies = company_list[
            (company_list.Symbol.str.lower().str.contains(symbol.lower()))
            | (company_list.Name.str.lower().str.contains(symbol.lower()))]    
        if len(filtered_companies) == 1:
            data = filtered_companies["Symbol"]
            data = data.iloc[0]
            print(filtered_companies)
            print("\nThis is the ticker symbol you have chosen? {}\n".format(data))
            download_data_csv(data)
        else:
            #print(filtered_companies)
            print("\nPlease be more specific about what company you are searching for\n")
            if len(filtered_companies) != 0:
                print(filtered_companies)
            symbol_data(company_list)
    except:
        print("\n\nPlease input only valid characters into console\n\n")

#Also used in data_filter and CSV() in Main_Module, turns date into prope format and simultaneously
#helps ensure user did not put something incorrect int
def validate_date(d):
    try:
        if len(d) == 10:
            datetime.strptime(d, '%Y-%m-%d')
            return True
        else: print("\nPlease input a valid start and end date in YYYY-MM-DD format\n"), validate_date()
    except ValueError:
        print("\nPlease input a valid start and end date in YYYY-MM-DD format\n"), validate_date()

def validate_csv(c):
    try:
        if c[-4:] == ".csv":
            return True
        else: print("\nPlease input file in a csv format, must end in.csv\n")
    except ValueError:
        print("\nPlease input file in a csv format, must end in .csv\n")
    
def download_data_csv(data):
    start = input("What will your start date wil be? Please input in the form YYYY-MM-DD? \n")
    if int(start[:4]) < 1970 or int(start[5:7]) > 12 or int(start[8:]) > 31:
        print("\nPlease input a valid start and end date in the form YYYY-MM-DD\n")
        download_data_csv(data)
    end = input("\nWhat will your end date be? Please input in the form YYYY-MM-DD? \n")
    if start > end or datetime.strptime(end, "%Y-%m-%d") > datetime.now() or int(end[5:7]) > 12 or int(end[8:]) > 31:
        print("\nPlease input a valid end date, Please input in the form YYYY-MM-DD format? \n")
        download_data_csv(data)
    csv = input("\nwhat will you name the csv? \n")
    date_choice(data, start, end, csv)

#Validates the details
def date_choice(data, start, end, csv):
    validate_date(start)
    validate_date(end)
    validate_csv(csv)
    check_file(data, start, end, csv)  

#If the user specified a file name that is already used by another
#file within their directory will reject this and return to menu
def check_file(data, start, end, csv):
    if os.path.isfile(csv):
        print("\nthat is already a file called that name, please retry\n")
    else:
        ticker(data, start, end, csv)

def ticker(data, start, end, csv):
    data_df = yf.download(data, start = start, end = end)
    data_df.to_csv(csv)
    read = pd.read_csv(csv, sep = "\t")
#Opens up and Allows user to see the full csv in an excel file
    Popen(csv, shell = True)
    return(read)
    