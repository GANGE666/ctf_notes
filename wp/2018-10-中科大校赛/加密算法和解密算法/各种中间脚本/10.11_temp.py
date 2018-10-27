m = [
    [23, 69, 40, 61, 47, 21, 62, 73, 18, 81],
    [46, 67, 40, 54, 31, 23, 54, 75, 64, 69],
    [21, 80, 63, 33, 60, 26, 39, 32, 48, 39],
    [80, 27, 69, 53, 37, 81, 24, 61, 23, 50],
    [35, 22, 66, 43, 68, 36, 67, 22, 58, 37],
    [81, 64, 51, 46, 37, 44, 75, 77, 71, 18],
    [34, 79, 74, 52, 27, 19, 38, 79, 30, 68],
    [19, 38, 52, 72, 49, 71, 36, 40, 60, 45],
    [76, 55, 41, 68, 39, 62, 48, 65, 21, 66],
    [38, 78, 43, 59, 55, 74, 50, 18, 36, 77]
]
input_num = []
add = [2, 6, 8, 8, 3, 5, 5, 7, 4, 9]
input_string = "QUICK_BROW"
charset = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_"

for c in input_string:
    input_num.append(charset.find(c))

for l in m:
    sum = 0
    for i in range(10):
        sum += input_num[i]*l[i]

    print((sum+add[m.index(l)]) % 256, end='')
    print(' ,', end='')
