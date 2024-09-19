# Given an unsorted array arr[]. Rotate the array to the left (counter-clockwise direction) by d steps,
#  where d is a positive integer. Do the mentioned change in the array in place.

# Note: Consider the array as circular.

# Examples :

# Input: arr[] = {1,2,3,4,5}, d = 2
# Output: 3 4 5 1 2
# Explanation: 1 2 3 4 5  when rotated by 2 elements, it becomes 3 4 5 1 2.
# Input: arr[] = {2,4,6,8,10,12,14,16,18,20}, d = 3
# Output: 8 10 12 14 16 18 20 2 4 6
# Explanation: 2 4 6 8 10 12 14 16 18 20 when rotated by 3 elements, it becomes 8 10 12 14 16 18 20 2 4 6.
# Expected Time Complexity: O(n)
# Expected Auxiliary Space: O(1)

# Constraints:
# 1 <= arr.size(),d <= 105
# 0 <= arr[i] <= 105

from collections import deque

def rotate_arr(arr, d):
    # first approach... to slow...
    # rot = d % len(arr)
    # for i in range(rot): arr.append(arr.pop(0))
    # return arr

    # Adjusted to make it faster not very clean.
    # rot = d % len(arr)
    # deq = deque(arr)
    # for i in range(rot): deq.append(deq.popleft())
    # for i in range(len(arr)): arr[i]=deq[i]
    # return deq

    # learned about the reverse function
    l = len(arr)
    d = d%l
    arr[0:d]  = reversed(arr[0:d])
    arr[d:l]  = reversed(arr[d:l])
    arr[0:l]  = reversed(arr[0:l])
    return arr


cases = int(input())
for c in range(cases):
    d = int(input())
    arr = list(map(int,input().split(',')))
    result = rotate_arr(arr,d)
    print(result)
