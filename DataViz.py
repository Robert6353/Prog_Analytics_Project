import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import pandas as pd
from sklearn.linear_model import LinearRegression

#In this module we are given the option attempt to visualise arrays or 
#columns from our data frame, 

#csv = dataframe, array = string, ind = string
def raw_time_series(csv, array, ind):
    #ind = input("Do you want a trend line")
    try:
        if ind == "1":
            Line_plot_trend(csv, array)
        elif ind == "2":
            Line_scatter_trend(csv, array)
        elif ind == "3":
            line_plot(csv, array)      
        elif ind == "4":
            scatter_plot(csv, array)
        elif ind == "5":
            sma(csv, array)
        elif ind == "6":
            wma(csv, array)
        elif ind == "7":
            ema(csv, array)
        elif ind== "8":
            MACD(csv, array)     
    except Exception:
        print("You input the wrong thing")

#Get linear plt with trend line
def Line_plot_trend(csv, array):
    #very difficult to plot date with Lin Regression modules
    Date = np.arange(csv["Date"].count())
    DateLR = Date.reshape(-1, 1)
    ArrayLR = csv[array].values.reshape(-1, 1)
    print(csv["Date"].count())

#Uses regression to find the best least squares trend line there is available
    reg = LinearRegression()
    reg.fit(DateLR, ArrayLR)
    print(f"The slope is {reg.coef_[0][0]} and the intercept is {reg.intercept_[0]}")
    
    predictions = reg.predict(DateLR.reshape(-1, 1))
    
    plt.figure(figsize=(12, 8))
    plt.plot(DateLR, ArrayLR, c = "b")
    plt.plot(DateLR, predictions, linewidth=2, c = "r")
    plt.title("trend line");
    plt.ylabel(array);
    plt.xlabel('Number of Days');
    plt.show()

#csv = pd.read_csv("berkshire.csv")
#Line_plot_trend(csv, "Open")
  
#Also uses linear regression to get the trend line, scatter plot  
def Line_scatter_trend(csv, array):  
    Date = np.arange(csv["Date"].count())
    DateLR = Date.reshape(-1, 1)
    ArrayLR = csv[array].values.reshape(-1, 1)
    print(csv["Date"].count())

    reg = LinearRegression()
    reg.fit(DateLR, ArrayLR)
    print(f"The slope is {reg.coef_[0][0]} and the intercept is {reg.intercept_[0]}")
    
    predictions = reg.predict(DateLR.reshape(-1, 1))
    #print(predictions)
    
    plt.figure(figsize=(12, 8))
    plt.scatter(DateLR, ArrayLR, c = "b")
    plt.plot(DateLR, predictions, linewidth=2, c = "r")
    plt.title("trend line");
    plt.ylabel(array);
    plt.xlabel('Number of Days');
    plt.show()

def line_plot(csv, array):
    Dat = pd.to_datetime(csv["Date"])
    date_index = csv.set_index(Dat)
    #Linear plot time series
    date_index[array].plot(figsize = (12, 8), c = "b")
    plt.title("Robs new plot")
    plt.xlabel("Date", size = 20)
    plt.ylabel(array, size = 20)
    plt.show() 
  
def scatter_plot(csv, array):
    Dat = pd.to_datetime(csv["Date"])
    #Scatter plot time series
    plt.figure(figsize = (12, 8))
    plt.scatter(Dat, csv[array], linewidth = 2, c = "b")
    plt.title("trend line");
    plt.ylabel(array);
    plt.xlabel('Date');
    plt.show()

def sma(csv, array):
    #Allow user to choose n
    n = int(input("What will n of the simple moving average be? "))
    #Sets date column as the index
    csv.index = csv["Date"]
    csv.index = pd.to_datetime(csv.index)
    #Create new column calle SMA1, its a rolling average of whatever n user specifies
    csv['SMA1'] = csv[array].rolling(n, min_periods=1).mean()
    sma_plot(csv, array, n)


def sma_plot(csv, array, n):
    plt.figure(figsize=(12, 8))
    plt.plot(csv.index, csv[array])
    plt.plot(csv.index, csv["SMA1"], linewidth=2, c = "b")
    plt.title("Simple moving average");
    plt.ylabel(array);
    plt.xlabel('Date');
    plt.show()

def wma(csv, array):
    n = int(input("What will n of the simple moving average be? "))
    csv.index = csv["Date"]
    csv.index = pd.to_datetime(csv.index)
    #n+1 so user can specify what n they need
    #Applies weights to all the items
    weights = np.arange(1, n+1)
    #Uses lambda to identify individual items within dataframe in order
    #to perform calculations on them, allows us to create a wma and apply
    #wieghts to different items in our chosen array
    csv["wma"] = csv[array].rolling(n).apply(
    lambda prices: np.dot(prices, weights)/weights.sum(), raw=True)
    print(csv["wma"].head(15), csv[array].head(15))
    csv["sma"] = csv[array].rolling(n).mean()
    wma_plot(csv, array, csv["sma"], csv["wma"], n)

def wma_plot(csv, array, sma, wma, n):
    plt.figure(figsize = (12,8))
    plt.plot(csv[array], label=f"{array}", color = "red")
    plt.plot(sma, label = f"{n} Day SMA", color = "blue")
    plt.plot(wma, label= f"{n} Day WMA", color = "green")
    #plt.plot(sma10, label="10-Day SMA")
    plt.title("Weighted moving average")
    plt.xlabel("Date")
    plt.ylabel(array)
    plt.legend()
    plt.show()

#Exponential moving average
def ema(csv, array):
    n = int(input("What is n going to be? "))
    ema10 = csv[array].ewm(span=n).mean()
    #Creates anew column int our data frame from which we calculuate the 
    #Exponential moving average
    csv['EMA'] = np.round(ema10, decimals=3)
    print(csv[[array, 'EMA']].head(15), csv[[array, 'EMA']].tail(15))
    ema_plot(csv, ema10, array)

def ema_plot(csv, ema10, array):
    plt.figure(figsize = (12,8))
    plt.plot(csv[array], label=array, color = "red")
    plt.plot(ema10, label="EMA", color = "blue")
    plt.title("Exponential moving average")
    plt.xlabel("Date")
    plt.ylabel(array)
    plt.show()
    
def MACD(csv, array):
    #Get Exponential Moving Average for n = 10
    ShortEMA = csv[array].ewm(span=10).mean()#AKA Fast moving average
    #Get other Exponential Moving Average
    LongEMA = csv[array].ewm(span=26, adjust=False).mean() #AKA Slow moving average
    #Calculate MACD
    MACD = ShortEMA - LongEMA
    #Calcualte line
    signal = MACD.ewm(span=9, adjust=False).mean()
    MACD_plot(csv, array, MACD, signal)

def MACD_plot(csv, array, MACD, signal):
    plt.figure(figsize=(12,8))
    plt.plot(csv.index, MACD, label='MACD', color = 'red')
    plt.plot(csv.index, signal, label='Signal Line', color='blue')
    plt.title("Moving Average Convergence Divergence")
    plt.xlabel("Date")
    plt.ylabel(array)
    plt.xticks(rotation=45)
    plt.show()
