from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from matplotlib.patches import Arrow
from working_area import plot_working_area, is_point_inside_working_area
import numpy as np
from utils import inverse_kinematics, forward_kinematics, reflect_point_about_axis, fix_angle
import sys
import math
from PIL import Image
from matplotlib.animation import FuncAnimation
import numpy as np

animation = None


def animation_frame(i, l_1, l_2, line_1, line_2, path, resolution, lim, theta_1_min, theta_1_max, theta_2_min, theta_2_max):
    target_x = path[i][1] * resolution - lim
    target_y = path[i][0] * resolution - lim
    result = inverse_kinematics(l_1, l_2, target_x, target_y)
    if (result == None):
        line_1.set_xdata([0, 0])
        line_1.set_ydata([0, 0])
        line_2.set_xdata([0, 0])
        line_2.set_ydata([0, 0])
        return [line_1, line_2]

    [theta_1, theta_2] = result
    theta_1 = math.radians(theta_1)
    theta_2 = math.radians(theta_2)
    link_1_start_x = 0
    link_1_start_y = 0
    link_1_end_x = l_1 * math.cos(theta_1)
    link_1_end_y = l_1 * math.sin(theta_1)

    link_2_start_x = link_1_end_x
    link_2_start_y = link_1_end_y
    link_2_end_x = target_x
    link_2_end_y = target_y

    line_1.set_xdata([link_1_start_x, link_1_end_x])
    line_1.set_ydata([link_1_start_y, link_1_end_y])
    line_2.set_xdata([link_2_start_x, link_2_end_x])
    line_2.set_ydata([link_2_start_y, link_2_end_y])
    return [line_1, line_2]


def find_path(resolution, l_1, l_2, theta_1_min, theta_1_max, theta_2_min, theta_2_max, start_x, start_y, end_x, end_y):
    lim = l_1 + l_2

    tmp = start_x
    start_x = start_y
    start_y = tmp
    tmp = end_x
    end_x = end_y
    end_y = tmp


    x_values = np.arange(-lim, lim, resolution)
    y_values = np.arange(-lim, lim, resolution)

    matrix = np.zeros((x_values.size, y_values.size))

    [ax, plt, fig] = plot_working_area(l_1, l_2, theta_1_min, theta_1_max,
                                       theta_2_min, theta_2_max, False)

    for i, x in enumerate(x_values, start=0):
        for j, y in enumerate(y_values, start=0):
            if (is_point_inside_working_area((x, y))):
                matrix[i][j] = 255

    start_x = round((start_x - lim) / resolution)
    start_y = round((start_y - lim) / resolution)
    end_x = round((end_x - lim) / resolution)
    end_y = round((end_y - lim) / resolution)

    grid = Grid(matrix=matrix)
    start = grid.node(start_x, start_y)
    end = grid.node(end_x, end_y)
    finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
    path, runs = finder.find_path(start, end, grid)
    for i, path_point in enumerate(path, start=0):
        if (i == len(path) - 1):
            break
        x = path_point[1] * resolution - lim
        y = path_point[0] * resolution - lim
        x2 = path[i + 1][1] * resolution - lim
        y2 = path[i + 1][0] * resolution - lim
        dx = x2 - x
        dy = y2 - y
        ax.add_patch(Arrow(x, y, dx, dy, width=0.25, color='red'))
    x = 0
    y = 0
    x2 = path[0][1] * resolution - lim
    y2 = path[0][0] * resolution - lim
    dx = x2 - x
    dy = y2 - y
    line_1, = ax.plot(0, 0)
    line_2, = ax.plot(0, 0)
    global animation
    animation = FuncAnimation(plt.gcf(), animation_frame, frames=np.arange(
        0, len(path) - 1, 1), interval=200, fargs=(l_1, l_2, line_1, line_2, path, resolution, lim, theta_1_min, theta_1_max, theta_2_min, theta_2_max))
    plt.show()
