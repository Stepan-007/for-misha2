kord = input().split()
kord2 = input().split()
if ((int(kord[0]) - int(kord2[0])) ** 2 + (int(kord[1]) - int(kord2[1])) ** 2) ** 0.5 <= int(kord[2]) + int(kord2[2]):
    print('YES')
else:
    print('NO')