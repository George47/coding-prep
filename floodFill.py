def numIslands(grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def DFS(row, col, grid):
            if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] != '1':
                return
            else:
                grid[row][col] = '0'
            DFS(row + 1, col, grid)
            DFS(row - 1, col, grid)
            DFS(row, col + 1, grid)
            DFS(row, col - 1, grid)
            
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    islands += 1
                    DFS(row, col, grid)
        return islands

def maxAreaOfIsland(grid: List[List[int]]) -> int:
        def dfs(row, col, grid):
            if row < 0 or col < 0 or row == len(grid) or col == len(grid[0]) or grid[row][col] != 1:
                return 0
            else:
                grid[row][col] = 0
                return 1 + dfs(row+1, col, grid) + dfs(row-1, col, grid) + dfs(row, col+1, grid) + dfs(row, col-1, grid)

        maxIsland = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    maxIsland = max(dfs(row, col, grid), maxIsland)
        return maxIsland