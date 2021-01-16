from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from matplotlib.patches import Arrow
from working_area import plot_working_area, is_point_inside_working_area
import numpy as np
from utils import inverse_kinematics
import sys
import math
from PIL import Image

# resolution = 0
# l_1 = 5
# l_2 = 4
# theta_1_min = 0
# theta_1_max = 225
# theta_2_min = 0
# theta_2_max = 180
# start_x = 5
# start_y = 5
# end_x = 5
# end_y = 5

def find_path(resolution, l_1, l_2, theta_1_min, theta_1_max, theta_2_min, theta_2_max, start_x, start_y, end_x, end_y):
    lim = l_1 + l_2

    x_values = np.arange(-lim, lim, resolution)
    y_values = np.arange(-lim, lim, resolution)

    matrix = np.zeros((x_values.size, y_values.size))

    [ax, plt] = plot_working_area(l_1, l_2, theta_1_min, theta_1_max,
                                  theta_2_min, theta_2_max, False)

    for i, x in enumerate(x_values, start=0):
        for j, y in enumerate(y_values, start=0):
            if (is_point_inside_working_area((x, y))):
                matrix[i][j] = 255

    result = Image.fromarray((matrix).astype(np.uint8))
    result.save('out.bmp')

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
    plt.show()
