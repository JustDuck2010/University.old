#program was written 15.09.22 at home by Igor B.
amo =0
a = int(input())
b = a
while b > 0:
    amo += b%10
    b//=10
print(amo)