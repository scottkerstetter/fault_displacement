"""
FAULT DISPLACEMENT

author: S Kerstetter
created: 2021-12-20

Calculates displacement for a fault given some inputs.

References: 
http://www.structuralgeology.org/2012/05/how-calculate-apparent-dip-real-dip.html
https://app.visiblegeology.com/apparentDip.html
Biholar, A., 2015 (THESIS)
"""

print("importing libraries...")
import math
import plots

# input variables
inputFileName = "fault_model.csv"
transDirDeg = 295 # transport direction in degrees

# **** IMPORT FUNCTIONS ****
# read fault data in one of two formats:
# - strike and dip data
# - two xy points along a fault's strike line
def read_fault_orientations(inputFile):
    # reads input file (csv)
    # extracts fault names, strikes and dips
    with open(inputFile) as csv:
        faultList = []
        for i, row in enumerate(csv):
            if i == 0:
                continue
            row_items = row.split(',')
            faultDict = {
                        "id":row_items[0],
                        "strike":int(row_items[1]),
                        "dip":int(row_items[2]),
                        "verticalDisplacement":int(row_items[3])
                      }
            faultList.append(faultDict)
    return faultList

def read_fault_xy(inputFile):
    with open (inputFile) as csv:
        faultList = []
        for i, row in enumerate(csv):
            if i == 0:
                continue
            row_items = row.split(',')
            faultDict = {
                "name":row_items[0],
                "x":(float(row_items[1]),float(row_items[3])),
                "y":(float(row_items[2]),float(row_items[4]))
            }
            faultList.append(faultDict)
    return faultList

# **** CALCULATIONS FOR FAULT DISPLACEMENT ****
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

def calc_dip_direction():
    pass

# **** FUNCTIONS USED FOR INPUTS OF XY DATA ****
def calc_strike_from_xy():
    # calculate the strike line of a fault given 2 points (xy's)
    pass

    
def calc_dip_direction_from_text():
    # used to calculate dip direction from cardinal directions such as "east", "north", etc.
    pass

# **** INITIATE SCRIPT ****
print("Welcome to Fault Displacement!")
print("reading input file...")
faultList = read_fault_xy(inputFileName)

for fault in faultList:
    print(fault)

plots.plot_map(faultList)

# for fault in faultList:
    # fault["netSlip"] = calc_netslip(fault, transDirDeg)
    # fault["horizontalDisplacement"] = calc_horizontal_displacement(fault, transDirDeg)
    # print(fault)