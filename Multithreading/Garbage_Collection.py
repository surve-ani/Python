import gc

a = []
a.append(a)

print(a)
# remove reference
#del a
a = None

collected = gc.collect()
print(f"GC collected {collected}")
