# Given an array arr[] of n integers and a target value, the task is to find whether there is a pair
# of elements in the array whose sum is equal to target. This problem is a variation of 2 Sum problem.

# Examples: 

# Input: arr[] = {0, -1, 2, -3, 1}, target = -2
# Output: True
# Explanation: If we calculate the sum of the output,1 + (-3) = -2

# Input: arr[] = {1, -2, 1, 0, 5}, target = 0
# Output: False


def pair_with_given_sum(target, arr):
    # Naive approach nested loop O(n^2)
    # length = len(arr)
    # for i in range(length):
    #     for j in range(length):
    #         if i == j:
    #                 pass
    #         elif arr[i] + arr[j] == target:
    #             return True
    # return False

    # A second approach loop through the list and subtract the target from each number, a complement, 
    # then use a hashing algorithm, for its fast lookup, to see if a complement exists. O(n)
    length = len(arr)

    d = dict()
    for i in range(length):
        if d.get(str(arr[i])) == None:
            d[str(target-arr[i])] = target-arr[i]
        else:
            return True
    return False


                

cases = int(input())
for c in range(cases):
    target = int(input())
    arr = list(map(int, input().split(',')))
    output = pair_with_given_sum(target, arr)
    print(output)
                
    
    