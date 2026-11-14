class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i + 1, len(nums)):
        #         if i!=j and nums[i]+nums[j]==target:
        #             return [i,j]

        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in nums:
                j=nums.index(diff)
                if i!=j:
                    return [min(i, j), max(i, j)]