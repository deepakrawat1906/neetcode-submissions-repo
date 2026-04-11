class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def rev(left,right):

            while left<right:
                tmp = nums[left]
                nums[left] = nums[right]
                nums[right] = tmp

                left+=1
                right-=1
        if len(nums)>1:
            n = len(nums)
            k = k%n
            if k == 0: 
                return
            rev(0,n-k-1)
            rev(n-k,n-1)
            rev(0,n-1)