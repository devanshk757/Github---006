class Solution:
    def reverseString(self, s: list[str]) -> None:
        left = 0

        for right in range(len(s) - 1, -1, -1):
            if left < right:
                s[left], s[right] = s[right], s[left]
            else:
                break
            left += 1
            right -= 1
        
        return s

        