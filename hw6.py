def multiple_of_three(n):
    if n == 1:
        return 3
    return multiple_of_three(n-1) + 3
    
    
print(multiple_of_three(5))

print(multiple_of_three(4))