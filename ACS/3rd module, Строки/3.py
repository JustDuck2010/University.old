#program was written 16.09.22 at home by Igor B.
a = input()
b = -1
c = -1
for i in range(len(a)):
    if a[i] == 'f':
        if b == -1:
            b = i
        c = i
if b == c:
    print(c)
elif c > b:
    print(b, c)
else:
    print(b)


'Дана строка, которая может содержать букву f\
Напечатайте позицию первого и последнего вхождения. Если буква f встречается только один раз, то выведите позицию один раз. Если буква f не встречается, напечатайте -1'