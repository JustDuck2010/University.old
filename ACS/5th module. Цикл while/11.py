a = input()
ar = [x for x in a]
aa = []
ab = []
ac = []
f = 0
q = a.count('h')
for i in range(len(ar)):
    if ar[i] == 'h':
        f += 1
    if f == 0:
        aa.append(ar[i])
    if 0 < f < q:
        ab.append(ar[i])
    if f == q:
        ab.append('h')
        f += 1
    if f > q and ar[i] != 'h':
        ac.append(ar[i])
bb = list(reversed(ab))
aa = [str(i) for i in aa]
ac = [str(i) for i in ac]
ba = ''.join(aa)
bb = ''.join(bb)
bc = ''.join(ac)
print(ba, bb, bc, sep = '')
