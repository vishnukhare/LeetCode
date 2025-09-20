class Solution:
    def calculateScore(self, s: str) -> int:
        res = 0
        hashmap = defaultdict(list)

        
        for i, ch in enumerate(s):
            curr = ord(ch) - ord('a')
            mirror = 25 - curr
            if hashmap[mirror]:
                res += i - hashmap[mirror].pop()
            else:
                hashmap[curr].append(i)

        return res


        