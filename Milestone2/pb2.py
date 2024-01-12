import numpy as np
import math
def to_dict():
    inputFile = r"E:\git repos\kla_hackathon_2024\Milestone1\Input\Testcase1.txt"
    mydict = {}
    with open(inputFile, 'r') as filedata:
        lines = filedata.readlines()
        for line in lines:
            if line.startswith("#") or line.startswith(" "):
                continue
            else:
                line = line.split(":")
                if line[0] not in mydict:
                    mydict[line[0]] = int(line[1])
    return mydict
a=to_dict()
die_size=a["DieSize"]
d=a["WaferDiameter"]
shift=a["DieShiftVector"]
ref=a["ReferenceDie"]
