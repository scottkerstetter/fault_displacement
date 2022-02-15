introText = f"""
FAULT DISPLACEMENT

author: S Kerstetter
created: 2022-15-02

Calculates displacement for a fault given some inputs.  This version uses pandas for data loading and exporting.

References: 
http://www.structuralgeology.org/2012/05/how-calculate-apparent-dip-real-dip.html
https://app.visiblegeology.com/apparentDip.html
Biholar, A., 2015 (THESIS)
"""

print(introText)


# ***** SETUP SCRIPT *****
# get input file name
print("\n\nEnter File Name of Fault Attributes")
inputFileName = input("> ")
# get transport direction
print("\nEnter Azimuth of Transport Direction")
transportDirection = float(input("> "))


# dependencies
print("\nloading libraries...")
import pandas as pd
import math
from sys import exit
import datetime as dt
import numpy as np


# get today's date for output filename
today = dt.date.today()
outputFileName = "displacement_calcs_" + str(int(transportDirection)) + "_" + str(today) + ".csv"
outputLogName = "displacement_calcs_" + str(int(transportDirection)) + "_log_" + str(today) + ".txt"


# list of values used when running the script
log = []
log.append("Date: " + str(today))
log.append("File Name: " + inputFileName)
log.append("Transport Direction: " + str(transportDirection))


# read input file containing fault attributes
print("\nreading input file...")
try:
    faultData1 = pd.read_csv(inputFileName)
except:
    exit(f"\nERROR: could not find file {inputFileName}") # exit if file not found


# ***** FAULT DISPLACEMENT CALCULATIONS *****
# calc line of intersection of fault plane and vertical plane in transport direction    
def calc_apparent_dip(df, transportDirection):
    # convert strike and dip degrees from degrees to radians
    df["STRIKE RAD"] = np.deg2rad(df["STRIKE"])
    df["DIP RAD"] = np.deg2rad(df["DIP"])
    # beta equals angle between fault strike and azimuth of transport direction. Units in radians.
    df["BETA"] = df["STRIKE RAD"] - math.radians(transportDirection)
    # calc apparent dip. Units in Radians.
    df["APPARENT DIP RAD"] = abs(np.arctan(np.sin(df["BETA"]) * np.tan(df["DIP RAD"])))
    # convert apparent dip from radians to degrees
    df["APPARENT DIP"] = np.rad2deg(df["APPARENT DIP RAD"])
    return df

# calc netslip (total displacement within fault plane) from vertical component of netslip (throw).
# requires apparent dip and vertical displacement info
def calc_net_slip(df):
    df["NET SLIP"] = df["THROW"] / np.sin(df["APPARENT DIP RAD"])
    return df

# calc horizontal component of 
def calc_horizontal_displacement(df):
    df["HORIZONTAL DISPLACEMENT"] = df["THROW"] / np.tan(df["APPARENT DIP RAD"])
    return df
    

# ***** INITIATE CALCULATIONS *****
faultData2 = calc_apparent_dip(faultData1, transportDirection)
faultData3 = calc_net_slip(faultData2)
faultData4 = calc_horizontal_displacement(faultData3)


# write output file
print("\nexporting output file...")
faultData4.to_csv(outputFileName, index=False)

print("\nwriting log file...")
with open (outputLogName, "w") as txt:
    for i in log:
        txt.write(i + "\n")
txt.close()

print("\nMISSION COMPLETE")