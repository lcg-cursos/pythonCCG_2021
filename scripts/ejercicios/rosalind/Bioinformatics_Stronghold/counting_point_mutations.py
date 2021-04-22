print("s:")
s = input()
print("t:")
t = input()
d = 0

for i in range(0,len(s)):
    #print(i , s[i], t[i])
    if s[i] != t[i]:
        d += 1

print("Hamming distance:", d)