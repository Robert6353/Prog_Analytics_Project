import numpy as np
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
#could also use style.use("ggplot")
import pandas as pd
from sklearn.linear_model import LinearRegression

#matplotlib.rcParams['axes.labelsize'] = 14
#matplotlib.rcParams['xtick.labelsize'] = 12
#matplotlib.rcParams['ytick.labelsize'] = 12
#matplotlib.rcParams['text.color'] = 'k'

def raw_time_series(csv, array, ind):
    Dat = pd.to_datetime(csv["Date"])
    date_index = csv.set_index(Dat)
    #ind = input("Do you want a trend line")
    if ind == "1":
        Line_plot_trend(csv, array)
    elif ind == "2":
        Line_scatter_trend(csv, array)
    elif ind == "3":
        line_plot(csv, array, date_index)      
    elif ind == "4":
        scatter_plot(csv, array, Dat)
    else:
        print("Please re-do this")

def Line_plot_trend(csv, array):  
    Date = np.arange(csv["Date"].count())
    DateLR = Date.reshape(-1, 1)
    ArrayLR = csv[array].values.reshape(-1, 1)
    print(csv["Date"].count())

    reg = LinearRegression()
    reg.fit(DateLR, ArrayLR)
    print(f"The slope is {reg.coef_[0][0]} and the intercept is {reg.intercept_[0]}")
    
    predictions = reg.predict(DateLR.reshape(-1, 1))
    
    plt.figure(figsize=(20, 8))
    plt.plot(DateLR, ArrayLR, c = "b")
    plt.plot(DateLR, predictions, linewidth=2, c = "r")
    plt.title("trend line");
    plt.ylabel(array);
    plt.xlabel('Number of Days');
    plt.show()
    
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
    
    plt.figure(figsize=(20, 8))
    plt.scatter(DateLR, ArrayLR, c = "b")
    plt.plot(DateLR, predictions, linewidth=2, c = "r")
    plt.title("trend line");
    plt.ylabel(array);
    plt.xlabel('Number of Days');
    plt.show()

def line_plot(csv, array, date_index):
    #Linear plot time series
    date_index[array].plot(figsize = (12, 8), c = "b")
    plt.title("Robs new plot")
    plt.xlabel("Date", size = 20)
    plt.ylabel(array, size = 20)
    plt.show() 
  
def scatter_plot(csv, array, Dat):
    #Scatter plot time series
    plt.figure(figsize = (12, 8))
    plt.scatter(Dat, csv[array], linewidth = 2, c = "b")
    plt.title("trend line");
    plt.ylabel(array);
    plt.xlabel('Number of Days');
    plt.show()

def moving_average_input(csv, array):
    n = int(input("What will n be? "))
    simple_moving_average(csv, array, n)

def single_moving_average(csv):
    csv["SMA_10"].plot(color='green', linewidth=3, figsize=(12,6))

def simple_moving_average(csv, array, n):
    csv['SMA1'] = csv[array].rolling(n, min_periods=1).mean()
    #csv['SMA2'] = csv[array].rolling(n, min_periods=1).mean()
    Date = np.arange(csv["Date"].count())
    plt.figure(figsize=(20, 8))
    plt.plot(Date, csv[array])
    plt.plot(Date, csv["SMA1"], linewidth=2, c = "b")
    #plt.plot(Date, csv["SMA2"], linewidth=2, c = "r")
    plt.title("trend line");
    plt.ylabel("y");
    plt.xlabel('Number of Days');
    plt.show()
   
#csv = pd.read_csv("berkshire.csv")
#raw_time_series(csv, "Open", "1") 
   
#Linear_regression(csv, "Open")

def weighted_moving_average():
    data = pd.read_csv("berkshire.csv", index_col = 'Date')
    data.index = pd.to_datetime(data.index)
    weights = np.arange(1,31)#need to alter so user can specify N
    data["wma10"] = data['Open'].rolling(30).apply(
    lambda prices: np.dot(prices, weights)/weights.sum(), raw=True)
    print(data["wma10"].head(20), data["Open"].head(20))
    data["sma10"] = data['Open'].rolling(30).mean()
    plt.figure(figsize = (12,6))
    plt.plot(data['Open'], label="Open")
    plt.plot(data["sma10"], label = "30 day SMA")
    plt.plot(data["wma10"], label="30-Day WMA")
    #plt.plot(sma10, label="10-Day SMA")
    plt.xlabel("Date")
    plt.ylabel("Open")
    plt.legend()
    plt.show()

#weighted_moving_average()
def MACD():
    plt.style.use('fivethirtyeight')
    data = pd.read_csv("amazon.csv")
    #Calculate the MACD and Signal Line indicators
    #Calculate the Short Term Exponential Moving Average
    ShortEMA = data.Close.ewm(span=12, adjust=False).mean() #AKA Fast moving average
    #Calculate the Long Term Exponential Moving Average
    LongEMA = data.Close.ewm(span=26, adjust=False).mean() #AKA Slow moving average
    #Calculate the Moving Average Convergence/Divergence (MACD)
    MACD = ShortEMA - LongEMA
    #Calcualte the signal line
    signal = MACD.ewm(span=9, adjust=False).mean()
    #Plot the chart
    plt.figure(figsize=(12.2,4.5)) #width = 12.2in, height = 4.5
    plt.plot(data.index, MACD, label='MACD', color = 'red')
    plt.plot(data.index, signal, label='Signal Line', color='blue')
    plt.xticks(rotation=45)
    plt.legend(loc='upper left')
    plt.show()

MACD()