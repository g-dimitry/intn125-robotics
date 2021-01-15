import numpy as np
from matplotlib.path import Path
from matplotlib.patches import Circle, Wedge, Polygon, Arc, PathPatch
from matplotlib.collections import PatchCollection
import matplotlib.pyplot as plt
import math
from utils import angle, forward_kinematics, angle_clockwise
from matplotlib.collections import PathCollection

patches = []
paths = []


def plot_working_area(l_1, l_2, theta_1_min, theta_1_max, theta_2_min, theta_2_max, plot=True):
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
    ################################################################
    current_path = Path.arc(start_angle, end_angle)
    new_verts = current_path.deepcopy().vertices
    for new_vert in new_verts:
        new_vert[0] = new_vert[0] * radius
        new_vert[1] = new_vert[1] * radius
    new_verts = new_verts[:]
    current_path = Path(new_verts, current_path.deepcopy().codes[:])
    paths.append(current_path)
    patches.append(PathPatch(current_path))
    ax.add_patch(patches[0])
    ################################################################
    ################        Link 2 at maximum       ################
    ################################################################
    end_point = forward_kinematics(l_1, l_2, theta_1_min, theta_2_max, True)
    start_point = forward_kinematics(l_1, l_2, theta_1_max, theta_2_max, True)
    radius = math.dist(end_point, o)
    start_angle = angle_clockwise(start_point, [1, 0])
    end_angle = angle_clockwise(end_point, [1, 0])
    ################################################################
    current_path = Path.arc(start_angle, end_angle)
    new_verts = current_path.deepcopy().vertices
    for new_vert in new_verts:
        new_vert[0] = new_vert[0] * radius
        new_vert[1] = new_vert[1] * radius * -1
    new_verts = new_verts[:]
    current_path = Path(new_verts, current_path.deepcopy().codes[:])
    paths.append(current_path)
    patches.append(PathPatch(current_path))
    ax.add_patch(patches[1])
    ################################################################
    ################        Link 1 at minimum       ################
    ################################################################
    center = (l_1 * math.cos(theta_1_min), l_1 * math.sin(theta_1_min))
    end_point = forward_kinematics(l_1, l_2, theta_1_min, theta_2_min, True)
    end_point = [end_point[0] - center[0], end_point[1] - center[1]]
    start_point = forward_kinematics(l_1, l_2, theta_1_min, theta_2_max, True)
    start_point = [start_point[0] - center[0], start_point[1] - center[1]]
    radius = l_2
    start_angle = angle_clockwise(start_point, [1, 0])
    end_angle = angle_clockwise(end_point, [1, 0])
    ################################################################
    current_path = Path.arc(start_angle, end_angle)
    new_verts = current_path.deepcopy().vertices
    for new_vert in new_verts:
        new_vert[0] = (new_vert[0] * radius + center[0])
        new_vert[1] = (new_vert[1] * radius + center[1]) * -1
    new_verts[np.shape(new_verts)[0] - 1] = paths[0].vertices[0]
    new_verts = new_verts[:]

    current_path = Path(new_verts, current_path.deepcopy().codes[:])
    paths.append(current_path)
    patches.append(PathPatch(current_path))
    ax.add_patch(patches[2])
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
    ################################################################
    current_path = Path.arc(start_angle, end_angle)
    new_verts = current_path.deepcopy().vertices
    for new_vert in new_verts:
        new_vert[0] = new_vert[0] * radius + center[0]
        new_vert[1] = new_vert[1] * radius + center[1]
    new_verts = new_verts[:]
    current_path = Path(new_verts, current_path.deepcopy().codes[:])
    paths.append(current_path)
    patches.append(PathPatch(current_path))
    ax.add_patch(patches[3])
    ################################################################
    ################           Plot curves          ################
    ################################################################
    ax.set_title("Working Area = {wa:.3f}".format(wa=wa))

    # tr1 = patches[0].get_transform()
    # t1 = tr1.transform_path(patches[0].get_path())
    # t1.vertices = t1.vertices[:-5]
    # t1.codes = t1.codes[:-6]
    # t1.codes = np.concatenate((t1.codes, np.array([2])))

    # tr2 = patches[1].get_transform()
    # t2 = tr2.transform_path(patches[1].get_path())
    # tr3 = patches[2].get_transform()
    # t3 = tr3.transform_path(patches[2].get_path())
    # tr4 = patches[3].get_transform()
    # t4 = tr4.transform_path(patches[3].get_path())

    # vertices = np.concatenate((t1.vertices[:],t2.vertices[:],t3.vertices[:],t4.vertices[:]))
    # cores = np.concatenate((t1.codes[:],t2.codes[:],t3.codes[:],t4.codes[:]))

    new_path = Path.make_compound_path(
        paths[0],
        paths[3],
        paths[1],
        paths[2],
    )

    old_vertices = new_path.deepcopy().vertices
    old_codes = new_path.deepcopy().codes
    new_path_vertices = []
    new_path_codes = []

    for i, old_vertex in enumerate(old_vertices, start=0):
        if (i == 0):
            new_path_vertices.append(old_vertex)
            new_path_codes.append(old_codes[i])
        else:
            if (old_codes[i] != 1):
                new_path_vertices.append(old_vertex)
                new_path_codes.append(old_codes[i])
    
    new_path = Path(new_path_vertices, new_path_codes)
    
    patches[0].remove()
    patches[1].remove()
    patches[2].remove()
    patches[3].remove()

    # path = Path(vertices, cores)

    # path2 = path.arc()
    # patches[0].remove()
    # patches[1].remove()
    # patches[3].remove()
    # patches[2].remove()

    path_patch = PathPatch(new_path, hatch='/', clip_on=True)
    ax.add_patch(path_patch)
    plt.savefig("5ara", format="svg")
    if (plot == True):
        plt.show()


def is_point_inside_working_area(point):
    isInside = False
    for patch in patches:
        transformed_point = patch.get_transform().transform(point)
        contains = patch.contains_point(transformed_point)
        if (contains == True):
            isInside = True
            break
    return isInside
