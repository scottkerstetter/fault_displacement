"""
FAULT BLOCKS

takes fault data inputs and creates fault blocks.
"""

import math

modelWidth = 1000
modelHeight = 1000


def read_block_assignment(inputFile):
    blockAssignment = []
    with open(inputFile) as csv:
        for i, row in enumerate(csv):
            if i == 0:
                continue
            row_items = row.split(',')
            row_items[1] = row_items[1].replace('\n', '') #remove newline char
            blockDict = {
                        'blockName': row_items[0],
                        'assignedFaults': row_items[1].split(' ')
                        }
            blockAssignment.append(blockDict)
    return blockAssignment

def make_point_list(block, faultList):
    # make a list of lists that can be passed to arcade
    # level 1 - list of points
    # level 2 - points (list of a single x val and single y val)
    pointList = []
    blockName = block['blockName']
    assignedFaults = block['assignedFaults']
    for faultName in assignedFaults:
        for fault in faultList:
            if faultName == fault['name']:
                if fault['p1'] not in pointList:
                    pointList.append(fault['p1'])
                if fault['p2'] not in pointList:
                    pointList.append(fault['p2'])
    return pointList