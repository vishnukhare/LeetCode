class Solution:
    def calculateScore(self, s: str) -> int:
        res = 0
        hashmap = defaultdict(list)

        
        for i in range(len(s)):
            curr = ord(s[i]) - ord('a')
            mirror = 25 - curr
            if hashmap[mirror]:
                res += i - hashmap[mirror].pop()
            else:
                hashmap[curr].append(i)
        return res


        