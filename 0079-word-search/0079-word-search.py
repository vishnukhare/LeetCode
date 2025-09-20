class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        visited = set()

        def find_word(idx, r, c):
            if idx == len(word):
                return True
            
            if (
                (r < 0 or r >=  rows)
                or (c < 0 or c >= cols) 
                or (word[idx] != board[r][c]) 
                or (r, c) in visited
            ):
                return False

            visited.add((r, c))

            res = (
                find_word(idx+1, r+1, c) or
                find_word(idx+1, r, c+1) or
                find_word(idx+1, r-1, c) or
                find_word(idx+1, r, c-1)
            )

            visited.remove((r, c))

            return res
        
        count = {}
        for c in word:
            count[c] = 1 + count.get(c, 0)
        
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]
        
        for r in range(rows):
            for c in range(cols):
                if find_word(0, r, c):
                    return True

        return False