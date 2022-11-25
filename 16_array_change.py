# Solution:
# 1) Compare 2 successive elements at once.
# 2) If the 2nd element > 1st element, then no change is required.
# 3) If the the 2nd element == 1st element, add 1 to the 2nd element.
# 4) If the 2nd element < 1st element, then find the difference; add diff + 1 to the 2nd element.
# 5) Update the count var accordingly. 

def solution(a):
    count = 0
    
    # Step through the array considering 2 consecutive elements at once.
    for i in range(len(a) - 1):
        
        # Check if 2nd element is < or = 1st element.
        if a[i + 1] <= a[i]:
            # Compute difference & add 1.
            p = a[i] - a[i + 1] + 1
            
            # Add this diff to 2nd element to make it > 1st element.
            a[i + 1] = a[i + 1] + p
            
            # Update count
            count = count + p
            
    
    return count