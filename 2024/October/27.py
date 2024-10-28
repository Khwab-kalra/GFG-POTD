# Triplet Family : Given an array arr of integers. Find whether three numbers are such that the sum of two elements equals the third element.

class Solution:
    def findTriplet(self, arr):
        for i in range(len(arr)):
            sum = 0
            for j in arr[i+1:]:
                sum = arr[i]+j
                if sum in arr:
                    return True
        return False
        
