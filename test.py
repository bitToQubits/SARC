class Solution:
    def totalPower(self, nums):
        nums.sort()
        mod = 10**9 + 7
        res = 0
        prefix = 0
        for num in nums:
            res = (res + num * num % mod * (prefix + num)) % mod
            prefix = (2 * prefix + num) % mod
        return res
        
if __name__ == "__main__":
    
    solution = Solution()
    print(solution.totalPower(nums=[2,1,4]))