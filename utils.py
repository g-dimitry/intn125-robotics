import math
import numpy as np


def angle(vector_1, vector_2):
    dot = vector_1[0]*vector_2[0] + vector_1[1]*vector_2[1]
    det = vector_1[0]*vector_2[1] - vector_1[1]*vector_2[0]
    angle = math.degrees(math.atan2(det, dot))
    angle = (360 - angle) % 360
    return angle


def angle_clockwise(vector_1, vector_2):
    dot = vector_1[0]*vector_2[0] + vector_1[1]*vector_2[1]
    det = vector_1[0]*vector_2[1] - vector_1[1]*vector_2[0]
    angle = math.degrees(math.atan2(det, dot))
    angle = (angle) % 360
    return angle


def forward_kinematics(l_1, l_2, theta_1, theta_2, in_radians=False):
    if (in_radians == False):
        theta_1 = math.radians(theta_1)
        theta_2 = math.radians(theta_2)
    x = l_1 * math.cos(theta_1) + l_2 * math.cos(theta_1 + theta_2)
    y = l_1 * math.sin(theta_1) + l_2 * math.sin(theta_1 + theta_2)
    return [x, y]


def fix_angle(a):
    return math.radians((math.degrees(a) + 360) % 360)


def inverse_kinematics(l1, l2, x, y):
    try:
        if np.sqrt(x**2 + y**2) > (l1 + l2):
            theta2_goal = 0
        else:
            theta2_goal = np.arccos(
                (x**2 + y**2 - l1**2 - l2**2) / (2 * l1 * l2))
        tmp = np.math.atan2(l2 * np.sin(theta2_goal),
                            (l1 + l2 * np.cos(theta2_goal)))
        theta1_goal = np.math.atan2(y, x) - tmp

        if theta1_goal < 0:
            theta2_goal = -theta2_goal
            tmp = np.math.atan2(l2 * np.sin(theta2_goal),
                                (l1 + l2 * np.cos(theta2_goal)))
            theta1_goal = np.math.atan2(y, x) - tmp
        print(theta1_goal)
        print(theta2_goal)
        return [math.degrees(theta1_goal), math.degrees(theta2_goal)]
    except:
        return None


def reflect_point_about_axis(x, y, a):
    x2 = x * (1-a*a) / (1+a*a) + y * 2 * a / (a*a + 1)
    y2 = x * 2 * a / (a*a + 1) + y * (a*a - 1)/(a*a + 1)
    return [x2, y2]
