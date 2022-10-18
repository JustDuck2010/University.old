a = input()
ar = [x for x in a]
ab = []
f = 0
q = a.count('h')
for i in range(len(ar)):
    if ar[i] == 'h':
        f += 1
    if not (1 <= f < q) and ar[i] != 'h':
        ab.append(ar[i])
    else:
        continue
print(*ab
#join() - метод