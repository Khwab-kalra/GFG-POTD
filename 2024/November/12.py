# Meeting Rooms
'''
Given an array arr[][] such that arr[i][0] is the starting time of ith meeting and arr[i][1] is the ending time of ith meeting, 
the task is to check if it is possible for a person to attend all the meetings such that he can attend only one meeting at a 
particular time.
Note: A person can attend a meeting if its starting time is greater than or equal to the previous meeting's ending time.
'''

class Solution:
    def canAttend(self,arr):
        # Your Code Here
        arr.sort()
        for i in range(len(arr)-1):
            if arr[i][1]>arr[i+1][0]:
                return False
        return True
                    
