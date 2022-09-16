#program was written 15.09.22 at home by Igor B.
amo =0
for i in range(3):
    a = int(input())
    b = a//2
    if a%2>0:
        b+=1
    amo += b
print(amo)