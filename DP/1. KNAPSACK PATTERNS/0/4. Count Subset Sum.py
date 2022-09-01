# Given an array arr[] of length N and an integer X, the task is to find the number of subsets with a sum equal to X.
# Input: arr[] = {1, 2, 3, 3}, X = 6 
# Output: 3 
# All the possible subsets are {1, 2, 3}, 
# {1, 2, 3} and {3, 3}

# Input: arr[] = {1, 1, 1, 1}, X = 1 
# Output: 4 

arr = [1,2,3,3]
n = len(arr)
target = 6


def recur(target, index):
    if target==0:
        return 1
    if target<0 or index<=0:
        return 0

    # if arr[index-1]<=target:
    return recur(target-arr[index-1],index-1) + recur(target,index-1)
    # else:
    #     return recur(target,index-1)

print(recur(target,n))


dp = [[-1]*(target+1) for i in range(n+1)]
def topDownApproach(target,index):
    if target==0:
        return 1
    if target<0 or index<=0:
        return 0
    if dp[index][target]!=-1:
        return dp[index][target]
    
    dp[index][target] = topDownApproach(target-arr[index-1],index-1) + topDownApproach(target,index-1)

    return dp[index][target]

print(topDownApproach(target,n))

dp2 = [[-1]*(target+1) for i in range(n+1)]
def bottomUpApproach(target,index):
    for i in range(index+1):
        for j in range(target+1):
            if i==0:
                dp2[i][j]=0
            if j==0:
                dp2[i][j]=1
            if i>0 and j>0:
                if arr[i-1]<=j:
                    dp2[i][j] = dp2[i-1][j-arr[i-1]]+dp2[i-1][j]
                else:
                    dp2[i][j] = dp2[i-1][j]
    return dp2[index][target]
    
print(bottomUpApproach(target,n))