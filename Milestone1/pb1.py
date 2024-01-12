import numpy as np
import math
def to_dict(inputFile):
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

def find_y_intercept(slope, point):
    x1, y1 = point
    y_intercept = y1 - slope * x1
    return y_intercept

def slope_from_angle(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    slope = math.tan(angle_radians)
    return slope

def generate_points_on_line(m, b, n,r):
    x_coordinates = np.linspace(-150, 150, n) 
    y_coordinates = m * x_coordinates + b
    f = open("E:\\git repos\\kla_hackathon_2024\\Milestone1\\output1.txt", "a")
    for i in range(len(x_coordinates)):
            f.write("("+ str(x_coordinates[i])+","+ str(y_coordinates[i])+")")
            f.write("\n")
    f.close()

def generate_points_on_lines(m,angle, b, n,r):
    x_coordinates = np.linspace(-r,r, n) 
    y_coordinates = m * x_coordinates + b
    angle_in_radians = math.radians(angle)
    f = open("E:\\git repos\\kla_hackathon_2024\\Milestone1\\output4.txt", "a")
    for i in range(len(x_coordinates)):
        x_result, y_result = calculate_polar_coordinates(x_coordinates[i], angle)
        f.write("("+ str(x_result)+","+ str(y_result)+")")
        f.write("\n")
    f.close()
def find_intercepts(angle_degrees):
    angle_radians = math.radians(angle_degrees)
    slope = math.tan(angle_radians)
    x_intercept = -1 * 0 / slope
    y_intercept = 0
    return x_intercept, y_intercept

a=to_dict(r"E:\git repos\kla_hackathon_2024\Milestone1\Input\Testcase1.txt"
)
angle=a["Angle"]
d=a["WaferDiameter"]
n=a["NumberOfPoints"]
slope = slope_from_angle(angle)
y_intercept = find_y_intercept(slope,(0,0))

def calculate_polar_coordinates(r, theta_degrees):
    theta_radians = math.radians(theta_degrees)
    x_component = r * math.cos(theta_radians)
    y_component = r * math.sin(theta_radians)
    return x_component, y_component

#generate_points_on_line(slope,y_intercept,n,d//2)
b=to_dict(r"E:\git repos\kla_hackathon_2024\Milestone1\Input\Testcase4.txt"
)
generate_points_on_lines(slope,b["Angle"], y_intercept,b["NumberOfPoints"],b["WaferDiameter"]//2)




