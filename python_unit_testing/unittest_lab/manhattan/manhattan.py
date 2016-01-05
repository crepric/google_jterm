# Imagine in a city with streets that form a regular 2D grid.
# Streets are North-South or East-West, and all blocks have the same length.
#
# N people start out at different intersections and want to meet up.
# They are only able to move along the roads (no crossing blocks diagonally etc.).
# Find the meeting place that minimizes the total travel distance.
#
# HINT: We should not tell you, but the correct answer to this problem
# is not unique. If you prefer spoilers, you can ask Riccardo about it,
# so you can get going with the tests. 

import sys
import random

def sum_distances(coordinates, meeting_point):
    current_distance = 0
    for coord in coordinates:
        current_distance += (abs(meeting_point[0] - coord[0]) +
                            abs(meeting_point[1] - coord[1]))
    return current_distance

def find_meeting_point(coordinates):
    xs = [x for (x,y) in coordinates]
    ys = [y for (x,y) in coordinates]
    min_distance = sys.maxint
    best_coords = (-1, -1)
    for x in xs:
        for y in ys:
            current_distance = sum_distances(coordinates, (x,y))
            if current_distance < min_distance:
                best_coords = (x,y)
                min_distance = current_distance
    return best_coords
