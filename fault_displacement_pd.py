print("""
FAULT DISPLACEMENT

version: 
author: 
created: 

Calculates displacement for a fault given some inputs.

References: Biholar, A., 2015
""")


print("importing libraries...")
import math
import pandas as pd


# input variables
inputFileName = "faults.csv"
transDirDeg = 295 # transport direction in degrees

print("reading input file...")
df = pd.read_csv(inputFileName)

print(df)

# **** START SCRIPT ****
def convert_to_radians(df, transportDirection):
    # convert strike and dip from degrees into radians and create new cols
    strikeList = []
    dipList = []
    for row in range(len(df)):
        strikeList.append(math.radians(df['strike'][row]))
        dipList.append(math.radians(df['dip'][row]))
    df['strike_rad'] = strikeList
    df['dip_rad'] = dipList
    #convert transport direction to radians
    transportDirection = math.radians(transportDirection)
    return df, transportDirection


def calc_apparent_dip(df, transportDirection):
    df['theta1_rad'] = df['dip_rad']
    df['rho1_rad'] = df['strike_rad'] - transport
    return df

def calc_netslip(df):
    pass


# **** INITIATE SCRIPT ****
df, transDirRad = convert_to_radians(df, transDirDeg)

print("transDirDeg", transDirDeg)
print("transDirRad", transDirRad)
print(df)