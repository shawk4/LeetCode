# buy_and_sell
# Given an array prices[] of length N, representing the prices of the stocks on different days,
#  the task is to find the maximum profit possible by buying and selling the stocks on different days
#  when at most one transaction is allowed. Here one transaction means 1 buy + 1 Sell.

# Note: Stock must be bought before being sold.

# Examples:

# Input: prices[] = {7, 10, 1, 3, 6, 9, 2}
# Output: 8
# Explanation: Buy for price 1 and sell for price 9.

# Input: prices[] = {7, 6, 4, 3, 1} 
# Output: 0
# Explanation: Since the array is sorted in decreasing order, 0 profit can be made without making any transaction.

# Input: prices[] = {1, 3, 6, 9, 11} 
# Output: 10
# Explanation: Since the array is sorted in increasing order, we can make maximum profit by buying at price[0] and selling at price[n-1]

cases = int(input())

def best_buy_sell_times(arr):
    # Naive approach nested loop to check all possibles
    # Kody's approach find min and check all later dates for max if max is < min then profit is 0
    min_index = min(range(len(arr)),key=arr.__getitem__) 
    max_remaining = max(arr[min_index:])
    print(f"min_index: {min_index}")
    print(f"max remaining: {max_remaining}")
    if arr[min_index] >= max_remaining:
        return 0
    else:
        return max_remaining - arr[min_index]
    

for c in range(cases):
    arr = list(map(int,input().split(', ')))
    output = best_buy_sell_times(arr)
    print(output)