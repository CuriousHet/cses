import sys
input = sys.stdin.readline

n,m = map(int, input().split())
grid = [list(input().strip()) for _ in range(n)]

vis = [[False]*m for _ in range(n)]
dirs = [(-1,0), (1,0), (0,-1), (0,1)]
cnt = 0

for i in range(n):
    for j in range(m):


        if grid[i][j] == '.' and vis[i][j] == False:
           cnt += 1
           stack = [(i,j)]
           vis[i][j] = True

           while stack:
               
               x, y = stack.pop()
               for dx, dy in dirs:
                   new_row = x + dx 
                   new_col = y + dy

                   if 0<=new_row<n and 0<=new_col<m and not vis[new_row][new_col] and grid[new_row][new_col] == '.':
                       vis[new_row][new_col] = True
                       stack.append((new_row, new_col))

print(cnt)