# Given an array of unique integers, make the array consecutive, then return the additional number of integers added.
def solution(statues):
    main = []
    for i in range(min(statues), max(statues) + 1):
        if i not in statues:
            main.append(i)
    
    return len(main)
