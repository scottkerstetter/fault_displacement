print("""
FAULT DISPLACEMENT

version: 1.0
author: S Kerstetter
created: 2021-12-20

Calculates displacement for a fault given some inputs.

References: 
http://www.structuralgeology.org/2012/05/how-calculate-apparent-dip-real-dip.html
https://app.visiblegeology.com/apparentDip.html
Biholar, A., 2015 (THESIS)
""")

print("importing libraries...")
import math

# input variables
inputFileName = "faults.csv"
transDirDeg = 295 # transport direction in degrees

# **** START SCRIPT ****
def read_input_file(inputFile):
    # reads input file (csv)
    # extracts fault names, strikes and dips
    with open(inputFile) as csv:
        faultList = []
        for row in csv:
            row_items = row.split(',')
            faultDict = {
                        "id":row_items[0],
                        "strike":int(row_items[1]),
                        "dip":int(row_items[2]),
                        "verticalDisplacement":int(row_items[3])
                      }
            faultList.append(faultDict)
    return faultList

def calc_apparent_dip(faultData, transportDirection):
    # convert strike and dip (delta) into radians
    strike = math.radians(faultData['strike'])
    dip = math.radians(faultData['dip'])
    # beta equal angle between fault strike and azimuth of transport direction
    beta = strike - math.radians(transportDirection)
    # calculate apparent dip
    apparentDip = abs(math.atan (math.sin(beta) * math.tan(dip)))
    return math.degrees(apparentDip)

def calc_netslip(faultData, transportDirection):
    # convert apparent dip into radians
    apparentDip = calc_apparent_dip(faultData, transportDirection)
    dip = math.radians(apparentDip)
    # calculate net slip
    netSlip = faultData['verticalDisplacement'] / math.sin(dip)
    return netSlip

def calc_horizontal_displacement(faultData, transportDirection):
    # convert apparent dip to radians
    apparentDip = calc_apparent_dip(faultData, transportDirection)
    dip = math.radians(apparentDip)
    # calculate horizontal movement parallel to transport direction / apparent dip
    horizontalDisplacement = faultData['verticalDisplacement'] / math.tan(dip)
    return horizontalDisplacement

# **** INITIATE SCRIPT ****
print("reading input file...")
faultList = read_input_file(inputFileName)
    
for fault in faultList:
    fault["netSlip"] = calc_netslip(fault, transDirDeg)
    fault["horizontalDisplacement"] = calc_horizontal_displacement(fault, transDirDeg)
    print(fault)