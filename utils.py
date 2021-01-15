import math


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


def inverse_kinematics(l_1, l_2, x, y):
    try:
        theta_2 = math.acos(
            (x*x + y*y - l_1 * l_1 - l_2 * l_2)/(2 * l_1 * l_2))
        theta_1 = math.atan(
            y/x) - math.atan((l_2 * math.sin(theta_2))/(l_1 + l_2 * math.cos(theta_2)))
        return [math.degrees(theta_1), math.degrees(theta_2)]
    except:
        return None
