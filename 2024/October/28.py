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
