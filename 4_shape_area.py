def solution(n):
    # Areas to calculate occur in this series: 1, 5, 13, 25
    # n = 1; a = 1
    # n = 2; a = 5 => a = 1 + (2 * 4 - 4) = 5
    # n = 3; a = 13 => a = 5 + (3 * 4 - 4) = 13
    if n == 1: 
        return 1
    else: 
        return (n * 4) - 4 + solution(n - 1)

