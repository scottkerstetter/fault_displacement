import fault_displacement as fd
import plots

inputFileName = "fault_model.csv"

faultList = fd.read_fault_xy_for_plt(inputFileName)

for fault in faultList:
    print(fault)

plots.plot_map(faultList)