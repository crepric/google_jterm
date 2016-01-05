# You are asked to find the index of the maximum value of an array of data under
# the assumption that the first part of the array is increasing, and then it
# becomes decreasing.  For example, if we are given this array:
#
#                   5 12 17 22 25 37 23 11 6 4 2 1
#
# our code should return the index of number 37 in the array, which is 5.

def find_max_idx(sorted_array):
    if len(sorted_array) == 0:
        return -1
    max_val = 0
    max_idx = 0
    for current_idx in range(0, len(sorted_array)):
        if sorted_array[current_idx] > max_val:
            max_idx = current_idx
        else:
            break
    return max_idx
