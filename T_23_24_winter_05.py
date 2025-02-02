"""
3 3
1 2 3
"""


def calculate_total_cuts(n, s, a_lst):
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a_lst[i]
    print(prefix)
    total = 0
    for l in range(1, n + 1):
        for r in range(l, n + 1):
            segment_sum = prefix[r] - prefix[l - 1]
            cuts = (segment_sum + s - 1) // s
            total += cuts
    return total


n, s = map(int, input().split())
a_lst = list(map(int, input().split()))
print(calculate_total_cuts(n, s, a_lst))
