def foo(num, exp):
    if num == 0:
        return -1
    if 0 < num < 2:
        return 0
    while True:
        num = num // 2
        exp += 1
        if num == 1 or num == 0:
            break
    return exp


n = int(input())
res_list = []
for i in range(1, n + 1):
    a = int(input())
    exp = summ = 0
    for i in range(3):
        exp = foo(a, 0)
        if exp == -1:
            summ = -1
            break
        else:
            summ += 2 ** exp
        a -= 2 ** exp
    res_list.append(summ)

for res in res_list:
    print(res)
