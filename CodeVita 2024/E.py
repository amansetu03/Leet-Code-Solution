# # # # # # # import math
# # # # # # #
# # # # # # #
# # # # # # # def calculate_presses():
# # # # # # #     # Input: Number of vertices
# # # # # # #     n = int(input("Enter number of vertices: "))
# # # # # # #
# # # # # # #     # Input: Vertices of the wall
# # # # # # #     vertices = [tuple(map(int, input().split())) for _ in range(n)]
# # # # # # #
# # # # # # #     # Input: Size of the brush
# # # # # # #     m = int(input("Enter the brush size: "))
# # # # # # #
# # # # # # #     # Step 1: Calculate the bounding box of the wall
# # # # # # #     min_x = min(v[0] for v in vertices)
# # # # # # #     max_x = max(v[0] for v in vertices)
# # # # # # #     min_y = min(v[1] for v in vertices)
# # # # # # #     max_y = max(v[1] for v in vertices)
# # # # # # #
# # # # # # #     # Step 2: Calculate the width and height of the wall
# # # # # # #     width = max_x - min_x + 1  # Inclusive range
# # # # # # #     height = max_y - min_y + 1  # Inclusive range
# # # # # # #
# # # # # # #     # Step 3: Calculate the number of presses
# # # # # # #     presses_x = math.ceil(width / m)  # Presses needed in the x-direction
# # # # # # #     presses_y = math.ceil(height / m)  # Presses needed in the y-direction
# # # # # # #     total_presses = presses_x * presses_y  # Total presses
# # # # # # #
# # # # # # #     # Output the result
# # # # # # #     print("Minimum number of presses required:", total_presses)
# # # # # # #
# # # # # # #
# # # # # # # # Run the function
# # # # # # # calculate_presses()
# # # # # #
# # # # # # import math
# # # # # #
# # # # # #
# # # # # # def calculate_presses():
# # # # # #     # Input: Number of vertices
# # # # # #     n = int(input("Enter number of vertices: "))
# # # # # #
# # # # # #     # Input: Vertices of the wall
# # # # # #     vertices = [tuple(map(int, input().split())) for _ in range(n)]
# # # # # #
# # # # # #     # Input: Size of the brush
# # # # # #     m = int(input("Enter the brush size: "))
# # # # # #
# # # # # #     # Step 1: Calculate the bounding box of the wall
# # # # # #     min_x = min(v[0] for v in vertices)
# # # # # #     max_x = max(v[0] for v in vertices)
# # # # # #     min_y = min(v[1] for v in vertices)
# # # # # #     max_y = max(v[1] for v in vertices)
# # # # # #
# # # # # #     # Step 2: Calculate the effective width and height of the wall
# # # # # #     width = max_x - min_x + 1  # Inclusive range for x-coordinates
# # # # # #     height = max_y - min_y + 1  # Inclusive range for y-coordinates
# # # # # #
# # # # # #     # Step 3: Calculate the minimum number of presses
# # # # # #     # Number of presses in the x-direction (cover width)
# # # # # #     presses_x = math.ceil(width / m)
# # # # # #     # Number of presses in the y-direction (cover height)
# # # # # #     presses_y = math.ceil(height / m)
# # # # # #     # Total presses needed
# # # # # #     total_presses = presses_x * presses_y
# # # # # #
# # # # # #     # Output the result
# # # # # #     print("Minimum number of presses required:", total_presses)
# # # # # #
# # # # # #
# # # # # # # Run the function
# # # # # # calculate_presses()
# # # # #
# # # # # import math
# # # # # from collections import deque
# # # # #
# # # # #
# # # # # def is_inside_polygon(x, y, vertices):
# # # # #     """Check if a point (x, y) lies inside the polygon using the ray-casting algorithm."""
# # # # #     n = len(vertices)
# # # # #     inside = False
# # # # #     px, py = vertices[0]
# # # # #     for i in range(1, n + 1):
# # # # #         cx, cy = vertices[i % n]
# # # # #         if y > min(py, cy) and y <= max(py, cy) and x <= max(px, cx):
# # # # #             if py != cy:
# # # # #                 xinters = (y - py) * (cx - px) / (cy - py) + px
# # # # #             if px == cx or x <= xinters:
# # # # #                 inside = not inside
# # # # #         px, py = cx, cy
# # # # #     return inside
# # # # #
# # # # #
# # # # # def calculate_presses():
# # # # #     # Input: Number of vertices
# # # # #     n = int(input("Enter number of vertices: "))
# # # # #
# # # # #     # Input: Vertices of the wall
# # # # #     vertices = [tuple(map(int, input().split())) for _ in range(n)]
# # # # #
# # # # #     # Input: Size of the brush
# # # # #     m = int(input("Enter the brush size: "))
# # # # #
# # # # #     # Step 1: Find bounding box of the wall
# # # # #     min_x = min(v[0] for v in vertices)
# # # # #     max_x = max(v[0] for v in vertices)
# # # # #     min_y = min(v[1] for v in vertices)
# # # # #     max_y = max(v[1] for v in vertices)
# # # # #
# # # # #     # Step 2: Fill a grid to represent the wall
# # # # #     wall = set()  # Set of all points that need to be painted
# # # # #     for x in range(min_x, max_x + 1):
# # # # #         for y in range(min_y, max_y + 1):
# # # # #             if is_inside_polygon(x, y, vertices):
# # # # #                 wall.add((x, y))
# # # # #
# # # # #     # Step 3: Calculate the number of presses needed
# # # # #     presses = 0
# # # # #     while wall:
# # # # #         # Pick a point in the wall to paint with the brush
# # # # #         x, y = next(iter(wall))
# # # # #         # Remove all points covered by the brush press
# # # # #         for i in range(m):
# # # # #             for j in range(m):
# # # # #                 wall.discard((x + i, y + j))
# # # # #         presses += 1
# # # # #
# # # # #     # Output the result
# # # # #     print("Minimum number of presses required:", presses)
# # # # #
# # # # #
# # # # # # Run the function
# # # # # calculate_presses()
# # # # import math
# # # #
# # # #
# # # # def is_inside_polygon(x, y, vertices):
# # # #     """Check if a point (x, y) lies inside the polygon using the ray-casting algorithm."""
# # # #     n = len(vertices)
# # # #     inside = False
# # # #     px, py = vertices[0]
# # # #     for i in range(1, n + 1):
# # # #         cx, cy = vertices[i % n]
# # # #         if y > min(py, cy) and y <= max(py, cy) and x <= max(px, cx):
# # # #             if py != cy:
# # # #                 xinters = (y - py) * (cx - px) / (cy - py) + px
# # # #             if px == cx or x <= xinters:
# # # #                 inside = not inside
# # # #         px, py = cx, cy
# # # #     return inside
# # # #
# # # #
# # # # def calculate_presses():
# # # #     # Input: Number of vertices
# # # #     n = int(input("Enter number of vertices: "))
# # # #
# # # #     # Input: Vertices of the wall
# # # #     vertices = [tuple(map(int, input().split())) for _ in range(n)]
# # # #
# # # #     # Input: Size of the brush
# # # #     m = int(input("Enter the brush size: "))
# # # #
# # # #     # Step 1: Find bounding box of the wall
# # # #     min_x = min(v[0] for v in vertices)
# # # #     max_x = max(v[0] for v in vertices)
# # # #     min_y = min(v[1] for v in vertices)
# # # #     max_y = max(v[1] for v in vertices)
# # # #
# # # #     # Step 2: Use a grid-based approach
# # # #     presses = 0
# # # #     for x in range(min_x, max_x + 1, m):
# # # #         for y in range(min_y, max_y + 1, m):
# # # #             # Check if the top-left corner of the current brush placement is inside the polygon
# # # #             if any(is_inside_polygon(x + dx, y + dy, vertices) for dx in range(m) for dy in range(m)):
# # # #                 presses += 1
# # # #
# # # #     # Output the result
# # # #     print("Minimum number of presses required:", presses)
# # # #
# # # #
# # # # # Run the function
# # # # calculate_presses()
# # #
# # # def get_wall_area(vertices):
# # #     n = len(vertices)
# # #     area = 0
# # #     for i in range(n):
# # #         x1, y1 = vertices[i]
# # #         x2, y2 = vertices[(i + 1) % n]
# # #         area += x1 * y2 - y1 * x2
# # #     return abs(area) / 2
# # #
# # #
# # # def min_presses_to_cover_wall(vertices, brush_size):
# # #     x_coords = [x for x, y in vertices]
# # #     y_coords = [y for x, y in vertices]
# # #
# # #     min_x, max_x = min(x_coords), max(x_coords)
# # #     min_y, max_y = min(y_coords), max(y_coords)
# # #
# # #     width = max_x - min_x
# # #     height = max_y - min_y
# # #
# # #     # Calculate required presses along x and y axis
# # #     presses_x = (width + brush_size - 1) // brush_size
# # #     presses_y = (height + brush_size - 1) // brush_size
# # #
# # #     return presses_x * presses_y
# # #
# # #
# # # # Read input
# # # N = int(input().strip())
# # # vertices = [tuple(map(int, input().strip().split())) for _ in range(N)]
# # # M = int(input().strip())
# # #
# # # # Calculate the area of the wall
# # # wall_area = get_wall_area(vertices)
# # #
# # # # Check area constraint
# # # if wall_area / (M * M) < 7:
# # #     min_presses = min_presses_to_cover_wall(vertices, M)
# # #     print(min_presses)
# # # else:
# # #     print("Invalid wall area for the given brush size.")
# # import sys
# #
# #
# # def isInside(x, y, verts):
# #     cross = 0
# #     N = len(verts)
# #     for i in range(N):
# #         x1, y1 = verts[i]
# #         x2, y2 = verts[(i + 1) % N]
# #         if (y1 <= y and y2 > y) or (y2 <= y and y1 > y):
# #             ix = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
# #             if ix > x:
# #                 cross += 1
# #     return cross % 2 != 0
# #
# #
# # def calculate_min_presses():
# #     N = int(input())
# #     verts = [tuple(map(int, input().split())) for _ in range(N)]
# #
# #     M = int(input())
# #
# #     minX = min(v[0] for v in verts)
# #     maxX = max(v[0] for v in verts)
# #     minY = min(v[1] for v in verts)
# #     maxY = max(v[1] for v in verts)
# #
# #     w = maxX - minX + 1
# #     h = maxY - minY + 1
# #
# #     grid = [[0] * w for _ in range(h)]
# #
# #     # Fill grid with 1's where the points are inside the polygon
# #     for y in range(minY, maxY):
# #         for x in range(minX, maxX):
# #             if isInside(x + 0.5, y + 0.5, verts):
# #                 grid[y - minY][x - minX] = 1
# #
# #     # Gather all the cells that are inside the polygon
# #     cells = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == 1]
# #
# #     # Sort cells by row and column
# #     cells.sort()
# #
# #     minPresses = sys.maxsize
# #
# #     def backtrack(idx, curGrid, presses):
# #         nonlocal minPresses
# #
# #         if presses >= minPresses:
# #             return
# #
# #         # Skip all the already covered cells
# #         while idx < len(cells) and curGrid[cells[idx][0]][cells[idx][1]] == 0:
# #             idx += 1
# #
# #         if idx == len(cells):
# #             minPresses = min(minPresses, presses)
# #             return
# #
# #         y, x = cells[idx]
# #
# #         canPlace = True
# #         for dy in range(M):
# #             for dx in range(M):
# #                 ny, nx = y + dy, x + dx
# #                 if ny >= h or nx >= w or curGrid[ny][nx] == 0:
# #                     canPlace = False
# #                     break
# #             if not canPlace:
# #                 break
# #
# #         if canPlace:
# #             # Copy the current grid
# #             newGrid = [row[:] for row in curGrid]
# #
# #             # Mark cells as covered
# #             for dy in range(M):
# #                 for dx in range(M):
# #                     ny, nx = y + dy, x + dx
# #                     if ny < h and nx < w:
# #                         newGrid[ny][nx] = 0
# #
# #             backtrack(idx + 1, newGrid, presses + 1)
# #
# #     # Start backtracking from the first uncovered cell
# #     backtrack(0, grid, 0)
# #
# #     print(minPresses)
# #
# #
# # # Run the function
# # calculate_min_presses()
# # import sys
# #
# #
# # def isInside(x, y, verts):
# #     cross = 0
# #     N = len(verts)
# #     for i in range(N):
# #         x1, y1 = verts[i]
# #         x2, y2 = verts[(i + 1) % N]
# #         if (y1 <= y and y2 > y) or (y2 <= y and y1 > y):
# #             ix = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
# #             if ix > x:
# #                 cross += 1
# #     return cross % 2 != 0
# #
# #
# # def calculate_min_presses():
# #     N = int(input())
# #     verts = [tuple(map(int, input().split())) for _ in range(N)]
# #
# #     M = int(input())
# #
# #     minX = min(v[0] for v in verts)
# #     maxX = max(v[0] for v in verts)
# #     minY = min(v[1] for v in verts)
# #     maxY = max(v[1] for v in verts)
# #
# #     w = maxX - minX + 1
# #     h = maxY - minY + 1
# #
# #     grid = [[0] * w for _ in range(h)]
# #
# #     # Fill grid with 1's where the points are inside the polygon
# #     for y in range(minY, maxY):
# #         for x in range(minX, maxX):
# #             if isInside(x + 0.5, y + 0.5, verts):
# #                 grid[y - minY][x - minX] = 1
# #
# #     # Gather all the cells that are inside the polygon
# #     cells = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == 1]
# #
# #     # Sort cells by row and column
# #     cells.sort()
# #
# #     minPresses = sys.maxsize
# #
# #     def backtrack(idx, curGrid, presses):
# #         nonlocal minPresses
# #
# #         if presses >= minPresses:
# #             return
# #
# #         # Skip all the already covered cells
# #         while idx < len(cells) and curGrid[cells[idx][0]][cells[idx][1]] == 0:
# #             idx += 1
# #
# #         if idx == len(cells):
# #             minPresses = min(minPresses, presses)
# #             return
# #
# #         y, x = cells[idx]
# #
# #         canPlace = True
# #         for dy in range(M):
# #             for dx in range(M):
# #                 ny, nx = y + dy, x + dx
# #                 if ny >= h or nx >= w or curGrid[ny][nx] == 0:
# #                     canPlace = False
# #                     break
# #             if not canPlace:
# #                 break
# #
# #         if canPlace:
# #             # Copy the current grid
# #             newGrid = [row[:] for row in curGrid]
# #
# #             # Mark cells as covered
# #             for dy in range(M):
# #                 for dx in range(M):
# #                     ny, nx = y + dy, x + dx
# #                     if ny < h and nx < w:
# #                         newGrid[ny][nx] = 0
# #
# #             backtrack(idx + 1, newGrid, presses + 1)
# #
# #     # Start backtracking from the first uncovered cell
# #     backtrack(0, grid, 0)
# #
# #     print(minPresses)
# #
# #
# # # Run the function
# # calculate_min_presses()
# import sys
#
#
# def isInside(x, y, verts):
#     cross = 0
#     N = len(verts)
#     for i in range(N):
#         x1, y1 = verts[i]
#         x2, y2 = verts[(i + 1) % N]
#         if (y1 <= y and y2 > y) or (y2 <= y and y1 > y):
#             ix = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
#             if ix > x:
#                 cross += 1
#     return cross % 2 != 0
#
#
# def calculate_min_presses():
#     N = int(input())
#     verts = [tuple(map(int, input().split())) for _ in range(N)]
#
#     M = int(input())
#
#     minX = min(v[0] for v in verts)
#     maxX = max(v[0] for v in verts)
#     minY = min(v[1] for v in verts)
#     maxY = max(v[1] for v in verts)
#
#     w = maxX - minX + 1
#     h = maxY - minY + 1
#
#     grid = [[0] * w for _ in range(h)]
#
#     # Fill grid with 1's where the points are inside the polygon
#     for y in range(minY, maxY):
#         for x in range(minX, maxX):
#             if isInside(x + 0.5, y + 0.5, verts):
#                 grid[y - minY][x - minX] = 1
#
#     # Gather all the cells that are inside the polygon
#     cells = [(i, j) for i in range(h) for j in range(w) if grid[i][j] == 1]
#
#     # Sort cells by row and column
#     cells.sort()
#
#     minPresses = sys.maxsize
#
#     def backtrack(idx, curGrid, presses):
#         nonlocal minPresses
#
#         if presses >= minPresses:
#             return
#
#         # Skip all the already covered cells
#         while idx < len(cells) and curGrid[cells[idx][0]][cells[idx][1]] == 0:
#             idx += 1
#
#         if idx == len(cells):
#             minPresses = min(minPresses, presses)
#             return
#
#         y, x = cells[idx]
#
#         canPlace = True
#         for dy in range(M):
#             for dx in range(M):
#                 ny, nx = y + dy, x + dx
#                 if ny >= h or nx >= w or curGrid[ny][nx] == 0:
#                     canPlace = False
#                     break
#             if not canPlace:
#                 break
#
#         if canPlace:
#             # Copy the current grid
#             newGrid = [row[:] for row in curGrid]
#
#             # Mark cells as covered
#             for dy in range(M):
#                 for dx in range(M):
#                     ny, nx = y + dy, x + dx
#                     if ny < h and nx < w:
#                         newGrid[ny][nx] = 0
#
#             backtrack(idx + 1, newGrid, presses + 1)
#
#     # Start backtracking from the first uncovered cell
#     backtrack(0, grid, 0)
#
#     print(minPresses)
#
#
# # Run the function
# calculate_min_presses()

import sys
from functools import lru_cache

def is_inside(x, y, verts):
    cross = 0
    N = len(verts)
    for i in range(N):
        x1, y1 = verts[i]
        x2, y2 = verts[(i + 1) % N]
        if ((y1 <= y) and (y2 > y)) or ((y2 <= y) and (y1 > y)):
            ix = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if ix > x:
                cross += 1
    return cross % 2 != 0

def main():
    N = int(input())
    verts = []
    minX, maxX, minY, maxY = sys.maxsize, -sys.maxsize, sys.maxsize, -sys.maxsize

    for _ in range(N):
        x, y = map(int, input().split())
        verts.append((x, y))
        minX = min(minX, x)
        maxX = max(maxX, x)
        minY = min(minY, y)
        maxY = max(maxY, y)

    M = int(input())

    w = maxX - minX + 1
    h = maxY - minY + 1
    grid = [[0] * w for _ in range(h)]

    for y in range(minY, maxY):
        for x in range(minX, maxX):
            if is_inside(x + 0.5, y + 0.5, verts):
                grid[y - minY][x - minX] = 1

    cells = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 1:
                cells.append((i, j))

    cells.sort()

    minPresses = sys.maxsize

    @lru_cache(None)
    def backtrack(idx, curGrid, presses):
        nonlocal minPresses
        if presses >= minPresses:
            return
        while idx < len(cells) and curGrid[cells[idx][0]][cells[idx][1]] == 0:
            idx += 1
        if idx == len(cells):
            minPresses = min(minPresses, presses)
            return
        y, x = cells[idx]
        canPlace = True
        for dy in range(M):
            for dx in range(M):
                ny, nx = y + dy, x + dx
                if ny >= h or nx >= w or curGrid[ny][nx] == 0:
                    canPlace = False
                    break
            if not canPlace:
                break
        if canPlace:
            newGrid = [row[:] for row in curGrid]
            for dy in range(M):
                for dx in range(M):
                    ny, nx = y + dy, x + dx
                    if ny < h and nx < w:
                        newGrid[ny][nx] = 0
            backtrack(idx + 1, tuple(map(tuple, newGrid)), presses + 1)

    backtrack(0, tuple(map(tuple, grid)), 0)

    print(minPresses)

if __name__ == "__main__":
    main()
