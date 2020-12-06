import numpy as np

#In this module we are trying to get descriptive analytics on arrays within
#our csv, 

#Menu to help identify what descriptive they want for the array
def stat_analysis(csv, array):
    print("What descriptive statistic do you want from the company")
    print("1. Mean\n2. std\n3. Range(Max-Min)\n4. Coefficient of Variation\n5. \
Max\n6. Min\n7. Lower Quartile range\n8. Upper Quartile range\n9. Median\nPress any other key to exit to main menu")
    descriptive = input("> ")
    try:
        if descriptive == "1":
            desc_calc(csv, array).mean()
        elif descriptive == "2":
            desc_calc(csv, array).sd()
        elif descriptive == "3":
           desc_calc(csv, array).range_()
        elif descriptive == "4":
            desc_calc(csv, array).coef()  
        elif descriptive == "5":
            desc_calc(csv, array).Maximum()
        elif descriptive == "6":
            desc_calc(csv, array).Minimum()
        elif descriptive == "7":
            desc_calc(csv, array).lower_quartile(array)
        elif descriptive == "8":
            desc_calc(csv, array).higher_quartile(array)
        elif descriptive == "9":
            desc_calc(csv, array).median(array)            
    except:
        return("Goodbye")

#
class desc_calc:
#Makes use of inheritance 
    def __init__(self, csv, col):
        self.csv = csv
        Array_name = col
        self.array_name = Array_name
        Array = np.array(self.csv[col])
        self.array = Array
#Need to comment this out depending on what kind of unit test you are doing 
#Descturcotr class activates after the method is called     
    def __del__(self):
       stat_analysis(self.csv, self.array_name)

#Makes use of inheritance and other OOP concepts to create very short methods
    def mean(self):
        print(f"{self.array_name} Mean: {self.array.mean()}")
        return(self.array.mean())

    def sd(self):
        print(f"{self.array_name} Standard Deviation: {self.array.std()}")
        return(self.array.std())
    
    def range_(self):
        print(f"{self.array_name} Range: {self.array.max()-self.array.min()}")
        return(self.array.max()-self.array.min())
        
    def coef(self):
        print(f"{self.array_name} Coefficient of Var: {self.array.std()/self.array.mean()}")
        return(self.array.std()/self.array.mean())
    
    def Maximum(self):
        print(f"{self.array_name} Max: {self.array.max()}")
        return(self.array.max())
    
    def Minimum(self):
        print(f"{self.array_name} Min: {self.array.min()}")
        return(self.array.min())
    
    def lower_quartile(self, array):
        Array = np.percentile(self.csv[array], 25, interpolation = "midpoint")
        self.array = Array
        print(f"{self.array_name} lower quartile range: {self.array}")
        return(self.array)
    
    def higher_quartile(self, array):
        Array = np.percentile(self.csv[array], 75, interpolation = "midpoint")
        self.array = Array
        print(f"{self.array_name} higher quartile range: {self.array}")
        return(self.array)
    
    def median(self, array):
        Array = np.percentile(self.csv[array], 50, interpolation = "midpoint")
        self.array = Array
        print(f"{self.array_name} Median: {self.array}")
        return(self.array)