# Solution:
# 1) Make a counter of 1 string.
# 2) Step through the 2nd string & icnrease a count var when a common char is found.
# 3) Decrease count of the char from the counter at the same time.

from collections import Counter

def solution(s1, s2):
    c1 = Counter(s1)
    
    s = 0
    
    for c in s2:
        if c in c1:
            s += 1
            
            # Reduce its count in the counter
            c1[c] -= 1
            
            # Check if the char's count == 0; then remove it from the counter.
            if c1[c] == 0:
                c1.pop(c)
    
    
    return s