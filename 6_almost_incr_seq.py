# Given a sequence of integers as an array, determine whether it is possible to obtain a strictly increasing sequence 
# by removing no more than one element from the array.

def solution(sequence):
    # Solution: 
    # 1) Compare 3 consecutive elements of the list, n - 2, n - 1 and n.
    # 2) If the curr < last element, then dropped = True.
    # 3) dropped notes the 1st instance where the sequence violated the strictly ^ condition
    # 4) If the strictly increasing condition is violated for the 2nd time, then the answer is False.
    dropped = False
    
    last = prev = min(sequence) - 1
    
    for i in sequence:
        # Compare current element with its predecessor.
        if i <= last:
            
            # Check if the strictly increasing condition has been previously violated.
            if dropped:
                
                # False if there are > 1 instances of the sequence decreasing.
                return False
            
            else:
                
                # Dropped = True for the 1st instance of the violation
                dropped = True
            
            # Check if the current element is also lesser than the previous-previous element
            if i <= prev:
                prev = last
            else:
                prev = last = i
        
        else:
            # Update the prev & last elements
            prev, last = last, i
    
    return True