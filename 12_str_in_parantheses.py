def solution(s):
    # Solution
    # 1) Add a string reverse operation whenever the closing brace is encountered.
    # 2) Also add a string concatenation operation whenever an opening & closing brace is encountered.
    # 3) Apply eval method to carry out these operations.
    
    # Add a concatenation op at an "(" & a string reverse + concatenation op at ")".
    f = s.replace("(", '"+("').replace(")", '")[::-1]+"')
    
    print(type(f), f)
    
    # Make sure to enclose the string within a string
    v = '"' + f + '"'
    
    # Apply eval to execute the operations
    d = eval(v)
    
    print(d)
    
    return d
    
    