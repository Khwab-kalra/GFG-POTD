# User function Template for python3
class Solution:

    def countPairsWithDiffK(self, arr, k):
        n = len(arr)
        maxEle = 0
        # Find the maximum element in the array.
        for i in range(n):
            maxEle = max(maxEle, arr[i])
        # Create a hash table to store the occurrences of each element.
        hash_table = [0] * (maxEle + 1)
        for i in range(n):
            hash_table[arr[i]] += 1
        # Initialize the count of pairs with difference k to 0.
        count = 0
        for i in range(maxEle + 1):
            if hash_table[i]:
                if k == 0:
                    count += (hash_table[i] * (hash_table[i] - 1)) // 2
                elif i + k <= maxEle:
                    count += (hash_table[i] * hash_table[i + k])
        # Return the count of pairs with difference k.
        return count
