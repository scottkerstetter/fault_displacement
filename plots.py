"""
PLOTS

a module for plotting fault data in 2D or 3D
"""
import matplotlib.pyplot as plt

def plot_map(faultList):
    # find min and max x and y values for plotting edges of map
    for i, fault in enumerate(faultList):
        if i == 0:
            xMin = min(fault['x'])
            xMax = max(fault['x'])
            yMin = min(fault['y'])
            yMax = max(fault['y'])
        else:
            if min(fault['x']) < xMin:
                xMin = min(fault['x'])
            if max(fault['x']) > xMax:
                xMax = max(fault['x'])
            if min(fault['y']) < yMin:
                yMin = min(fault['y'])
            if max(fault['y']) > yMax:
                yMax = max(fault['y'])
        
    fig, ax = plt.subplots(1,1, figsize=(7,7))
    # set scales equal to max value
    plt.xlim(xMin,xMax)    
    plt.ylim(yMin,yMax)
    plt.axis('square')
    # plot each fault line
    for fault in faultList:
        ax.plot(fault["x"], fault["y"], label=fault["name"])
    ax.legend()
    plt.show()
    
    
    
def plot_fault_3d():
    pass