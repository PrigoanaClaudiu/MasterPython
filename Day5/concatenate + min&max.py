def miniMaxi(s):
    mini = s[0]
    maxi = s[0]

    for i in range(0, len(s)):
        if mini > s[i]:
            mini = s[i]
        if maxi < s[i]:
            maxi = s[i]

    return mini, maxi

s = [1, 2, 5, 6, 2]
s2 = [5, 2, 12, 3, 6]
print(s+s2)

mini, maxi = miniMaxi(s+s2)
print(mini, maxi)

