"""
Вывод максимально долгого списка песен

5 "Первая 01:01" "Вторая 02:00" "Третья 03:00" "Четвёртая 03:01" "Пятая 01:00" 10
4 "Первая 01:01" "Вторая 02:00" "Третья 03:00" "Четвёртая 03:01" 10
5 Первая 01:01 Вторая 02:00 Третья 03:00 Четвёртая 03:01 Пятая 01:00 10
sleep(1000)
python Sber_01.py 5 "Первая 01:01" "Вторая 02:00" "Третья 03:00" "Четвёртая 03:01" "Пятая 01:00" 10
python Sber_01.py 5 "Первая 01:01" "Вторая 04:00" "Третья 05:00" "Четвёртая 05:01" "Пятая 01:00" 10

python Sber_01.py 3 "First 04:20" "Second 0:39" "Last 0:40" 5

python Sber_01.py 7 "Каждый 01:20" "Охотник 01:20" "Желает 01:20" "Знать 01:20" "Где 01:20" "Сидит 01:20" "Фазан 01:20" 10

python Sber_01.py 25 "эhньjYsШnwТЩ 04:49" "IzЫmЙЛсЭEТрУ 06:18" "UUмоdxNСSмбХ 04:32" "FYЗcчwкЕёЭРн 09:13" "rrФтКИРDфсБр 05:49" "xгГЦDNZyDЙдЩ 08:54" "РRлуъЦЬмдхoЗ 08:19" "ЫycОчjqqКVЗН 01:48" "юЫОЛтЙgШTfGE 09:37" "ушёКUWтcдАЗВ 00:05" "ЧCmLЮхвЦъWLЦ 08:35" "EЕьSpфнIЖЁaд 02:32" "рзkEШnмхQСCN 06:45" "jЙиНТOyPУЗsD 00:07" "ШшхlиOНэЭмqж 05:00" "юzЧУчРгВэМQл 04:25" "ЗКRSЧeIЭТьшS 08:43" "BчэTдBчШHёuз 07:38" "яqЧlCrтJсаon 09:38" "NqВЛтЛlЯоПdИ 09:23" "шЛЪёдwЮёгфВQ 01:26" "БлDTЗхЦuмMОH 08:46" "фЩeМSпCЖTtЁя 05:53" "рвYMТеuВЧиЬh 01:56" "ЁТjИhкaЩиcЙх 07:05" 100


IzЫmЙЛсЭEТрУ
UUмоdxNСSмбХ
FYЗcчwкЕёЭРн
rrФтКИРDфсБр
xгГЦDNZyDЙдЩ
РRлуъЦЬмдхoЗ
ЫycОчjqqКVЗН
юЫОЛтЙgШTfGE
ЧCmLЮхвЦъWLЦ
EЕьSpфнIЖЁaд
рзkEШnмхQСCN
jЙиНТOyPУЗsD
ШшхlиOНэЭмqж
юzЧУчРгВэМQл
ЗКRSЧeIЭТьшS
NqВЛтЛlЯоПdИ




FYЗcчwкЕёЭРн
ЫycОчjqqКVЗН
юЫОЛтЙgШTfGE
ушёКUWтcдАЗВ
EЕьSpфнIЖЁaд
рзkEШnмхQСCN
jЙиНТOyPУЗsD
ШшхlиOНэЭмqж
юzЧУчРгВэМQл
ЗКRSЧeIЭТьшS
BчэTдBчШHёuз
яqЧlCrтJсаon
NqВЛтЛlЯоПdИ
шЛЪёдwЮёгфВQ
БлDTЗхЦuмMОH
фЩeМSпCЖTtЁя
рвYMТеuВЧиЬh
ЁТjИhкaЩиcЙх

"""

import sys
from itertools import combinations


def output(s_d, t):
    for key in s_d.keys():
        print(key)
    print(f"{f'{t // 60}' if t // 60 >= 10 else f'0{t // 60}'}"
          f":"
          f"{f'{t % 60}' if t % 60 > 10 else f'0{t % 60}'}")


def song_comb(s_d, t, t_l, N, depth, b_t, b_d, s_q, b_l):
    if t <= t_l:
        output(s_d, t)
    else:
        s_d[depth + 1] = 0
        for combs in combinations(s_d.items(), N):
            c_l = [v[1] for v in combs if v[1] != 0]
            sum_t = sum(c_l)
            if sum_t <= t_l and sum_t >= b_t:
                b_t = sum_t
                b_d = {v[0]: v[1] for v in combs if v[1] != 0}
                b_l.append(b_d)
        if b_t:
            for d in b_l:
                # print(d, len(d))
                if len(d) < 18:
                    print(len(d))
            output(b_d, b_t)
        if not b_t:
            song_comb(s_d, t, t_l, N - 1, depth + 1, b_t, b_d, s_q, b_l)


s_d, M, N = {}, 0, 0
for arg in sys.argv[1:]:
    if arg == sys.argv[1]:
        N = int(arg)
    elif arg == sys.argv[-1]:
        M = int(arg) * 60
    else:
        S, L = arg.split(' ')[0], arg.split(' ')[1]
        L = int(L.split(':')[0]) * 60 + int(L.split(':')[1])
        if 0 < len(S) < 255 and 1 < L < 5999:
            s_d[S] = L
else:
    if 2 < N < 100 and 0 < M < 60000 and min(s_d.values()) <= M:
        song_comb(s_d, sum(s_d.values()), M, N, 0, 0, {}, len(s_d), [])
