class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        reversed_number = sign * int(str(abs(x))[::-1])

        if -(2**31) <= reversed_number <= 2**31 - 1:
            return reversed_number
        return 0


if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse(5230))
