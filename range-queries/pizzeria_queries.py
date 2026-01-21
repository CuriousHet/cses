import sys
input = sys.stdin.readline

INF = 10**18

N, Q = map(int, input().split())
p = list(map(int, input().split()))

# build size
size = 1
while size < N:
    size <<= 1
    
mn0 = [INF] * (2 * size)
mn1 = [INF] * (2 * size)

# build leaves
for i in range(N):
    mn0[size + i] = p[i] + (i + 1)
    mn1[size + i] = p[i] + (N - i)

# build internal nodes
for i in range(size - 1, 0, -1):
    mn0[i] = min(mn0[2*i], mn0[2*i + 1])
    mn1[i] = min(mn1[2*i], mn1[2*i + 1])

def update(idx, val):
    i = size + idx
    mn0[i] = val + (idx + 1)
    mn1[i] = val + (N - idx)
    i >>= 1
    while i:
        mn0[i] = min(mn0[2*i], mn0[2*i + 1])
        mn1[i] = min(mn1[2*i], mn1[2*i + 1])
        i >>= 1


def query(l, r, t):
    res = INF
    l += size
    r += size
    while l <= r:
        if l & 1:
            res = min(res, mn1[l] if t else mn0[l])
            l += 1
        if not (r & 1):
            res = min(res, mn1[r] if t else mn0[r])
            r -= 1
        l >>= 1
        r >>= 1
    return res


out = []
for _ in range(Q):
    data = list(map(int, input().split()))
    if data[0] == 1:
        _, k, x = data
        update(k - 1, x)
    else:
        _, k = data
        k -= 1
        left = query(0, k, 1)
        right = query(k, N - 1, 0)
        ans = min(
            left - (N - k),
            right - (k + 1)
        )
        out.append(str(ans))

print("\n".join(out))
