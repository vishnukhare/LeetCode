class Solution:
    def calculateScore(self, s: str) -> int:
        def mirror(c):
            return chr(ord('z') - (ord(c) - ord('a')))
        
        from collections import defaultdict
        stacks = defaultdict(list)  
        score = 0
        
        for i, ch in enumerate(s):
            m = mirror(ch)
            if stacks[m]:  
                j = stacks[m].pop()
                score += i - j
            else:
                stacks[ch].append(i)
        
        return score
