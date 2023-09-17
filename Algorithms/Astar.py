import sys

# For getting input from input.txt file
sys.stdin = open("D:\myCode\Python\Algorithms\input.txt", "r")

# Printing the Output to output.txt file
sys.stdout = open("D:\myCode\Python\Algorithms\output.txt", "w")


visited = []
queue = []


def printgrid(grid):
    # print(grid)

    for r in grid:
        for c in r:
            print(c, end=" ")
        print()


def sorting(x):
    return x[1]


def Up(grid_copy, pacpos):
    i = pacpos[0][0]  # [[1,2],4]
    j = pacpos[0][1]
    print(i)
    print(pacpos)
    if i > 0:
        # print(i, j, end=" , ")
        # printgrid(grid)  # function
        if grid[i - 1][j] != "%":
            return [i - 1, j]
    return pacpos


def Down(grid, pacpos):
    global grid_r
    i = pacpos[0][0]
    j = pacpos[0][1]

    if i < (grid_r - 1):
        if grid[i + 1][j] != "%":
            return [i + 1, j]
    return pacpos


def Left(grid, pacpos):
    global grid_c
    i = pacpos[0][0]
    j = pacpos[0][1]

    if j > 0:
        if grid[i][j - 1] != "%":
            return [i, j - 1]
    return pacpos


def Right(grid, pacpos):
    global grid_c
    i = pacpos[0][0]
    j = pacpos[0][1]

    if j < (grid_c - 1):
        if grid[i][j + 1] != "%":
            return [i, j + 1]
    return pacpos


def heuristic(pacpos, foodpos):
    r = pacpos[0]
    c = pacpos[1]
    r1 = foodpos[0]
    c1 = foodpos[1]
    return abs(r1 - r) + abs(c1 - c)


def Astar(pacpos, foodpos, grid):
    cost = 0
    global queue
    while queue:
        m = queue.pop(0)  # [[1,2], 4]
        visited.append(m)
        cost = cost + 1

        temp = Up(grid, m)
        if temp == foodpos:
            visited.append(foodpos)
            return 1
        else:
            if temp != pacpos:
                if temp not in visited:
                    h = heuristic(temp, foodpos)
                    c = cost + h
                    queue.append([temp, c])  # [[1,2], 4]

        temp = Left(grid, m)
        if temp == foodpos:
            visited.append(foodpos)
            return 1
        else:
            if temp != pacpos:
                if temp not in visited:
                    h = heuristic(temp, foodpos)
                    c = cost + h
                    queue.append([temp, c])

        temp = Right(grid, m)
        if temp == foodpos:
            visited.append(foodpos)
            return 1
        else:
            if temp != pacpos:
                if temp not in visited:
                    h = heuristic(temp, foodpos)
                    c = cost + h
                    queue.append([temp, h, c])

        temp = Down(grid, m)
        if temp == foodpos:
            visited.append(foodpos)
            return 1
        else:
            if temp != pacpos:
                if temp not in visited:
                    h = heuristic(temp, foodpos)
                    c = cost + h
                    queue.append([temp, c])

    return 1


pacpos = []
# for i in range(0, 2):
#     ele = int(input())

pacpos_r, pacpos_c = map(int, input().split())
pacpos.append(pacpos_r)
pacpos.append(pacpos_c)

foodpos = []
foodpos_r, foodpos_c = map(int, input().split())
foodpos.append(foodpos_r)
foodpos.append(foodpos_c)

gridsize = []
grid_r, grid_c = map(int, input().split())
gridsize.append(grid_r)
gridsize.append(grid_c)

grid = []
for i in range(0, grid_r):
    inputs = list(input())
    grid.append(inputs)


# print(pacpos)
# print(foodpos)

# print(gridsize)
# print(grid)
queue.sort(key=sorting)

queue.append([pacpos, 0])
Astar(pacpos, foodpos, grid)

import copy

distance_path = copy.deepcopy(visited)
print(len(visited))

while visited:
    temp = visited.pop(0)
    print(f"{temp[0]} {temp[1]}")


print(len(distance_path) - 1)
while distance_path:
    temp = distance_path.pop(0)
    print(f"{temp[0]} {temp[1]}")
