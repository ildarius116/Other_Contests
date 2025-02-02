"""
Пример 1
Входные данные:
1 2 3 4 5 6 7 8 9
3
Выходные данные:
24
Пример 2
Входные данные:
-1 -2 -3 -4 -5 -6 -7 -8 -9
3
Выходные данные:
-6


"""


def max_sequence_sum(numbers: str, sequence_length: str) -> str:
    n_lst = list(map(int, numbers.split()))
    sl = int(sequence_length)
    max_summ = float("-inf")
    for i in range(len(n_lst) - sl + 1):
        summ = sum(n_lst[i: i + sl])
        if summ > max_summ:
            max_summ = summ
    return str(max_summ)


numbers_list = input()
sequence_length = input()
result = max_sequence_sum(numbers_list, sequence_length)
print(result)
