# Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.

#Recursive approach
def recur(arr1,arr2,ind):
    if ind<0 and sum(arr1)==sum(arr2):
        return True
    if ind<0:
        return False
    
    return recur(arr1+[arr[ind]],arr2,ind-1) or recur(arr1, arr2+[arr[ind]],ind-1)


arr = [1,5,11,5,4]
n = len(arr)
total = sum(arr)
print(recur([],[],n-1))


##### HOWEVER, it can be interpreted as Subset Sum problem. If we check sum(arr)//2 can be formed from the array, we are effectivly proving it's existence given that sum(arr)%2 = 0

def recur2(target, index):
    if target==0:
        return True    
    if index<=0:
        return False

    if arr[index-1]<=target:
        return recur2(target-arr[index-1], index-1) or recur2(target,index-1)
    else:
        return recur2(target,index-1)

if total%2: print(False)
else:
    print(recur2(total//2,n))


# Memoization
dp = [[-1]*(total//2 + 1) for i in range(n+1)]
def topDownApproach(target,index):
    if target==0:
        return True
    
    if index<=0:
        return False

    if dp[index][target]!=-1:
        return dp[index][target]
    
    if arr[index-1]<=target:
        dp[index][target] = topDownApproach(target-arr[index-1],index-1) or topDownApproach(target,index-1)
    else:
        dp[index][target] = topDownApproach(target,index-1)

    return dp[index][target]

print(topDownApproach(total//2,n))

# Tabulation

dp2 = [[-1]*(total//2 +1 ) for i in range(n+1)]

def bottomUpApproach(target,index):
    for i in range(index+1):
        for j in range(target+1):
            if i==0:
                dp2[i][j] = False
            if i==0 and j==0:
                dp2[i][j] = True
            if i!=0 and j==0:
                dp2[i][j] = False
            if i>0 and j>0:
                if arr[i-1]<=j:
                    dp2[i][j] = dp2[i-1][j-arr[i-1]] or dp2[i-1][j]
                else:
                    dp2[i][j] = dp2[i-1][j]
    return dp2[index][target]

print(bottomUpApproach(total//2, n))