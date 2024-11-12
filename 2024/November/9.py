#Minimum sum
'''
Given an array arr[] such that each element is in the range [0 - 9], find the minimum possible sum of two numbers formed 
using the elements of the array. All digits in the given array must be used to form the two numbers. 
Return a string without leading zeroes.
'''

class Solution:
    def minSum(self, arr):
        # Sort the array
        arr.sort()
        
        num1 = ''
        num2 = ''
        
        # Distribute the digits alternately
        for i in range(len(arr)):
            if i % 2 == 0:
                num1 += str(arr[i])
            else:
                num2 += str(arr[i])
        
        # Function to add two numbers represented as strings
        def addStrings(num1, num2):
            i, j = len(num1) - 1, len(num2) - 1
            carry = 0
            result = []
            
            while i >= 0 or j >= 0 or carry:
                n1 = int(num1[i]) if i >= 0 else 0
                n2 = int(num2[j]) if j >= 0 else 0
                total = n1 + n2 + carry
                carry = total // 10
                result.append(str(total % 10))
                i -= 1
                j -= 1
            
            # The result is reversed
            return ''.join(result[::-1])
        
        # Add the two numbers
        sum_str = addStrings(num1, num2)
        
        # Remove leading zeros
        sum_str = sum_str.lstrip('0')
        
        # If the result is empty, return '0'
        return sum_str if sum_str else '0'
