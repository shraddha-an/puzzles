def solution(picture):
    # Solution:
    # 1) Add borders to the existing strings.
    # 2) Find out the number of characters this new string has.
    # 3) Introduce perimeter borders of * x k to the rectangular matrix.
    modded_string = ["*" + s + "*" for s in picture]
    
    # Length of perimeter borders
    k = "*" * len(modded_string[0])
    
    # New list with the borders added in
    l = []
    l.append(k)
    l.extend(modded_string)
    l.append(k)
    
    return l