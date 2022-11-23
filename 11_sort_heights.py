# Some people are standing in a row in a park. There are trees between them which cannot be moved. 
# Your task is to rearrange the people by their heights in a non-descending order without moving the trees. 

# Solution
# 1) In a separate list, sort the people heights in descending order.
# 2) Keep a tree ptr that tracks tree positions; in non-tree positions fill in the people heights from list above.
def solution(heights):
    # Sort people heights in descending order
    sorted_heights = sorted([height for height in heights if height != -1], reverse = True)

    # tree ptr to keep track of tree positions
    tree_ptr = 0

    # fill in non-tree positions with sorted heights
    for i in range(len(heights)):
        if heights[i] == -1:
            continue
        else:
            heights[i] = sorted_heights.pop()
    
    
    return heights