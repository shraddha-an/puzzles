# Given an array of strings, return another array containing all of its longest strings.

def solution(inputArray):
    if len(inputArray) == 1: return inputArray
    
    # Find out the length of the longest string
    max_len = max([len(st) for st in inputArray])
    
    # Gather all strings with this max length
    strings = [st for st in inputArray if len(st) == max_len]
    
    return strings
    


