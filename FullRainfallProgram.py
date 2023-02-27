#Name: Paudie Scanlon
#Date: 18/2/22
#Purpose: To create an interactive historical weather program

import pandas as pd
import statistics as stat
import plotly as plt
import numpy as np

weatherpd = pd.read_csv("dly3904.csv", skiprows=24)

def userChoice ():
    choice = int(input("Please choose from the following options"\
                        "\n 1: Temperature."\
                        "\n 2: Rainfall."\
                        "\n 3: Sunshine"\
                        "\n 4: Wind Gust \n"))
    return(choice)

def getData(serChoice):
    dataSeries = weatherpd[[serChoice]]
    filter = dataSeries[serChoice] !=''
    df_new = dataSeries[filter]
    return(df_new)

print("Welcome to the interactive Cork Airport Historical Weather app.")
while True:
    choice = userChoice()

    if choice == 1:
        serChoice = "maxtp"
        fullChoice = "temperature"
        unit = "C"
        break
    elif choice == 2:
        serChoice = "rain"
        fullChoice = "rainfall"
        unit = "mm"
        break
    elif choice == 3:
        serChoice = "sun"
        fullChoice = "hours of sunshine"
        unit = ""
        break
    elif choice == 4:
        serChoice = "hg"
        fullChoice = "gust of wind"
        unit = "knots"
        break
    else:
        print("Sorry, that is not a valid choice. Try again.")
        choice = userChoice

results = getData(serChoice)
sortedResults = results.sort_values(by=serChoice, ascending=True, na_position = "first")
maxValue = sortedResults.values[-1]
print("Thank you. The maximum", fullChoice, "was", maxValue, unit)
    
    


