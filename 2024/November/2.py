#Given an unsorted array arr and a number k which is smaller than the size of the array.
#Return true if the array contains any duplicate within k distance throughout the array else false.

class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        # your code
        tmp = []
        for i in range(len(arr)):
            if arr[i] in tmp:
                return True
            tmp.append(arr[i])
            if i>=k:
                tmp.remove(arr[i-k])
        return False
            
