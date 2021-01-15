import numpy as np
from matplotlib.patches import Circle, Wedge, Polygon, Arc
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import math
from utils import angle, forward_kinematics


def plot_working_area(l_1, l_2, theta_1_min, theta_1_max, theta_2_min, theta_2_max):
    ################################################################
    ################  Transform angles to radians   ################
    ################################################################
    theta_1_min = math.radians(theta_1_min)
    theta_1_max = math.radians(theta_1_max)
    theta_2_min = math.radians(theta_2_min)
    theta_2_max = math.radians(theta_2_max)
    ################################################################
    ################     Calculate Working Area     ################
    ################################################################
    wa = l_1 * l_2 * (math.cos(theta_2_min) -
                      math.cos(theta_2_max)) * (theta_1_max - theta_1_min)
    ################################################################
    ################           Setup Graph          ################
    ################################################################
    patches = []
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')
    ax.autoscale(True, 'both')
    ################################################################
    ################        Common Variables        ################
    ################################################################
    o = [0, 0]
    ################################################################
    ################        Link 2 at minimum       ################
    ################################################################
    start_point = forward_kinematics(l_1, l_2, theta_1_min, theta_2_min, True)
    end_point = forward_kinematics(l_1, l_2, theta_1_max, theta_2_min, True)
    radius = math.dist(end_point, o)
    start_angle = angle(start_point, [1, 0])
    end_angle = angle(end_point, [1, 0])
    ax.add_patch(Wedge((0, 0), radius, start_angle, end_angle, fill=False,
                       edgecolor='black', width=0))
    ################################################################
    ################        Link 2 at maximum       ################
    ################################################################
    start_point = forward_kinematics(l_1, l_2, theta_1_min, theta_2_max, True)
    end_point = forward_kinematics(l_1, l_2, theta_1_max, theta_2_max, True)
    radius = math.dist(end_point, o)
    start_angle = angle(start_point, [1, 0])
    end_angle = angle(end_point, [1, 0])
    ax.add_patch(Wedge((0, 0), radius, start_angle, end_angle, fill=False,
                       edgecolor='black', width=0))
    ################################################################
    ################        Link 1 at minimum       ################
    ################################################################
    center = (l_1 * math.cos(theta_1_min), l_1 * math.sin(theta_1_min))
    start_point = forward_kinematics(l_1, l_2, theta_1_min, theta_2_min, True)
    start_point = [start_point[0] - center[0], start_point[1] - center[1]]
    end_point = forward_kinematics(l_1, l_2, theta_1_min, theta_2_max, True)
    end_point = [end_point[0] - center[0], end_point[1] - center[1]]
    radius = l_2
    start_angle = angle(start_point, [1, 0])
    end_angle = angle(end_point, [1, 0])
    ax.add_patch(Wedge(center, radius, start_angle, end_angle, fill=False,
                       edgecolor='black', width=0))
    ################################################################
    ################        Link 1 at maximum       ################
    ################################################################
    center = (l_1 * math.cos(theta_1_max), l_1 * math.sin(theta_1_max))
    start_point = forward_kinematics(l_1, l_2, theta_1_max, theta_2_min, True)
    start_point = [start_point[0] - center[0], start_point[1] - center[1]]
    end_point = forward_kinematics(l_1, l_2, theta_1_max, theta_2_max, True)
    end_point = [end_point[0] - center[0], end_point[1] - center[1]]
    radius = l_2
    start_angle = angle(start_point, [1, 0])
    end_angle = angle(end_point, [1, 0])
    ax.add_patch(Wedge(center, radius, start_angle, end_angle, fill=False,
                       edgecolor='black', width=0))
    ################################################################
    ################           Plot curves          ################
    ################################################################
    ax.set_title("Working Area = {wa:.3f}".format(wa=wa))
    plt.show()
