vow = ""
conso = ""

s = "abcdefghijklmnopqrstuvwxyz"

for i in s:
    if i in ("a","e","i","o","u","A","E","I","O","U"):
        vow = vow+i
    else:
        conso = conso +i

print(len(vow))
print(len(conso))