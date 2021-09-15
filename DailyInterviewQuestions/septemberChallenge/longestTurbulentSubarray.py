class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        dp = [1 for e in range(len(arr))]
        
        for i in range(1,len(arr)-1):
            if(i%2 == 0 and arr[i-1] < arr[i]):
                dp[i] = dp[i-1]+1
            elif(i%2 == 1 and arr[i-1] > arr[i]):
                dp[i] = dp[i-1]+1
                
        ans = max(dp)
        print(dp)
        
        dp = [1 for e in range(len(arr))]
        
        for j in range(1,len(arr)-1):
            if(j%2 == 0 and arr[j-1] > arr[j]):
                dp[j] = dp[j-1]+1
            elif(j%2 == 1 and arr[j-1] < arr[j]):
                dp[j] = dp[j-1]+1
        print(dp)
        
        return max(ans,max(dp))
