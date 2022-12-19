def climb(n):
    if n == 1 or n ==2:
        return n
    return climb(n-1) + climb(n-2)

print(climb(10))
