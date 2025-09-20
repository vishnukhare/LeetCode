import collections

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        dp = [0] * (n + 1)
        dp[1] = 1

        total_people_aware = 1

        for i in range(2, n + 1):
            new_people_sharing_today = 0

            start_day_to_sum = max(1, i - forget + 1)
            end_day_to_sum = i - delay

            for j in range(start_day_to_sum, end_day_to_sum + 1):
                new_people_sharing_today = (new_people_sharing_today + dp[j]) % MOD
            
            dp[i] = new_people_sharing_today

            total_people_aware = (total_people_aware + dp[i]) % MOD

            if i > forget:
                total_people_aware = (total_people_aware - dp[i - forget] + MOD) % MOD
                
        return total_people_aware