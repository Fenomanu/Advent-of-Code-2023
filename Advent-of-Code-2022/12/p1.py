from classes import Graph
import numpy as np

data_matrix = []
length = 0

(sr, sc) = (-1,-1)
(er, ec) = (-1,-1)


with open("input.txt") as file:
    lines = file.readlines()
    length = len(lines)
    for i in range(length): data_matrix.append([])
    row = 0
    for line in lines:
        line = line.strip()
        if line != "":
            col = 0
            for c in line:
                if c == "S": (sr, sc) = (row, col)
                elif c == "E": (er, ec) = (row, col)
                data_matrix[row].append(c)
                col += 1

        row += 1

    matrix = np.ones(length * length) * 1000

    

    print(len(matrix))

    s = (sr, sc)
    e = (er, ec)
    print(s)
    print(e)
   # for row in data_matrix: print(row)