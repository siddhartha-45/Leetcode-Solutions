class Solution(object):
    def checkSubarraySum(self, nums, k):
        sum = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i - 1] == 0 and nums[i] == 0:
                return True
            sum += nums[i]
            if sum % k == 0:
                return True
            
            j = 0
            temp_sum = sum
            
            while (i - j) > 1 and temp_sum >= k:
                temp_sum -= nums[j]
                j += 1
                if temp_sum % k == 0:  
                    return True
        return False