class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        if n < 0:
            return False
        palidrone = []
        for i in range(len(str(n))):
            result = n % 10
            n = n // 10
            palidrone.append(result)
        reve = "".join([str(num) for num in palidrone])
        print(reve, x)
        if reve != str(x):
            return False
        else:
            return True

c = Solution()
print(c.isPalindrome(10))