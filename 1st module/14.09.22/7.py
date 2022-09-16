#program was written 15.09.22 in home by Igor B.

#1234 -> 13
#1999 -> 20
#2000 -> 20
#2001 -> 21

a = int(input())
q = 0
b = a
while b > 0:
    q += 1
    b//=10
p = a//(10**(q-2))
if a%100 >= 1:
    p += 1
print(p)