# from collections import deque
#
#
# def bfs(start, destination, N, M, board):
#     # Directions for moving in the grid
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # up, down, left, right
#
#     # Initialize BFS queue with start position and initial move count
#     queue = deque([(start[0], start[1], 0)])  # (row, col, move count)
#     visited = [[False] * M for _ in range(N)]
#     visited[start[0]][start[1]] = True
#
#     while queue:
#         r, c, moves = queue.popleft()
#
#         # If we reached the destination, return the move count
#         if (r, c) == destination:
#             return moves
#
#         # Try to move in all 4 possible directions
#         for dr, dc in directions:
#             nr, nc = r + dr, c + dc
#
#             # Check if the new position is within bounds
#             if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
#                 # The destination cell must be empty or contain a lift, not unstable
#                 if board[nr][nc] != 1 and board[nr][nc] != 0:
#                     continue
#                 visited[nr][nc] = True
#                 queue.append((nr, nc, moves + 1))
#
#     # If we exhaust the queue without finding the destination
#     return -1  # Impossible
#
#
# def main():
#     # Read inputs
#     N, M = map(int, input().split())
#     board = [list(map(int, input().split())) for _ in range(N)]
#     start = tuple(map(int, input().split()))
#     destination = tuple(map(int, input().split()))
#
#     # We use BFS to find the shortest path.
#     result = bfs(start, destination, N, M, board)
#
#     if result == -1:
#         print("Impossible")
#     else:
#         print(result)
#
#
# if __name__ == "__main__":
#     main()
# from collections import deque
#
# def is_stable(x, y, grid, N):
#     # A cell is stable if it has a lift directly below it or it's the last row
#     if x == N - 1:  # Last row is always stable
#         return True
#     return grid[x + 1][y] == 1  # Stable if there's a lift directly below
#
# def bfs(grid, start, end, N, M):
#     # Directions: up, down, left, right
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     queue = deque([(start[0], start[1], 0)])  # (x, y, steps)
#     visited = set()
#     visited.add((start[0], start[1]))
#
#     while queue:
#         x, y, steps = queue.popleft()
#
#         # If we've reached the destination, return the number of steps
#         if (x, y) == end:
#             return steps
#
#         # Handle sliding down if the current cell is empty and unstable
#         if grid[x][y] == 0 and not is_stable(x, y, grid, N):
#             # Slide down until reaching a stable cell
#             while x + 1 < N and grid[x + 1][y] == 0 and not is_stable(x + 1, y, grid, N):
#                 x += 1
#             # After sliding down, we treat the cell as stable
#             if (x, y) not in visited:
#                 visited.add((x, y))
#                 queue.append((x, y, steps + 1))
#
#         # Try moving in all four directions (up, down, left, right)
#         for dx, dy in directions:
#             nx, ny = x + dx, y + dy
#
#             # Check boundaries and if the cell is not visited
#             if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited:
#                 # We can move to a lift or a stable empty cell
#                 if grid[nx][ny] == 0 and is_stable(nx, ny, grid, N):
#                     visited.add((nx, ny))
#                     queue.append((nx, ny, steps + 1))
#                 elif grid[nx][ny] == 1:
#                     visited.add((nx, ny))
#                     queue.append((nx, ny, steps + 1))
#
#     return "Impossible"  # If no valid path was found
#
# # Read input
# N, M = map(int, input().strip().split())
# grid = []
# for _ in range(N):
#     grid.append(list(map(int, input().strip().split())))
#
# start = tuple(map(int, input().strip().split()))
# end = tuple(map(int, input().strip().split()))
#
# # Compute the minimum number of steps
# result = bfs(grid, start, end, N, M)
# print(result)
#
# from collections import deque
#
# def is_stable(x, y, grid, N):
#     """
#     A cell is stable if it is in the last row or if there is a lift directly below it.
#     """
#     if x == N - 1:  # Last row is always stable
#         return True
#     return grid[x + 1][y] == 1  # Stable if there's a lift directly below
#
# def bfs(grid, start, end, N, M):
#     # Directions for movement: up, down, left, right
#     directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     queue = deque([(start[0], start[1], 0)])  # (x, y, steps)
#     visited = set()
#     visited.add((start[0], start[1]))
#
#     while queue:
#         x, y, steps = queue.popleft()
#
#         # If we've reached the destination, return the number of steps
#         if (x, y) == end:
#             return steps
#
#         # Handle sliding down if the current cell is empty and unstable
#         if grid[x][y] == 0 and not is_stable(x, y, grid, N):
#             # Slide down until reaching a stable cell
#             while x + 1 < N and grid[x + 1][y] == 0 and not is_stable(x + 1, y, grid, N):
#                 x += 1
#             # After sliding down, we treat the cell as stable
#             if (x, y) not in visited:
#                 visited.add((x, y))
#                 queue.append((x, y, steps + 1))
#
#         # Try moving in all four directions (up, down, left, right)
#         for dx, dy in directions:
#             nx, ny = x + dx, y + dy
#
#             # Check boundaries and if the cell is not visited
#             if 0 <= nx < N and 0 <= ny < M and (nx, ny) not in visited:
#                 # Move to an empty cell if it is stable, or to a lift cell
#                 if grid[nx][ny] == 0 and is_stable(nx, ny, grid, N):
#                     visited.add((nx, ny))
#                     queue.append((nx, ny, steps + 1))
#                 elif grid[nx][ny] == 1:  # If it's a lift, we can move there
#                     visited.add((nx, ny))
#                     queue.append((nx, ny, steps + 1))
#
#     return "Impossible"  # If no valid path was found
#
# # Read input
# N, M = map(int, input().strip().split())
# grid = []
# for _ in range(N):
#     grid.append(list(map(int, input().strip().split())))
#
# start = tuple(map(int, input().strip().split()))
# end = tuple(map(int, input().strip().split()))
#
# # Compute the minimum number of steps
# result = bfs(grid, start, end, N, M)
# print(result)

# from collections import deque
#
#
# def stable(x, y, mat, n):
#     if x == n - 1:
#         return True
#     return mat[x + 1][y] == 1
#
#
# def bfs(mat, start, end, n, m):
#     steps_direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     queue = deque([(start[0], start[1], 0)])
#     vsi = set()
#     vsi.add((start[0], start[1]))
#
#     while queue:
#         x, y, steps = queue.popleft()
#         if (x, y) == end:
#             return steps
#         if mat[x][y] == 0 and not stable(x, y, mat, n):
#             while x + 1 < n and mat[x + 1][y] == 0 and not stable(x + 1, y, mat, n):
#                 if (x, y) not in vsi:
#                     vsi.add((x, y))
#                     queue.append((x, y, steps + 1))
#         for dx, dy in steps_direction:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in vsi:
#                 if mat[nx][ny] == 0 and stable(nx, ny, mat, n):
#                     vsi.add((nx, ny))
#                     queue.append((nx, ny, steps + 1))
#                 elif mat[nx][ny] == 1:
#                     vsi.add((nx, ny))
#                     queue.append((nx, ny, steps + 1))
#     return "Impossible"
#
#
# def main():
#     n, m = [int(s) for s in input().strip().split()]
#     mat = []
#     for _ in range(n):
#         mat.append([int(s) for s in input().split()])
#     start = tuple([int(x) for x in input().split()])
#     end = tuple([int(x) for x in input().split()])
#
#     ans = bfs(mat, start, end, n, m)
#     return ans

#
# from collections import deque
#
#
# def istable(x, y, mat, n):
#     if x == n - 1:
#         return True
#     return mat[x + 1][y] == 1
#
#
# def bfs(mat, start, end, n, m):
#     steps_direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     queue = deque([(start[0], start[1], 0)])
#     vsi = set()
#     vsi.add((start[0], start[1]))
#
#     while queue:
#         x, y, steps = queue.popleft()
#         if (x, y) == end:
#             return steps
#         if mat[x][y] == 0 and not istable(x, y, mat, n):
#             while x + 1 < n and mat[x + 1][y] == 0 and not istable(x + 1, y, mat, n):
#                 x += 1
#             if (x, y) not in vsi:
#                 vsi.add((x, y))
#                 queue.append((x, y, steps + 1))
#         for dx, dy in steps_direction:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in vsi:
#                 if mat[nx][ny] == 0 and istable(nx, ny, mat, n):
#                     vsi.add((nx, ny))
#                     queue.append((nx, ny, steps + 1))
#                 elif mat[nx][ny] == 1:
#                     vsi.add((nx, ny))
#                     queue.append((nx, ny, steps + 1))
#     return "Impossible"
#
#
# def main():
#     n, m = [int(s) for s in input().split()]
#     mat = []
#     for _ in range(n):
#         mat.append([int(s) for s in input().split()])
#     start = tuple([int(x) for x in input().split()])
#     end = tuple([int(x) for x in input().split()])
#
#     ans = bfs(mat, start, end, n, m)
#     return ans
#
#
# if __name__ == "__main__":
#     print(main(), end="")

# //mmm
# from collections import deque
#
#
# # Check if a cell is stable or has a lift below it
# def istable(x, y, mat, n):
#     if x == n - 1:  # Last row is always stable
#         return True
#     return mat[x + 1][y] == 1  # Check if there's a lift below
#
#
# # BFS function to calculate minimum steps
# def bfs(mat, start, end, n, m):
#     steps_direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     queue = deque([(start[0], start[1], 0)])  # (x, y, steps)
#     vsi = set()  # Visited set to avoid revisiting cells
#     vsi.add((start[0], start[1]))
#
#     while queue:
#         x, y, steps = queue.popleft()
#
#         # If the current position is the destination
#         if (x, y) == end:
#             return steps
#
#         # If the current cell is empty and unstable (no lift below), simulate gravity
#         if mat[x][y] == 0 and not istable(x, y, mat, n):
#             # Let the block fall down until it reaches a stable position
#             while x + 1 < n and mat[x + 1][y] == 0 and not istable(x + 1, y, mat, n):
#                 x += 1
#             if (x, y) not in vsi:
#                 vsi.add((x, y))
#                 queue.append((x, y, steps + 1))
#
#         # Explore 4 possible directions (up, down, left, right)
#         for dx, dy in steps_direction:
#             nx, ny = x + dx, y + dy
#             if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in vsi:
#                 if mat[nx][ny] == 0 and istable(nx, ny, mat, n):  # Move only to stable empty cells
#                     vsi.add((nx, ny))
#                     queue.append((nx, ny, steps + 1))
#                 elif mat[nx][ny] == 1:  # Move to a lift cell
#                     vsi.add((nx, ny))
#                     queue.append((nx, ny, steps + 1))
#
#     return "Impossible"  # If no path to destination exists
#
#
# # Main function to handle input and output
# def main():
#     n, m = map(int, input().split())  # Read grid dimensions
#     mat = [list(map(int, input().split())) for _ in range(n)]  # Read the grid
#
#     start = tuple(map(int, input().split()))  # Starting position
#     end = tuple(map(int, input().split()))  # Destination position
#
#     # Call the bfs function to calculate the minimum steps
#     result = bfs(mat, start, end, n, m)
#     print(result)
#
#
# if __name__ == "__main__":
#     main()

from collections import deque


# Check if a cell is stable or has a lift below it
def istable(x, y, mat, n):
    if x == n - 1:  # Last row is always stable
        return True
    return mat[x + 1][y] == 1  # Check if there's a lift below


# BFS function to calculate minimum steps
def bfs(mat, start, end, n, m):
    steps_direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start[0], start[1], 0)])  # (x, y, steps)
    vsi = set()  # Visited set to avoid revisiting cells
    vsi.add((start[0], start[1]))

    while queue:
        x, y, steps = queue.popleft()

        # If the current position is the destination
        if (x, y) == end:
            return steps

        # If the current cell is empty and unstable (no lift below), simulate gravity
        if mat[x][y] == 0 and not istable(x, y, mat, n):
            # Let the block fall down until it reaches a stable position
            while x + 1 < n and mat[x + 1][y] == 0 and not istable(x + 1, y, mat, n):
                x += 1
            if (x, y) not in vsi:  # Add only if new position
                vsi.add((x, y))
                queue.append((x, y, steps + 1))  # Count the fall as one move

        # Explore 4 possible directions (up, down, left, right)
        for dx, dy in steps_direction:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and (nx, ny) not in vsi:
                if mat[nx][ny] == 0 and istable(nx, ny, mat, n):  # Move only to stable empty cells
                    vsi.add((nx, ny))
                    queue.append((nx, ny, steps + 1))
                elif mat[nx][ny] == 1:  # Move to a lift cell
                    vsi.add((nx, ny))
                    queue.append((nx, ny, steps + 1))

    return "Impossible"  # If no path to destination exists


# Main function to handle input and output
def main():
    n, m = map(int, input().split())  # Read grid dimensions
    mat = [list(map(int, input().split())) for _ in range(n)]  # Read the grid

    start = tuple(map(int, input().split()))  # Starting position
    end = tuple(map(int, input().split()))  # Destination position

    # Call the bfs function to calculate the minimum steps
    result = bfs(mat, start, end, n, m)
    print(result)


if __name__ == "__main__":
    main()
