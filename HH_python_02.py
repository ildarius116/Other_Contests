"""
Пример 1
Входные данные:
Ivanov,5,6,7,8
Lisii,9,8,10,9
Sokolova,5,6,8,5
Tritonov,7,2,3,4
Chernov,8,8,8,8
Svetova,4,5,3,6
Zayatz,5,5,5,5
Rezhik,6,6,6,6
Выходные данные:
Lisii,9.0
Chernov,8.0
Ivanov,6.5
Rezhik,6.0
Sokolova,6.0
Zayatz,5.0

Пример 2
Входные данные:
Ivanov,4,3,2,1
Lisii,2,2,3,1
Sokolova,3,4,2,1
Tritonov,1,1,2,1
Выходные данные:
Никто
"""


def select_candidates(candidate_strings):
    c_lst = []
    r_lst = []
    for candidate in candidate_strings:
        lst = candidate.split(',')
        sur = lst[0]
        n_list = list(map(int, lst[1:]))
        middle = round((sum(n_list) / len(n_list)), 1)
        if middle >= 5:
            c_lst.append((sur, middle))
    c_lst.sort(key=lambda x: (x[1], x[0]), reverse=True)
    for cand_f, cand_n in c_lst:
        r_lst.append(f'{cand_f},{cand_n}')
    if r_lst:
        return r_lst
    return ['Никто']


lines = []
while True:
    try:
        line = input()
        if line == "":
            break
    except EOFError:
        break
    lines.append(line)

print(lines)
for candidate in select_candidates(lines):
    print(candidate)
