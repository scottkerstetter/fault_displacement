import math

# 3D BLOCK

modelHeight = 200
directory = "/Users/scottkerstetter/Documents/python/fault_displacement/"
inputFileName = "fault_verts2.csv"
outputFileName = "export_for_blender.csv"

# **** START SCRIPT ****a
def read_input_file(inputFile):
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
                        "strike":float(row_items[1]),
                        "dip":float(row_items[2]),
                        "verticalDisplacement":float(row_items[3]),
                        "x1":float(row_items[4]),
                        "y1":float(row_items[5]),
                        "x2":float(row_items[6]),
                        "y2":float(row_items[7]),
                      }
            faultList.append(faultDict)
    csv.close()
    return faultList

def calc_dip_direction(faultData):
    strike = faultData['strike']
    if strike + 90 >= 360:
        dipDirection = strike + 90 - 360
    else:
        dipDirection = strike + 90
    return dipDirection

def calc_lower_fault_vert(faultData, height):
    # convert degrees to radians.  Calculate conjugate angle of dip.
    dipDirection = math.radians(faultData['dipDir'])
    dipConjugate = math.radians(90 - faultData['dip'])
    # calculate horizontal distance from upper vert
    vert_offset = height * math.tan(dipConjugate)
    # calculate x & y components of vert_offset
    xComp = vert_offset * math.sin(dipDirection)
    yComp = vert_offset * math.cos(dipDirection)
    # sum starting values with x & y components of vert_offset
    # number xy3 and xy4 in opposite order of xy1 and xy2 so blender can close polygon
    x3 = faultData['x2'] + xComp
    y3 = faultData['y2'] + yComp
    x4 = faultData['x1'] + xComp
    y4 = faultData['y1'] + yComp
    return x3, y3, x4, y4

def calc_lower_model_edge_vert():
    pass

def calc_intersection_line():
    pass

def calc_strike_from_xy():
    pass

def export_verts_for_blender(outputFile, data):
    with open(outputFile, 'w') as csv:
        for row in data:
            csv.write(row+'\n')
    csv.close()
    return

# **** INITIATE SCRIPT ****
faults = read_input_file(inputFileName)

for fault in faults:
    fault['dipDir'] = calc_dip_direction(fault)
    fault['x3'], fault['y3'], fault['x4'], fault['y4'] = calc_lower_fault_vert(fault, modelHeight)
    print(fault)

fault = faults[0]

outputData = []
for i in range(1,5):
    if i < 3:
        outputData.append(str(fault[f'x{i}'])+','+str(fault[f'y{i}'])+','+str(modelHeight))
    else:
        outputData.append(str(fault[f'x{i}'])+','+str(fault[f'y{i}'])+','+str(0))

export_verts_for_blender(outputFileName, outputData)

print("MISSION COMPLETE")
