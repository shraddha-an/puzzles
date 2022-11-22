# Solution:
# 1) Convert the number to a string & split it in half.
# 2) Take both halves & add up their digits.
# 3) Compare the sum of the 2 halves.

def solution(n):
    sn = str(n)
    k = len(sn) // 2
    
    # Splitting into halves
    half = [sn[:k], sn[k:]]
    
    # helper function to take a string, add up its digits & return the sum
    def helper(s):
        return sum([int(i) for i in s])
    
    # Adding the halves
    summed = [helper(sl) for sl in half]
    
    # Compare the 2 sums
    return len(set(summed)) == 1