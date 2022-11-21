# Given matrix, a rectangular matrix of integers, where each value represents the cost of the room, your task is to return the total sum of all rooms available for occupancy.
# Free rooms & the rooms below the free rooms are unfit for occupancy.

def solution(matrix):
    # My approach:
    # 1) For each floor note down which index is 0.
    # 2) Only visit till total_floors - 1; make the rooms below free rooms; free as well.
    # 2) While stepping through the row/floor matrices, make the values in the free columns as 0.
    
    # Stepping through floors.
    for col in range(len(matrix) - 1):
        # Stepping through each room on a floor.
        for row in range(len(matrix[0])):
            if matrix[col][row] == 0:
                
                # Set the value directly below to 0 as well
                matrix[col + 1][row] = 0

    
    # Sum the remaining room values
    g = sum([elem for row in matrix for elem in row])
    
    return g
 
