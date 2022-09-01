# Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete item or don’t pick it (0-1 property).

weight = [10,20,30]
value = [60,100,120]
w = 50
n = len(weight)



#Recursive approach
def recur(w,n):
    if (w==0 or n==0):
        return 0

    if weight[n-1]<=w:
        return max(value[n-1]+recur(w-weight[n-1],n-1),recur(w,n-1))
    else:
        return recur(w,n-1)

print(recur(w,n))


dp = [[-1]*(w+1) for i in range(n+1)]

def topDownApproach(w,n):
    if (w==0 or n==0): return 0

    if dp[n][w] != -1: return dp[n][w]

    if weight[n-1]<=w:
        dp[n][w] = max(value[n-1]+recur(w-weight[n-1],n-1),recur(w,n-1))
    else:
        dp[n][w] = recur(w,n-1)
    
    return dp[n][w]

print(topDownApproach(w,n))


dp2 = [[-1]*(w+1) for i in range(n+1)]

def bottomUpApproach(w,n):
    for i in range(n+1):
        for j in range(w+1):
            if i==0 or j==0: 
                dp2[i][j] = 0
            elif weight[i-1]<=j:
                dp2[i][j] = max(value[i-1]+dp2[i-1][j-weight[i-1]],dp2[i-1][j])
            else:
                dp2[i][j] = dp2[i-1][j]
    return dp[n][w]

print(bottomUpApproach(w,n))