def sum_tail(n, acc=0):
    if n == 0:
        return acc
    
    return sum_tail(n - 1, acc + n)

print(sum_tail(3)) 