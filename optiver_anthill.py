import numpy

def inside_boundary(x, y): # define boundary here -- (0,0) must be included inside
    return ((x-2.5) / 30) ** 2 + ((y-2.5) / 40) ** 2 < 1

# define smallest rectangular enclosure for the boundary (by steps of 10)
MIN_X = -30
MAX_X = 40
MIN_Y = -40
MAX_Y = 50

# get all points the ant could reach inside the boundary
internal_boundary_points = []

for x in range(MIN_X, MAX_X, 10): 
    for y in range(MIN_Y, MAX_Y, 10):
        if inside_boundary(x,y):
            internal_boundary_points.append((x,y))

# generate matrix for system of equations
degree_system = len(internal_boundary_points)

coef_matrix = [[0 for _ in range(degree_system)] for _ in range(degree_system)]

for i, (a,b) in enumerate(internal_boundary_points):
    coef_matrix[i][internal_boundary_points.index((a, b))] = 1 # current pos
    try: coef_matrix[i][internal_boundary_points.index((a, b+10))] = -1/4 # north
    except ValueError: pass

    try: coef_matrix[i][internal_boundary_points.index((a, b-10))] = -1/4 # south
    except ValueError: pass

    try: coef_matrix[i][internal_boundary_points.index((a+10, b))] = -1/4 # east
    except ValueError: pass

    try: coef_matrix[i][internal_boundary_points.index((a-10, b))] = -1/4 # west
    except ValueError: pass

coef_matrix = numpy.array(coef_matrix)

# generate vector of values (simply all 1s)
value_vector = numpy.array([1 for _ in range(degree_system)])

# solve the system
solution = numpy.linalg.solve(coef_matrix, value_vector)

# find the time from (0,0)
average_ant_time = solution[internal_boundary_points.index((0,0))]

print(average_ant_time, numpy.rint(average_ant_time))