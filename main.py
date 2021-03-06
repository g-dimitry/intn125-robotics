import numpy as np
from matplotlib.patches import Circle, Wedge, Polygon, Arc
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import math
from working_area import plot_working_area
from utils import forward_kinematics, angle, inverse_kinematics
from path_finding import find_path
# Modes:
# 1 - Forward Kinematics
# 2 - Inverse Kinematics
# 3 - Working Area
# 4 - Robot Animation

print("Modes: \n")
print("1) Forward Kinematics \n")
print("2) Inverse Kinematics \n")
print("3) Working Area \n")
print("4) Path finding \n")
mode = int(input("Please select a mode: "))

if (mode == 1):
    l_1 = int(input("Please input link 1 length: "))
    theta_1 = int(input("Please input link 1 angle in degrees: "))
    l_2 = int(input("Please input link 2 length: "))
    theta_2 = int(input("Please input link 2 angle in degrees: "))
    [x, y] = forward_kinematics(l_1, l_2, theta_1, theta_2)
    print(round(x, 3))
    print(round(y, 3))
elif (mode == 2):
    l_1 = int(input("Please input link 1 length: "))
    l_2 = int(input("Please input link 2 length: "))
    x = int(input("Please input x: "))
    y = int(input("Please input y: "))
    [theta_1, theta_2] = inverse_kinematics(l_1, l_2, x, y)
    print("Theta 1")
    print(theta_1)
    print("Theta 2")
    print(theta_2)
elif (mode == 3):
    l_1 = int(input("Please input link 1 length: "))
    l_2 = int(input("Please input link 2 length: "))
    theta_1_min = int(input("Please input theta 1 min in angles: "))
    theta_1_max = int(input("Please input theta 1 max in angles: "))
    theta_2_min = int(input("Please input theta 2 min in angles: "))
    theta_2_max = int(input("Please input theta 2 max in angles: "))
    plot_working_area(
        l_1, l_2, theta_1_min, theta_1_max, theta_2_min, theta_2_max)
elif (mode == 4):
    resolution = float(input("Please input resolution: "))
    l_1 = int(input("Please input link 1 length: "))
    l_2 = int(input("Please input link 2 length: "))
    theta_1_min = int(input("Please input theta 1 min in angles: "))
    theta_1_max = int(input("Please input theta 1 max in angles: "))
    theta_2_min = int(input("Please input theta 2 min in angles: "))
    theta_2_max = int(input("Please input theta 2 max in angles: "))
    start_x = float(input("Please input start x: "))
    start_y = float(input("Please input start y: "))
    end_x = float(input("Please input end x: "))
    end_y = float(input("Please input end y: "))
    find_path(resolution, l_1, l_2, theta_1_min, theta_1_max,
              theta_2_min, theta_2_max, start_x, start_y, end_x, end_y)
