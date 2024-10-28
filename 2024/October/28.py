# Remove duplicates in array

class Solution:
    def removeDuplicates(self, arr):
        a=[]
        # code here 
        a.append(arr[0])
        for i in arr:
            if i not in a:
                a.append(i)
        return a

# Optimised Time Performance

class Solution:
    def removeDuplicates(self, arr):
        check = [0] * 101
        ans = []
        for num in arr:
            if check[num] == 0:
                ans.append(num)  # Add to the result if not seen
                check[num] = 1   # Mark as seen
        
        return ans
            
