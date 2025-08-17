class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = [0] * (n+1)
        for i in range(0, n+1):
            if i == 0:
                continue
            else:
                if i % 3 == 0 and i % 5 == 0:
                    res[i] = 'FizzBuzz'
                elif i % 3 == 0:
                    res[i] = 'Fizz'
                elif i % 5 == 0:
                    res[i] = 'Buzz'
                else:
                    res[i] = str(i)

        return res[1:]