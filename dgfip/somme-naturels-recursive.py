def calc_sum(a, i = 0):
    if i == len(a):
        return 0
    if a[i] > 0:
        sum = a[i] + calc_sum(a, i+1)
    else:
        sum = calc_sum(a, i+1)
    return sum

a = [1, -5, 3, 6, -8, 6]
print(calc_sum(a))
