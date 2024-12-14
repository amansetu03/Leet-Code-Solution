#
#
# from collections import defaultdict
#
#
# def find_connected_blocks(grid, N, M):
#     blocks = defaultdict(set)
#     visited = set()
#
#     def dfs(i, j, block_num):
#         if (i, j) in visited or i < 0 or i >= N or j < 0 or j >= M or grid[i][j] != block_num:
#             return
#
#         visited.add((i, j))
#         blocks[block_num].add((i, j))
#
#         for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
#             dfs(ni, nj, block_num)
#
#     for i in range(N):
#         for j in range(M):
#             if (i, j) not in visited:
#                 dfs(i, j, grid[i][j])
#
#     return blocks
#
#
# def find_dependencies(blocks, N, M, target):
#     """
#     Find all blocks that need to be removed to reach target block
#     Returns the count of blocks to remove
#     """
#     block_tops = {}
#     for block_num, coords in blocks.items():
#         min_row = min(i for i, j in coords)
#         block_tops[block_num] = min_row
#
#     target_coords = blocks[target]
#     target_top = block_tops[target]
#     blocks_to_remove = set()
#
#     for block_num, coords in blocks.items():
#         if block_num == target:
#             continue
#
#         block_top = block_tops[block_num]
#
#         if block_top <= target_top:
#             target_columns = set(j for i, j in target_coords)
#             block_columns = set(j for i, j in coords)
#
#             if target_columns & block_columns:
#                 blocks_to_remove.add(block_num)
#
#     return len(blocks_to_remove)
#
#
# def solve_block_extraction():
#     N, M = map(int, input().split())
#
#     grid = []
#     for _ in range(N):
#         row = list(map(int, input().split()))
#         grid.append(row)
#
#     K = int(input())
#
#     blocks = find_connected_blocks(grid, N, M)
#
#     result = find_dependencies(blocks, N, M, K)
#     print(result)
#
#
# if __name__ == "__main__":
#     solve_block_extraction()
#

from collections import defaultdict

def find_connected_blocks(grid, N, M):
    """
    Find all connected blocks of the same color using DFS.
    """
    blocks = defaultdict(set)
    visited = set()

    def dfs(i, j, block_num):
        if (i, j) in visited or i < 0 or i >= N or j < 0 or j >= M or grid[i][j] != block_num:
            return

        visited.add((i, j))
        blocks[block_num].add((i, j))

        for ni, nj in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]:
            dfs(ni, nj, block_num)

    for i in range(N):
        for j in range(M):
            if (i, j) not in visited:
                dfs(i, j, grid[i][j])

    return blocks

def is_supported(grid, i, j, N, M, block_num):
    """
    Check if the block at (i, j) is supported by another block.
    A block is supported if there is another block of the same color below or beside it.
    """
    if i + 1 < N and grid[i + 1][j] == block_num:
        return True
    if j - 1 >= 0 and grid[i][j - 1] == block_num:
        return True
    return False

def find_dependencies(blocks, grid, N, M, target):
    """
    Find all blocks that need to be removed to reach the target block
    Returns the count of blocks to remove
    """
    blocks_to_remove = set()
    target_blocks = blocks[target]

    # Traverse each block to check for dependencies
    for block_num, coords in blocks.items():
        if block_num == target:
            continue

        # For each block, check if it is in the way of the target block
        for (i, j) in coords:
            if not is_supported(grid, i, j, N, M, block_num):
                blocks_to_remove.add(block_num)
                break

    return len(blocks_to_remove)

def solve_block_extraction():
    N, M = map(int, input().split())  # Rows and columns

    grid = []
    for _ in range(N):
        row = list(map(int, input().split()))
        grid.append(row)

    target_color = int(input())

    blocks = find_connected_blocks(grid, N, M)  # Find all blocks by color
    result = find_dependencies(blocks, grid, N, M, target_color)  # Count blocks to remove
    print(result)

if __name__ == "__main__":
    solve_block_extraction()

