import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from statsmodels.tsa.arima_model import ARIMA
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix

#Choice between 1 a Linear regression model, 2 KNN and 3 ARIMA
def predictive_analytics_menu(csv, array, type_model):
    try:
        if type_model == "1":
            Lin_regression(csv, array)
        elif type_model == "2":
            n = int(input("What will n be? "))
            KNN(csv, n)
        elif type_model == "3":
            Arima(array)
    except:
        print("Incorrect input please try again")

def Lin_regression(csv, array):
    #Turns into numy array and back to datetime so we can see dates in our graph
    csv['Date'] = pd.to_datetime(csv.Date)
    csv.index = csv['Date']
    csv.index = (csv.index - pd.to_datetime('1970-01-01')).days
    y = np.asarray(csv[array])
    x = np.asarray(csv.index.values)
    regression_model = LinearRegression()
    # train the model wit past data while mixing up the data
    regression_model.fit(x.reshape(-1, 1), y.reshape(-1, 1))

    # Prediction based on for past dates
    y_learned = regression_model.predict(x.reshape(-1, 1))
    #Lets us predict fro 365 days, but no reason couldn't be extended
    newindex = np.asarray(pd.RangeIndex(start=x[-1], stop=x[-1] + 365))
    # Predictions for future 
    y_predict = regression_model.predict(newindex.reshape(-1, 1))
    print (f"{array} at 2029 would be around ", y_predict[-1])
    x = pd.to_datetime(csv.index, origin='1970-01-01', unit='D')
    future_x = pd.to_datetime(newindex, origin='1970-01-01', unit='D')
    
    #Gives us the RMSE AND E squared output in out console
    absError = y_predict - y
    SE = np.square(absError) # squared errors
    MSE = np.mean(SE) #
    RMSE = np.sqrt(MSE) # Root Mean Squared Error, RMSE
    Rsquared = 1.0 - (np.var(absError) / np.var(y))  #R squared 
    print('RMSE:', RMSE)
    print('R-squared:', Rsquared)

    #setting figure size
    from matplotlib.pylab import rcParams
    rcParams['figure.figsize'] = 20,10
    #plot the actual data
    plt.figure(figsize=(16,8))
    plt.plot(x,csv[array], label='Close Price History')
    #plot the regression model
    plt.plot(x,y_learned, color='r', label='Mathematical Model')
    #plot the future predictions
    plt.plot(future_x,y_predict, color='g', label='Future predictions')
    plt.suptitle('Stock Market Predictions', fontsize=16)
    fig = plt.gcf()
    fig.canvas.set_window_title('Stock Market Predictions')
    plt.legend()
    plt.show()

def Arima(array):
    #Due to nature of Arima have to give user choice, difficult to perform
    #working calulations on csv from Main_Module as needs an index
    csv = input("What csv will your Arima model use")
    data = pd.read_csv(csv, index_col = "Date", squeeze=True)
    data.drop("Volume", inplace = True, axis = 1)

    # fit model to the data from csv and mix up the data
    model = ARIMA(data.values.reshape(-1, 1), order=(5, 1, 0))
    model_fit = model.fit(disp=0)
    print(model_fit.summary())
    # plot and measure the residual errors
    residuals = pd.DataFrame(model_fit.resid)
    residuals.plot()
    pyplot.show()
    residuals.plot(kind='kde')
    pyplot.show()
    print(residuals.describe())

def KNN(csv, n):
    csv.drop("Date", inplace = True, axis = 1)
    csv["Open"] = csv['Open'].astype(int)
    csv["Close"] = csv['Close'].astype(int)
    csv["Adj Close"] = csv['Adj Close'].astype(int)
    csv["Volume"] = csv['Volume'].astype(int)

    X = csv.iloc[:, :-1].values
    y = csv.iloc[:, 3].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
    scaler = StandardScaler()
    scaler.fit(X_train)

    X_train = scaler.transform(X_train)
    X_test = scaler.transform(X_test)
    classifier = KNeighborsClassifier(n_neighbors=n)
    classifier.fit(X_train, y_train)
    y_pred = classifier.predict(X_test)
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    error = []

# Calculating error for K between 1 and 40
    for i in range(1, 40):
        knn = KNeighborsClassifier(n_neighbors=i)
        knn.fit(X_train, y_train)
        pred_i = knn.predict(X_test)
        error.append(np.mean(pred_i != y_test))
    plt.figure(figsize=(12, 6))
    plt.plot(range(1, 40), error, color='red')
    plt.title('Error Rate K Value')
    plt.xlabel('K Value')
    plt.ylabel('Mean Error')  