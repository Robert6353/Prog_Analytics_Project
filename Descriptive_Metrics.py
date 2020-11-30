import numpy as np

def stat_analysis(csv):
    print("What descriptive statistic do you want from the company")
    print("1. Mean\n2. std\n3. Range(Max-Min)\n4. Coefficient of Variation\n5. \
Max\n6. Min\n7. Lower Quartile range\n8. Upper Quartile range\n9. Median\nPress any other key to exit to main menu")
    descriptive = input("> ")
    while descriptive in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        if descriptive == "1":
            mean_input(csv)
        elif descriptive == "2":
            std_input(csv)
        elif descriptive == "3":
            range_input(csv)
        elif descriptive == "4":
            coefficient_of_variation_input(csv)
        elif descriptive == "5":
            maximum_input(csv)
        elif descriptive == "6":
            minimum_input(csv)
        elif descriptive == "7":
            lower_quartile_input(csv)
        elif descriptive == "8":
            higher_quartile_input(csv)
        elif descriptive == "9":
            median_input(csv)
    else:
        import Main_Module
        Main_Module.menu(Main_Module.user_input())

#*********************************************************************

def mean_input(csv):
    print("Calculate mean of")
    print("1. Opening price\n2. Closing price\n3. High\n4. Low\n5. Adj Close\n6. Volume\nAny other key to exit")
    variable = input("> ")
    mean(csv, variable)

def mean(csv, variable):
    while variable in ["1", "2", "3", "4", "5", "6"]:
        if variable == "1":
            mean_open_output(csv)
        elif variable == "2":
            mean_close_output(csv)
        elif variable == "3":
            mean_high_output(csv)
        elif variable == "4":
            mean_low_output(csv)
        elif variable == "5":
            mean_adj_close_output(csv)
        elif variable == "6":
            mean_volume_output(csv)
    else:
        stat_analysis(csv)

def mean_open_output(csv):
    Open = np.array(csv["Open"])
    print(f"Opening Price Mean: {Open.mean()}")
    mean_input(csv)

def mean_close_output(csv):
    Close = np.array(csv["Close"])
    print(f"Closing price Mean: {Close.mean()}")   
    mean_input(csv)

def mean_high_output(csv):
    High = np.array(csv["High"])
    print(f"Highest price Mean: {High.mean()}")
    mean_input(csv)

def mean_low_output(csv):
    Low = np.array(csv["Low"])
    print(f"Lowest Price Mean: {Low.mean()}")
    mean_input(csv)

def mean_adj_close_output(csv):
    Adj_Close = np.array(csv["Adj Close"])
    print(f"Adjusted Closing Price Mean: {Adj_Close.mean()}")
    mean_input(csv)

def mean_volume_output(csv):
    Volume = np.array(csv["Volume"])
    print(f"Trading Volume Mean: {Volume.mean()}")
    mean_input(csv)

#***************************************************************

def std_input(csv):
    print("Calculate mean of")
    print("1. Opening price\n2. Closing price\n3. High\n4. Low\n5. Adj Close\n6. Volume\nAny other key to exit")
    variable = input("> ")
    std(csv, variable)

def std(csv, variable):
    if variable == "1":
        std_open_output(csv)
    elif variable == "2":
        std_close_output(csv)
    elif variable == "3":
        std_high_output(csv)
    elif variable == "4":
        std_low_output(csv)
    elif variable == "5":
        std_adj_close_output(csv)
    elif variable == "6":
        std_volume_output(csv)
    else:
        stat_analysis(csv)

def std_open_output(csv):
    Open = np.array(csv["Open"])
    print(f"Opening Price Standard Deviation: {Open.std()}")
    std_input(csv)

def std_close_output(csv):
    Close = np.array(csv["Close"])
    print(f"Closing Price Standard Deviation: {Close.std()}")
    std_input(csv)

def std_high_output(csv):
    High = np.array(csv["High"])
    print(f"Highest Price Standard Deviation: {High.std()}")   
    std_input(csv)

def std_low_output(csv):
    Low = np.array(csv["Low"])
    print(f"Lowest Price Standard Deviation: {Low.std()}")  
    std_input(csv)

def std_adj_close_output(csv):
    Adj_Close = np.array(csv["Adj Close"])
    print(f"Adjusted Closing Price Standard Deviation: {Adj_Close.std()}")
    std_input(csv)

def std_volume_output(csv):
    Volume = np.array(csv["Volume"])
    print(f"Trading Volume Standard Deviation: {Volume.std()}")
    std_input(csv)

#**********************************************************************

def range_input(csv):
    print("Calculate Range of")
    print("1. Opening price\n2. Closing price\n3. High\n4. Low\n5. Adj Close\n6. Volume\nAny other key to exit")
    variable = input("> ")
    range_(csv, variable)


def range_(csv, variable):
    if variable == "1":
        range_open_output(csv)
    elif variable == "2":
        range_close_output(csv)
    elif variable == "3":
        range_high_output(csv)
    elif variable == "4":
        range_low_output(csv)
    elif variable == "5":
        range_adj_close_output(csv)
    elif variable == "6":
        range_volume_output(csv)
    else:
        stat_analysis(csv)

def range_open_output(csv):
    Open = np.array(csv["Open"])
    print(f"Opening Price Range: {Open.max()-Open.min()}")
    range_input(csv)

def range_close_output(csv):
    Close = np.array(csv["Close"])
    print(f"Closing Price Range: {Close.max()-Close.min()}")
    range_input(csv)

def range_high_output(csv):
    High = np.array(csv["High"])
    print(f"Highest Price Range: {High.max()-High.min()}")
    range_input(csv)

def range_low_output(csv):
    Low = np.array(csv["Low"])
    print(f"Lowest Price Range: {Low.max()-Low.min()}")
    range_input(csv)
    
def range_adj_close_output(csv):
    Adj_Close = np.array(csv["Adj Close"])
    print(f"Adjusted Closing Price Range: {Adj_Close.max()-Adj_Close.min()}")
    range_input(csv)
    
def range_volume_output(csv):
    Volume = np.array(csv["Volume"])
    print(f"Trading Volume Range: {Volume.max()-Volume.min()}")
    range_input(csv)

#****************************************************************

def coefficient_of_variation_input(csv):
    print("Calculate coefficient of variation of")
    print("1. Opening price\n2. Closing price\n3. High\n4. Low\n5. Adj Close\n6. Volume\nAny other key to exit")
    variable = input("> ")
    coefficient_of_variation(csv, variable)

def coefficient_of_variation(csv, variable):
    if variable == "1":
        coefficient_open_output(csv)
    elif variable == "2":
        coefficient_close_output(csv)
    elif variable == "3":
        coefficient_high_output(csv)
    elif variable == "4":
        coefficient_low_output(csv)
    elif variable == "5":
        coefficient_adj_close_output(csv)
    elif variable == "6":
        coefficient_volume_output(csv)
    else:
        stat_analysis(csv)

def coefficient_open_output(csv):
    Open = np.array(csv["Open"])
    print(f"Opening Price Coefficient of Var: {Open.std()/Open.mean()}")
    coefficient_of_variation_input(csv)

def coefficient_close_output(csv):
    Close = np.array(csv["Close"])
    print(f"Closing Price Coefficient of Var: {Close.std()/Close.mean()}")
    coefficient_of_variation_input(csv)

def coefficient_high_output(csv):
    High = np.array(csv["High"])
    print(f"Highest Price Coefficient of Var: {High.std()/High.mean()}")
    coefficient_of_variation_input(csv)

def coefficient_low_output(csv):
    Low = np.array(csv["Low"])
    print(f"Lowest Price Coefficient of Var: {Low.std()/Low.mean()}")
    coefficient_of_variation_input(csv)

def coefficient_adj_close_output(csv):
    Adj_Close = np.array(csv["Adj Close"])
    print(f"Adjustd Closing Price Coefficient of Var: {Adj_Close.std()/Adj_Close.mean()}")
    coefficient_of_variation_input(csv)

def coefficient_volume_output(csv):
    Volume = np.array(csv["Volume"])
    print(f"Trading Volume Coefficient of Var: {Volume.std()/Volume.mean()}")
    coefficient_of_variation_input(csv)

#*************************************************************************

def maximum_input(csv):
    print("Claculuate the max of")
    print("1. Opening price\n2. Closing price\n3. High\n4. Low\n5. Adj Close\n6. Volume\nAny other key to exit")
    variable = input("> ")
    maximum(csv, variable)


def maximum(csv, variable):
    if variable == "1":
        Open = np.array(csv["Open"])
        print(f"Opening Price Max: {Open.max()}")
    elif variable == "2":
        Close = np.array(csv["Close"])
        print(f"Closing Price Max: {Close.max()}")
    elif variable == "3":
        High = np.array(csv["High"])
        print(f"Highest Price Max: {High.max()}")
    elif variable == "4":
        Low = np.array(csv["Low"])
        print(f"Lowest Price Max: {Low.max()}")
    elif variable == "5":
        Adj_Close = np.array(csv["Adj Close"])
        print(f"Adjustd Closing Price Max: {Adj_Close.max()}")
    elif variable == "6":
        Volume = np.array(csv["Volume"])
        print(f"Trading Volume Max: {Volume.max()}")
    else:
        stat_analysis(csv)

def maximum_open_output(csv):
    Open = np.array(csv["Open"])
    print(f"Opening Price Max: {Open.max()}")
    maximum_input(csv)

def maximum_close_output(csv):
    Close = np.array(csv["Close"])
    print(f"Closing Price Max: {Close.max()}")
    maximum_input(csv)

def maximum_high_output(csv):
    High = np.array(csv["High"])
    print(f"Highest Price Max: {High.max()}")
    maximum_input(csv)

def maximum_low_output(csv):
    Low = np.array(csv["Low"])
    print(f"Lowest Price Max: {Low.max()}")
    maximum_input(csv)

def maximum_adj_close_output(csv):
    Adj_Close = np.array(csv["Adj Close"])
    print(f"Adjustd Closing Price Max: {Adj_Close.max()}")
    maximum_input(csv)

def maximum_volume_output(csv):
    Volume = np.array(csv["Volume"])
    return(f"Trading Volume Max: {Volume.max()}")
    maximum_input(csv)


#*************************************************************************

def minimum_input(csv):
    print("Calculuate minimum of")
    print("1. Opening price\n2. Closing price\n3. High\n4. Low\n5. Adj Close\n6. Volume\nAny other key to exit")
    variable = input("> ")
    minimum(csv, variable)


def minimum(csv, variable):
    if variable == "1":
        minimum_open_output(csv)
    elif variable == "2":
        minimum_close_output(csv)
    elif variable == "3":
        minimum_high_output(csv)
    elif variable == "4":
        minimum_low_output(csv)
    elif variable == "5":
        minimum_adj_close_output(csv)
    elif variable == "6":
        minimum_volume_output(csv)
    else:
        stat_analysis(csv)

def minimum_open_output(csv):
    Open = np.array(csv["Open"])
    print(f"Opening Price Min: {Open.min()}")
    minimum_input(csv)

def minimum_close_output(csv):
    Close = np.array(csv["Close"])
    print(f"Closing Price Min: {Close.min()}")
    minimum_input(csv)

def minimum_high_output(csv):
    High = np.array(csv["High"])
    print(f"Highest Price Min: {High.min()}")
    minimum_input(csv)

def minimum_low_output(csv):
    Low = np.array(csv["Low"])
    print(f"Lowest Price Min: {Low.min()}")
    minimum_input(csv)

def minimum_adj_close_output(csv):
    Adj_Close = np.array(csv["Adj Close"])
    print(f"Adjustd Closing Price Min: {Adj_Close.min()}")
    minimum_input(csv)

def minimum_volume_output(csv):
    Volume = np.array(csv["Volume"])
    print(f"Trading Volume Min: {Volume.min()}")
    minimum_input(csv)


#*************************************************************************

def lower_quartile_input(csv):
    print("Calculuate lower Quartile of")
    print("1. Opening price\n2. Closing price\n3. High\n4. Low\n5. Adj Close\n6. Volume\nAny other key to exit")
    variable = input("> ")
    lower_quartile_range(csv, variable)

def lower_quartile_range(csv, variable):
    if variable == "1":
        lower_quartile_open_output(csv)
    elif variable == "2":
        lower_quartile_close_output(csv)
    elif variable == "3":
        lower_quartile_high_output(csv)
    elif variable == "4":
        lower_quartile_low_output(csv)
    elif variable == "5":
        Adj_Close = np.percentile(csv["Adj Close"], 25, interpolation = "midpoint")
        print(f"Adjustd Closing Price lower quartile range: {Adj_Close}")
    elif variable == "6":
        Volume = np.percentile(csv["Volume"], 25, interpolation = "midpoint")
        print(f"Trading Volume lower quartile range: {Volume}")
    else:
        stat_analysis(csv)

def lower_quartile_open_output(csv):
    Open = np.percentile(csv["Open"], 25, interpolation = "midpoint")
    print(f"Opening Price lower quartile range: {Open}")
    lower_quartile_input(csv)

def lower_quartile_close_output(csv):
    Close = np.percentile(csv["Close"], 25, interpolation = "midpoint")
    print(f"Closing Price lower quartile range: {Close}")
    lower_quartile_input(csv)

def lower_quartile_high_output(csv):
    High = np.percentile(csv["High"], 25, interpolation = "midpoint")
    print(f"Highest Price lower quartile range: {High}")
    lower_quartile_input(csv)

def lower_quartile_low_output(csv):
    Low = np.percentile(csv["Low"], 25, interpolation = "midpoint")
    print(f"Lowest Price lower quartile range: {Low}")
    lower_quartile_input(csv)

def lower_quartile_adj_close_ouptut(csv):
    Adj_Close = np.percentile(csv["Adj Close"], 25, interpolation = "midpoint")
    print(f"Adjustd Closing Price lower quartile range: {Adj_Close}")
    lower_quartile_input(csv)

def lower_quartile_volume_ouptut(csv):
    Adj_Close = np.percentile(csv["Adj Close"], 25, interpolation = "midpoint")
    print(f"Adjustd Closing Price lower quartile range: {Adj_Close}")
    lower_quartile_input(csv)

#*************************************************************************

def higher_quartile_input(csv):
    print("Calculuate higher Quartile of")
    print("1. Opening price\n2. Closing price\n3. High\n4. Low\n5. Adj Close\n6. Volume\nAny other key to exit")
    variable = input("> ")
    Higher_quartile(csv, variable)

def Higher_quartile(csv, variable):
    if variable == "1":
        higher_quartile_open_ouptut(csv)
    elif variable == "2":
        higher_quartile_close_ouptut(csv)
    elif variable == "3":
        higher_quartile_high_ouptut(csv)
    elif variable == "4":
        higher_quartile_low_ouptut(csv)
    elif variable == "5":
        higher_quartile_adj_close_ouptut(csv)
    elif variable == "6":
        higher_quartile_volume_ouptut(csv)
    else:
        stat_analysis(csv)

def higher_quartile_open_ouptut(csv):
    Open = np.percentile(csv["Open"], 75, interpolation = "midpoint")
    print(f"Opening Price higher quartile range: {Open}")
    higher_quartile_input(csv)

def higher_quartile_close_ouptut(csv):
    Close = np.percentile(csv["Close"], 75, interpolation = "midpoint")
    print(f"Closing Price higher quartile range: {Close}")
    higher_quartile_input(csv)

def higher_quartile_high_ouptut(csv):
    High = np.percentile(csv["High"], 75, interpolation = "midpoint")
    print(f"Highest Price higher quartile range: {High}")
    higher_quartile_input(csv)

def higher_quartile_low_ouptut(csv):
    Low = np.percentile(csv["Low"], 75, interpolation = "midpoint")
    print(f"Lowest Price higher quartile range: {Low}")
    higher_quartile_input(csv)

def higher_quartile_adj_close_ouptut(csv):
    Adj_Close = np.percentile(csv["Adj Close"], 75, interpolation = "midpoint")
    print(f"Adjustd Closing Price higher quartile range: {Adj_Close}")
    higher_quartile_input(csv)

def higher_quartile_volume_ouptut(csv):
    Volume = np.percentile(csv["Volume"], 75, interpolation = "midpoint")
    print(f"Trading Volume higher quartile range: {Volume}")
    higher_quartile_input(csv)

#*************************************************************************

def median_input(csv):
    print("Calculuate Median of")
    print("1. Opening price\n2. Closing price\n3. High\n4. Low\n5. Adj Close\n6. Volume\nAny other key to exit")
    variable = input("> ")
    Median(csv, variable)

def Median(csv, variable):
    if variable == "1":
        Open = np.percentile(csv["Open"], 50, interpolation = "midpoint")
        print(f"Opening Price Median: {Open}")
    elif variable == "2":
        Close = np.percentile(csv["Close"], 50, interpolation = "midpoint")
        print(f"Closing Price Median: {Close}")
    elif variable == "3":
        High = np.percentile(csv["High"], 50, interpolation = "midpoint")
        print(f"Highest Price Median: {High}")
    elif variable == "4":
        Low = np.percentile(csv["Low"], 50, interpolation = "midpoint")
        print(f"Lowest Price Median: {Low}")
    elif variable == "5":
        Adj_Close = np.percentile(csv["Adj Close"], 50, interpolation = "midpoint")
        print(f"Adjustd Closing Price Median: {Adj_Close}")
    elif variable == "6":
        Volume = np.percentile(csv["Volume"], 50, interpolation = "midpoint")
        print(f"Trading Volume Median: {Volume}")
    else:
        stat_analysis(csv)

def median_open_ouptut(csv):
    Open = np.percentile(csv["Open"], 50, interpolation = "midpoint")
    print(f"Opening Price Median: {Open}")
    median_input(csv)

def median_close_outut(csv):
    Close = np.percentile(csv["Close"], 50, interpolation = "midpoint")
    print(f"Closing Price Median: {Close}")
    median_input(csv)

def median_high_ouput(csv):
    High = np.percentile(csv["High"], 50, interpolation = "midpoint")
    print(f"Highest Price Median: {High}")
    median_input(csv)

def median_low_ouput(csv):
    Low = np.percentile(csv["Low"], 50, interpolation = "midpoint")
    print(f"Lowest Price Median: {Low}")
    median_input(csv)

def median_adj_close_ouput(csv):
    Adj_Close = np.percentile(csv["Adj Close"], 50, interpolation = "midpoint")
    print(f"Adjustd Closing Price Median: {Adj_Close}")
    median_input(csv)

def median_volume_ouput(csv):
    Volume = np.percentile(csv["Volume"], 50, interpolation = "midpoint")
    print(f"Trading Volume Median: {Volume}")
    median_input(csv)
