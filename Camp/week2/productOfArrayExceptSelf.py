class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        leftproducts = {0:1}
        rightproducts = {len(nums)-1:1}
        
        for i in range(1,len(nums)):
            leftproducts[i] = leftproducts.get(i-1,1) * nums[i-1]
            rightproducts[len(nums)-(i+1)] = rightproducts.get(len(nums) - i,1) * nums[len(nums)-i]
            
        products = []
        for i in range(len(nums)):
            products.append(leftproducts[i] * rightproducts[i])
            
        return products
