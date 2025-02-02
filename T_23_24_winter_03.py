"""
3 1
3 4 6

3 1
3 4 6 5 4
"""

n, m = map(int, input().split())
a_lst = list(map(int, input().split()))
a_min = a_lst[0]
a_max = a_lst[1]
a_list_cor = []
for a_cur in a_lst[2:]:
    if a_cur < a_min:
        a_list_cor.append(a_min - a_cur)
    elif a_cur > a_max:
        a_list_cor.append(a_cur - a_max)
    else:
        m -= 1
a_list_cor.sort()
cor_summ = ind = 0
while m > 0:
    cor_summ += a_list_cor[ind]
    m -= 1
    ind += 1
print(cor_summ)
