class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums1=set(nums)
        nums2=list(nums1)
        if len(nums)==len(nums2):
            return False
        else:
            return True
            
        