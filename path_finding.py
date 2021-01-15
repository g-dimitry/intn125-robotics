from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from working_area import plot_working_area, is_point_inside_working_area
import numpy as np
from utils import inverse_kinematics
import sys
import math
from PIL import Image


resolution = 0.1
l_1 = 5
l_2 = 4
theta_1_min = 0
theta_1_max = 225
theta_2_min = 0
theta_2_max = 180

start_x = 8
start_y = 3.5
end_x = 4
end_y = 2.5

lim = l_1 + l_2

x_values = np.arange(-lim, lim, resolution)
y_values = np.arange(-lim, lim, resolution)

matrix = np.zeros((x_values.size, y_values.size))

plot_working_area(l_1, l_2, theta_1_min, theta_1_max,
                  theta_2_min, theta_2_max, True)

# for i, x in enumerate(x_values, start=0):
#     for j, y in enumerate(y_values, start=0):
#         if (is_point_inside_working_area((x, y))):
#             matrix[i][j] = 255

# result = Image.fromarray((matrix).astype(np.uint8))
# result.save('out.bmp')


# with open('path.txt', 'w') as f:
#     print('\n'.join([''.join(['{:4}'.format(item) for item in row])
#       for row in matrix]), file=f)


# start_x = round((start_x - x_lim[0]) / resolution)
# start_y = round((start_y - y_lim[0]) / resolution)
# end_x = round((end_x - x_lim[1]) / resolution)
# end_y = round((end_y - y_lim[1]) / resolution)

# grid = Grid(matrix=matrix)
# start = grid.node(start_x, start_y)
# end = grid.node(end_x, end_y)
# finder = AStarFinder(diagonal_movement=DiagonalMovement.always)
# path, runs = finder.find_path(start, end, grid)
# print('operations:', runs, 'path length:', len(path))
# with open('path.txt', 'w') as f:
#     print(grid.grid_str(path=path, start=start, end=end), file=f)
#     # print('This message will be written to a file.', file=f)
