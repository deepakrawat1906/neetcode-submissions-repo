class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        l = 0
        r = len(nums)-1

        while l<=r:
            m  = (l+r)//2

            if target==nums[m]:
                return True
            
            if nums[m]>nums[l]:
                if target>=nums[l] and target<nums[m]:
                    r = m-1
                else:
                    l = m+1
            elif nums[l]>nums[m]:
                if target>nums[m] and target<=nums[r]:
                    l=m+1
                else:
                    r=m-1
            else:
                l+=1
        return False
        