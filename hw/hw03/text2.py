def count_coins(change):
    def count(n,m):
        if m > n:
            return 0
        elif m == n:
            return 1
        else:
            return count(n - m, m) + count(n, get_next_coin(m))
    return count(change,1)

def get_next_coin(coin):
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25
print (count_coins(10))