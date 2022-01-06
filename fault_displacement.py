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
inputFileName2 = "block_assignment.csv"
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

def read_fault_xy_for_plt(inputFile):
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


def read_fault_xy_for_arcade(inputFile):
    with open (inputFile) as csv:
        faultList = []
        for i, row in enumerate(csv):
            if i == 0:
                continue
            row_items = row.split(',')
            faultDict = {
                "name":row_items[0],
                "p1":(float(row_items[1]),float(row_items[2])),
                "p2":(float(row_items[3]),float(row_items[4]))
            }
            faultList.append(faultDict)
    return faultList

def read_vertices(inputFile):
    masterList = []
    with open (inputFile) as csv:
        for i, row in enumerate(csv):
            if i == 0:
                continue
            row_items = row.split(',')
            block_id = row_item[0]
            x = int(row_item[1])
            y = int(row_item[2])
    return masterList


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

def move_block_model():
    # create list of blocks that need to be moved.
    # pop blocks from list after they are moved.
    # keep running sum of horizontal displacement equal to current block and all previous blocks.
    pass

# **** INITIATE SCRIPT ****
if __name__ == "__main__":
    print("Welcome to Fault Displacement!")
    print("reading input file...")
    faultList = read_fault_xy_for_plt(inputFileName)

    for fault in faultList:
        print(fault)

    plots.plot_map(faultList)

    """
    blockAssignment = fault_blocks.read_block_assignment(inputFileName2)

    for block in blockAssignment:
        print(block)



    masterList = []
    for block in blockAssignment:
        masterList.append(fault_blocks.make_point_list(block, faultList))

    draw_blocks.render_fault_block(masterList[1])

    draw_blocks.arcade.run()
    """
    # for fault in faultList:
        # fault["netSlip"] = calc_netslip(fault, transDirDeg)
        # fault["horizontalDisplacement"] = calc_horizontal_displacement(fault, transDirDeg)
        # print(fault)