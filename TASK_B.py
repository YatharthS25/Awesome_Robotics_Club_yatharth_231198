import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("Picture 1.png")

threshold = 150  

grid_array = []

num_rows = 5 
num_cols = 5  
cell_height = image.shape[0] // num_rows
cell_width = image.shape[1] // num_cols

for i in range(num_rows):
    for j in range(num_cols):
        cell = image[i * cell_height: (i+1) * cell_height, j * cell_width: (j+1) * cell_width]

        avg_color = np.mean(cell, axis=(0, 1))

        if np.mean(avg_color) > threshold:
            grid_array.append('yellow')
        else:
            grid_array.append('blue')

grid_array = np.array(grid_array).reshape(num_rows, num_cols)


def Shortest_Path(grid_array, dimension):
    steps = 0
    ans = [[0, 0]]
    x = 0
    y = 0
    pt = [x, y]
    while (x < dimension) and (y < dimension):     
        print("Current position:", x, y)
        if (y + 1 < dimension) and (grid_array[x][y + 1] == 'yellow'):
            steps += 1
            y += 1
            ans.append([x, y]) 
            print("Moving right")
        elif (x + 1 < dimension) and (grid_array[x + 1][y] == 'yellow'):
            steps += 1
            x += 1
            ans.append([x, y]) 
            print("Moving down")
        else:
            break 
    return ans

ans = Shortest_Path(grid_array, 5)
print("Final path:", ans)
# print(grid_array)


