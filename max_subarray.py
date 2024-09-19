# max_subarray
# Given an array arr[], the task is to find the subarray that has the maximum sum and return its sum.

# Examples:

# Input: arr[] = {2, 3, -8, 7, -1, 2, 3}
# Output: 11
# Explanation: The subarray {7, -1, 2, 3} has the largest sum 11.

# Input: arr[] = {-2, -4}
# Output: –2
# Explanation: The subarray {-2} has the largest sum -2.

# Input: arr[] = {5, 4, 1, 7, 8}
# Output: 25
# Explanation: The subarray {5, 4, 1, 7, 8} has the largest sum 25.

cases = int(input())

def find_max_subarray(arr):
    # Naive approach explore all possible array sizes time probably O(n!) perhaps a sliding window opperation 
    #   where we increment the size of the window from 1 to len(arr)
    # pass

    # Kody's Approach
    # what if we kept track of a total sum as we traverse the array then if ever that sum
    # goes negative then we store the total as a max then continue down the array.
    # maximum = arr[0]
    # total = 0
    # search_i = 0
    # start_i = 0
    # end_i = 0
    # for i, val in enumerate(arr):
    #     if total + val > maximum:
    #         maximum = total + val
    #         start_i = search_i
    #         end_i = i
    #     if val+total < 0 and val < 0:
    #         total = 0
    #         search_i = i+1
    #     else:
    #         total = val + total
    # return start_i, end_i, maximum

    # Kadane's algorithm approach
    res = arr[0]
    maxEnding = arr[0]
    for i in range(1, len(arr)):
        
        # Find the maximum sum ending at index i by either extending 
        # the maximum sum subarray ending at index i - 1 or by
        # starting a new subarray from index i
        maxEnding = max(maxEnding + arr[i], arr[i])
        
        # Update res if maximum subarray sum ending at index i > res
        res = max(res, maxEnding)
    
    return 0,0,res

            
    


for c in range(cases):
    arr = list(map(int, input().split(', ')))
    start, end, maximum = find_max_subarray(arr)
    print(arr[start:end+1])
    print(maximum)