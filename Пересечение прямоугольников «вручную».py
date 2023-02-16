kord = input().split()
kord2 = input().split()
if abs(int(kord[0]) - int(kord2[0])) < int(kord[2]) + int(kord2[2])\
        and abs(int(kord[1]) - int(kord2[1])) < int(kord[3]) + int(kord2[3]):
    print('YES')
else:
    print('NO')
