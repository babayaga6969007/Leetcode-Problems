class Solution(object):
    def runningSum(self):
        nums = input("Enter space-separated integers: ").split()
        nums = [int(num) for num in nums]
        
        running_sum = 0
        result = []
        for num in nums:
            running_sum += num
            result.append(running_sum)
        return result
sol = Solution()

result = sol.runningSum()
print("Running sum:", result)
