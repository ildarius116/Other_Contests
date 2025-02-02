"""
6 10 20 30
8 17 5 28 39 13

6 10 20 30
8 17 5 28 39 13
"""


def correction_list(a_lst, list_cor, target_num):
    for a_cur in a_lst:
        ost = a_cur % target_num
        list_cor.append(target_num - ost)
    return list_cor


def search_minimum(act_min, summ, list_cor):
    s_ind = 0
    while s_ind < len(a_lst):
        if summ + list_cor[s_ind] < act_min:
            act_min = summ + list_cor[s_ind]
        s_ind += 1
    return act_min


n, x, y, z = map(int, input().split())
a_lst = list(map(int, input().split()))
x_list_cor = correction_list(a_lst, [], x)
y_list_cor = correction_list(a_lst, [], y)
z_list_cor = correction_list(a_lst, [], z)

act_min = float('inf')
f_ind = 0
while f_ind < len(a_lst):
    if x_list_cor[f_ind] == y_list_cor[f_ind] == z_list_cor[f_ind]:
        if x_list_cor[f_ind] < act_min:
            act_min = x_list_cor[f_ind]
    elif x_list_cor[f_ind] == y_list_cor[f_ind]:
        tmp_summ = x_list_cor[f_ind]
        act_min = search_minimum(act_min, tmp_summ, z_list_cor)
    elif x_list_cor[f_ind] == z_list_cor[f_ind]:
        tmp_summ = x_list_cor[f_ind]
        act_min = search_minimum(act_min, tmp_summ, z_list_cor)
    elif z_list_cor[f_ind] == y_list_cor[f_ind]:
        tmp_summ = z_list_cor[f_ind]
        act_min = search_minimum(act_min, tmp_summ, z_list_cor)
    f_ind += 1

alt_min = min(x_list_cor) + min(y_list_cor) + min(z_list_cor)
if alt_min < act_min:
    act_min = alt_min

print(act_min)
