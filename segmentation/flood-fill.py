#!/usr/bin/env python
import numpy as np

def flood_fill(arr, j, i, target, replacement):
    """
        Adaption of the 8-neighbours flood fill (See https://en.wikipedia.org/wiki/Flood_fill)
        Args:
            arr(numpy.ndarray): Array to segment
            j(int): rows index
            i(int): cols index
            target(int): value to replace
            replacement(int): replacement value
    """
    if arr[j][i] == replacement:
        return arr

    if arr[j][i] != target:
        return arr

    arr[j][i] = replacement

    # 4-neighbour
    arr = flood_fill(arr, j-1, i, target, replacement)
    arr = flood_fill(arr, j+1, i, target, replacement)
    arr = flood_fill(arr, j, i-1, target, replacement)
    arr = flood_fill(arr, j, i+1, target, replacement)

    # 4-diag-neighbour
    arr = flood_fill(arr, j-1, i-1, target, replacement)
    arr = flood_fill(arr, j-1, i+1, target, replacement)
    arr = flood_fill(arr, j+1, i-1, target, replacement)
    arr = flood_fill(arr, j+1, i+1, target, replacement)

    return arr

# flood fill segmentation
arr = np.array(
    (
        (0, 0, 0, 0, 0, 0, 0, 0, 0),        
        (0, 1, 1, 1, 0, 1, 1, 1, 0),        
        (0, 1, 1, 1, 0, 1, 1, 1, 0),        
        (0, 1, 1, 0, 1, 1, 1, 1, 0),        
        (0, 0, 0, 1, 1, 1, 0, 0, 0),        
        (0, 1, 1, 1, 1, 0, 1, 1, 0),        
        (0, 1, 1, 1, 0, 1, 1, 1, 0),        
        (0, 1, 1, 1, 0, 1, 1, 1, 0),        
        (0, 0, 0, 0, 0, 0, 0, 0, 0),        
    )
)

print 'arr:\n', arr
flood_filled_arr = flood_fill(arr, 4, 4, 1, 2)
print 'result:\n', flood_filled_arr
