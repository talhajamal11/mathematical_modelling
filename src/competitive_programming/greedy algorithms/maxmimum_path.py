""" 
You can only go down or up in a n x m matrix. Each point has a number. Find the path that maximises the sum
of the numbers you traverse over
"""
import numpy as np

rows = 3
cols = 4
matrix =[[rows*i + j + 1 for j in range(rows)] for i in range(cols)]
max_path = [[0] * (rows)] * cols
#print(max_path)

for y in range(cols + 1):
    for x in range(rows + 1):
        max_path[y][x] = matrix[y][x] + max(max_path[y-1][x], max_path[y][x-1])
    