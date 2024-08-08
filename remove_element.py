# remove_element
# remove specific integers and count remaing integers in list
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # nums.remove(val) # only removes 1
        # k = len(list(filter(lambda a: a != val, nums))) # does not play nice with leet 
        
    # for loop method
        # size = len(nums)
        # rem = [0] * size
        # k = 0
        # for i, num in enumerate(nums):
        #     if num == val:
        #         rem[i] = 1
        #         nums[size] = nums[i]
        #         nums[i] = nums[i+1]
        #     else:
        #         k+=1
        # for i, bol in enumerate(rem):
        #     j = size - i
        #     if bol:
        #         del nums[size]
        
        # # While loop method
        #     check = True
        #     while check:
        #         if val in nums:
        #             nums.remove(val)
        #         else:
        #             check = False
        # k = len(nums)
    
        # double pointer method
        k = 0
        for num in nums:
            if num != val:
                nums[k] = num
                k += 1

        print(nums)
        return k
        
def main():
    solution = Solution()     
# case 1
    nums = [1,9,2,9,3,4,5,6,7,8,9,9,9,9]
    val = 9
    k = solution.removeElement(nums, val)
    print(k)
    
    
if __name__ == '__main__':
    main()