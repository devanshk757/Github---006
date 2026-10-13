class Solution:
    def sumOfGoodIntegers(self, n: int, k: int) -> int:
        i = max(n - k, 1)
        sum = 0
        while i <= n+k :
            if (n & i) == 0:
                sum += i
            i += 1

        return sum