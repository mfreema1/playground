def stairs_naive(n):
    if(n < 3):
        return n
    one_step = stairs_naive(n - 1)
    two_step = stairs_naive(n - 2)
    return one_step + two_step

d = {1: 1, 2: 2}
def stairs_top_down(n):
    if(n in d):
        return d[n]
    one_step = stairs_top_down(n - 1)
    two_step = stairs_top_down(n - 2)
    d[n] = one_step + two_step
    return d[n]

dt = {1: 1, 2: 2}
def stairs_bottom_up(n):
    for num in range(3, n + 1):
        d[num] = d[num - 1] + d[num - 2]
    return d[n]

print(stairs_naive(35))
print(stairs_top_down(35))
print(stairs_bottom_up(35))

#cool! now let's check out the other case where we have an array of step size choices
def stairs_multi_naive(n, x):
    if n == 0:
        return 1
    total = 0
    for step in x:
        if(n - step >= 0):
            total += stairs_multi_naive(n - step, x)
    return total

print(stairs_multi_naive(5, [1, 3, 5]))

dct = {0: 1}
def stairs_multi_top_down(n, x):
    if(n in dct):
        return dct[n]
    total = 0
    for step in x:
        if(n - step >= 0):
            total += stairs_multi_top_down(n - step, x)
    dct[n] = total
    return dct[n] #doing it this way helps prevent you from forgetting to cache it

print(stairs_multi_top_down(100, [1, 3, 5]))