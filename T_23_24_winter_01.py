r_ind = m_ind = 0
s = input()
for ind in range(len(s)):
    if s[ind].lower() == "r":
        r_ind = ind
    elif s[ind].lower() == "m":
        m_ind = ind
if r_ind < m_ind:
    print("Yes")
else:
    print("No")
