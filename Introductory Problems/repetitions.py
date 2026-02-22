import sys
input = sys.stdin.readline

s = input()
mx, curr = 1, 1

for i in range(1,len(s)):

    if s[i-1] == s[i]:
        curr+=1
        mx = max(mx, curr)
    else:
        curr = 1

print(mx)