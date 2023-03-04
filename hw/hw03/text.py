def num_eights(x):
    if x % 10 == 8:
        return num_eights(x//10)+1
    if x == 0:
        return 0
    return num_eights(x//10)

def pingpong(n):
    def flag(x):
        if x == 1:
            return 1
        if num_eights(x) or x % 8 == 0:
            return -flag(x-1)
        return flag(x-1)
    if n == 1:
        return 1
    return pingpong(n-1) + flag(n-1)


print(pingpong(18))








def ping(n):
    flag , res  = 1 , 0
    index = 1
    while index <=n:
        res += 1*flag
        if num_eights(index) or index % 8 == 0 :
            flag *= -1
        index += 1
    return res



