# Solution:
    # 1) Check each elemenet in both arrays for equality.
    # 2) When the 1st instance of an unequal element occurs, store its index in a list.
    # 3) When another unequal instance occurs, swap the elements at the unequal instances.
    # 4) Check if arrays are similar after this swap.

def solution(a, b):
    if a == b: return True
    
    i = 0
    prev = []
    
    while i < len(a):
        if a[i] != b[i]:
            
            # Check if a previous unequal instance has already occurred.
            if len(prev):
                
                # Swap the current & previous unequal instance.
                a[i], a[prev[0]] = a[prev[0]], a[i]
                
                # Check if the arrays are now similar
                if a == b: return True
            
            else:
                prev.append(i)
        
        i += 1
    
    return False
    