# Given an array of non-negative integers and an integer sum. We have to tell whether there exists any subset in an array whose sum is equal to the given integer sum.

# Examples:

# Input: arr[] = {3, 34, 4, 12, 3, 2}, sum = 7
# Output: True
# Explanation: There is a subset (4, 3) with sum 7.

# Input: arr[] = {2, 2, 2, 3, 2, 2}, sum = 10
# Output: True

# Recursive approach


arr = [3,34,4,12,3,2]
target = 10
n = len(arr)


def recur(target,index):
    if target==0:
        return True
    if target<0 or index<=0:
        return False

    return recur(target-arr[index-1],index-1) or recur(target,index-1)
    
print(recur(target,n))

dp = [[-1]*(target+1) for i in range(n+1)]

def topDownApproach(target, index):
    if target==0: 
        return True
    if target<0 or index<=0:
        return False

    if dp[index][target]!=-1:
        return dp[index][target]
    
    dp[index][target] = topDownApproach(target-arr[index-1],index-1) or topDownApproach(target, index-1)
    return dp[index][target]

print(topDownApproach(target,n))

dp2 = [[-1]*(target+1) for i in range(n+1)]

def bottomUpApproach(target,n):
    for i in range(n+1):
        for j in range(target+1):
            if i==0:
                dp2[i][j] = False
            if j==0:
                dp2[i][j] = True
            if i>0 and j>0:
                if j<arr[i-1]:
                    dp2[i][j] = dp2[i-1][j]
                else:
                    dp2[i][j] = dp2[i-1][j-arr[i-1]] or dp2[i-1][j]
    return dp2[n][target]

print(bottomUpApproach(target,n))