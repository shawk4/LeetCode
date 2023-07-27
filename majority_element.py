# majority element 
#  given a list of numbers return the number that fills more than half the list. assume this will always happen
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # running total approach
        counter =  0
        majority_num = nums[0]
        for num in nums:
            if majority_num == num:
                counter += 1
            else:
                counter -=1
            if counter == 0:
                majority_num = num
                counter +=1
        return majority_num
            


def main():
    sol = Solution()
    nums1 = [3,1,3]
    nums2 = [2,2,1,1,1,2,2]
    nums3 = [2,-1,2,-1,1,-1,1,-1,1,-1,2,-1,2,-1,-1]
    nums4 = [9,9,9,9,1,2,2]
    nums5 = [0,0,0,1,1,0,2,2,0]
    lists = [nums1,nums2, nums3, nums4, nums5]
    for nums in lists:
        temp = sol.majorityElement(nums)
        print(temp)
if __name__ == "__main__":
    main()


