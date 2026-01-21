import sys
input = sys.stdin.readline
write = sys.stdout.write

n, q = map(int, input().split())
arr = list(map(int, input().split()))

queries = [(0, 0, 0)] * q
for i in range(q):
    a, b = map(int, input().split())
    queries[i] = (b, a, i)

queries.sort()

bit = [0] * (n + 1)
last = {}
ans = [0] * q

j = 0

for i in range(1, n + 1):
    v = arr[i - 1]

    if v in last:
        p = last[v]
        while p <= n:
            bit[p] -= 1
            p += p & -p

    p = i
    while p <= n:
        bit[p] += 1
        p += p & -p

    last[v] = i

    while j < q and queries[j][0] == i:
        _, a, idx = queries[j]
        s = 0
        p = i
        while p > 0:
            s += bit[p]
            p -= p & -p

        t = 0
        p = a - 1
        while p > 0:
            t += bit[p]
            p -= p & -p

        ans[idx] = s - t
        j += 1

write("\n".join(map(str, ans)))