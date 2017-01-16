"""
463 Island Perimeter

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:




grid = [[0,1,0,0],
        [1,1,1,0],
        [0,1,0,0],
        [1,1,0,0]]

"""
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        num_1 = 0
        horizontal_neighbor = 0
        vertical_neighbor = 0
        for i in grid:
            for position in range(len(i)):
                if i[position] == 1:
                    num_1 += 1
                    if position < len(i) - 1:
                        if i[position+1] == 1:
                            horizontal_neighbor += 1
        transpose = list(map(list, zip(*grid)))
        for j in transpose:
            for position in range(len(j)):
                if j[position] == 1:
                    if position < len(j) - 1:
                        if j[position+1] == 1: 
                            vertical_neighbor += 1
        
        total_line = num_1 * 4
        total_line_horizontal = horizontal_neighbor * 2
        total_line_vertical = vertical_neighbor * 2
        final = total_line - total_line_horizontal - total_line_vertical
        
        return final

"""
Better solution need to study more:
def islandPerimeter(self, grid):
    return sum(sum(map(operator.ne, [0] + row, row + [0]))
               for row in grid + map(list, zip(*grid)))
        