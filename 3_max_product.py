# Given an array of integers, find the pair of adjacent elements 
# that has the largest product and return that product.
# Constraints: -1000 <= array[i] <= 1000

def solution(inputArray):
    max_product = -2000
    
    for i in range(len(inputArray) - 1):
        product = inputArray[i] * inputArray[i + 1]
        max_product = max(max_product, product)
    
    return max_product


