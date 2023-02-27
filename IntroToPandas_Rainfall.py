
#Name:
#Date:
#Purpose: To import and use a pandas DataFrame

#Read through the code and comments to ensure you understand what is happening.
#1. Use stat.mean to print the average rainfall from the rainfallSeries data.
#2. Import the data from dly3904.csv to a new dataframe variable.
#3. Rename the rainfallSeries to a more specific name.
#4. Create a new series for the Cork Airport rainfall data and print the average value to the screen.


import pandas as pd #import the pandas library
import statistics as stat #import the statistics library

#read in the data from the file to a pandas dataframe and skip the first 9 rows of information
iniscarraRainfall = pd.read_csv("dly3704.csv", skiprows=9)

print(iniscarraRainfall.head()) #print the first five lines of the dataframe to the screen

rainfallSeries = iniscarraRainfall["rain"] #Create a series

print("\n")
print(rainfallSeries)


#print(stat.mean(rainfallSeries))



