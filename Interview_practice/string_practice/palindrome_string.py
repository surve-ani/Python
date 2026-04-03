str = "abcdefg"

print(str == str[::-1])


rev = ""
for i in str:
    rev = i+rev

print(rev==str)