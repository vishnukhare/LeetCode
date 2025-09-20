class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        def dfs(r, c, k):
            
            if k == len(word):
                return True
            
            if not (0 <= r < m and 0 <= c < n and board[r][c] == word[k]):
                return False

            original_char = board[r][c]
            board[r][c] = '#'

            found = (dfs(r + 1, c, k + 1) or
                     dfs(r - 1, c, k + 1) or
                     dfs(r, c + 1, k + 1) or
                     dfs(r, c - 1, k + 1))

            board[r][c] = original_char
            
            return found

        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True
        
        return False