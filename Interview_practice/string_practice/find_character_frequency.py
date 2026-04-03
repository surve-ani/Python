
st = "abccdefgqbdeab"
f_dup = ""

print(f"a = {st}")
print(f"len(a) = {len(st)}")

for i in st:
    count = 0
    for j in st:
        if i == j:
            count = count + 1
            
    if count>0:
        if i not in f_dup:
            print(f"{i} = {count}")
            f_dup = f_dup+i

        




