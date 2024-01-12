import numpy as np
import math

def convert_file_to_dictionary(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    wafer_diameter_str = lines[0].strip()
    die_size_str = lines[1].strip()
    die_shift_vector_str = lines[2].strip()
    reference_die_str = lines[3].strip()

    # Extracting values from WaferDiameter
    wafer_diameter_info = wafer_diameter_str.split(':')
    wafer_diameter = int(wafer_diameter_info[1])

    # Extracting values from DieSize
    die_size_info = die_size_str.split(':')
    die_size_width, die_size_height = map(int, die_size_info[1].split('x'))

    # Extracting values from DieShiftVector
    die_shift_vector_info = die_shift_vector_str.split(':')
    die_shift_vector = tuple(map(int, die_shift_vector_info[1][1:-1].split(',')))

    # Extracting values from ReferenceDie
    reference_die_info = reference_die_str.split(':')
    reference_die = tuple(map(int, reference_die_info[1][1:-1].split(',')))

    # Creating the dictionary
    result_dict = {
        'WaferDiameter': wafer_diameter,
        'DieSize': {
            'Width': die_size_width,
            'Height': die_size_height
        },
        'DieShiftVector': {
            'X': die_shift_vector[0],
            'Y': die_shift_vector[1]
        },
        'ReferenceDie': {
            'X': reference_die[0],
            'Y': reference_die[1]
        }
    }
    return result_dict

def isInside(circle_x, circle_y, rad, x, y):
	if ((x - circle_x) * (x - circle_x) + (y - circle_y) * (y - circle_y) <= rad * rad):
		return True;
	else:
		return False;

inputFile = r"E:\git repos\kla_hackathon_2024\Milestone2\Input\Testcase1.txt"
dic = convert_file_to_dictionary(inputFile)
d=dic["WaferDiameter"]
r=d//2
die_size=dic["DieSize"]
w=die_size["Width"]
h=die_size["Height"]	
shift_vector=dic["DieShiftVector"]
x,y=shift_vector['X'],shift_vector['Y']
ref_die=dic["ReferenceDie"]
ref_x,ref_y=ref_die['X'],ref_die['Y']
visited=[]

def dfs(x1,y1,flag):
	if x1>r or y1>r or x1<-r or y1<-r or not isInside(x,y,r, x1, y1):
		return
	if ((x1-15)//30,(y1-15)//30) not in visited:
		visited.append(((x1-15)//30,(y1-15)//30))
	if not flag:
		for i,j in ((x1+w,y1),(x1,y1+h)):
			dfs(i,j,0)
	else:
		for i,j in ((x1-w,y1),(x1,y1-h)):
			dfs(i,j,1)

dfs(ref_x,ref_y,0)
dfs(ref_x,ref_y,1)
llc_x,llc_y=ref_x-(w//2),ref_y-(h//2)
res={}
for i in visited:
	res[i]=(i[0]*w+llc_x,(i[1]*h)+llc_y)
f = open("E:\\git repos\\kla_hackathon_2024\\Milestone2\\output1.txt", "a")
for i in res:
	f.write(str(i)+":"+str(res[i]))
	f.write("\n")
f.close()


    
