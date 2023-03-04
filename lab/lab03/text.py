def count_ways(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    return count_ways(n-1)+(n-2)
print(count_ways(4  ))