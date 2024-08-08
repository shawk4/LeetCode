class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # dual pointer approach
        k = 0
        for num in nums:
            if num != nums[k]:
                k += 1
                nums[k] = num
        print(nums)
        return k+1
        

def main():
    solution = Solution()     
# case 1
    nums = [0,0,1,1,1,2,2,3,3,4]
# case 2
    # nums = [1,1,2]
    k = solution.removeDuplicates(nums)
    print(k)
    
    
if __name__ == '__main__':
    main()