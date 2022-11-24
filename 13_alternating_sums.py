def solution(a):
    # Solution:
    # 1) Sort alternate elements into 2 lists.
    # 2) Calculate the sum of both lists & return them
    t1, t2 = [], []
    
    for i in range(len(a)):
        if i % 2 == 0:
            t1.append(a[i])
        else:
            t2.append(a[i])
    
    return [sum(t1), sum(t2)]
    
            