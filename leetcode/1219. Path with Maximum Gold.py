class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(i, j, value):
            seen.add((i, j))
            dp[i][i] = max(dp[i][j], value)
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n and grid[x][y] and (x, y) not in seen:
                    dfs(x, y, value + grid[x][y])
            seen.discard((i, j))
            return dp[i][j]

        m, n = len(grid), len(grid[0])
        seen = set()
        dp = [[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    dfs(i, j, grid[i][j])
        return max(c for row in dp for c in row)
        