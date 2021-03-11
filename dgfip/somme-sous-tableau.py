def calc_sum(i, a, length):
    sum = 0
    j = i
    max_sum = None
    max_j = None
    while j < length:
        sum += a[j]
        if max_sum is None or sum > max_sum:
            max_sum = sum
            max_j = j
        j += 1
    return [max_sum, max_j]

a = [-8, -1, 5, -3, 8, -2, -10, 9]
max_i = 0
max_j = 0
max_sum = a[0]
length = len(a)
i = 0
while i < length:
    sum, j = calc_sum(i, a, length)
    if sum > max_sum:
        max_sum = sum
        max_i = i
        max_j = j
    i += 1

print(max_sum, max_i, max_j)
