# 상하좌우 문제
from posixpath import split


n = int(input())
x,y = 1, 1
plans = input().split()

# L R U D 에 따른 이동 방향      행렬 기준좌표  행 : 세로     열 : 가로 
dx = [0,0,-1,1]
dy = [-1,1,0,0]
move_types = ['L','R','U','D']

for plan in plans:
  for i in range(len(move_types)):
    if plan == move_types[i]:
      nx = x + dx[i]
      ny = y + dy[i]
  if nx<1 or ny<1 or nx>n or ny>n:
    continue 

  x,y = nx, ny  

print(x,y)
