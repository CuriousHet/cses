import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

bit = 1 # because sum=0 is possible in all cases, so started from that i.e 0th bit
res = []

"""
Here each bit represent if that sum is possible or not 
like initially bit = 1 i.e 0001
step 1: num = 2 {possible num = 0, 2}
bit << 2 gives 00100 i.e we added num to existing to get new possible sum
then add it to old sum i.e bit which gives bit = bit | (bit << val)
so now bit = 0001 + 0100 = 0101
 
step 2: num = 2 {possible num = 0, 2, 4}
bit      = 000101
bit << 2 = 010100
new bit  = 010101

step: 3 num = 4 {0, 2, 4, 6 ,8}
bit      = 0000010101
bit << 4 = 0101010000
new bit  = 0101010101

"""
for val in arr:
    bit |= bit << val

res = [i for i in range(1,bit.bit_length()) if bit & (1 << i)]
print(len(res))
print(*res)