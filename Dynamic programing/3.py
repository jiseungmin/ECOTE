# 효율적인 화폐구성 문제
a,b = map(int(input().split()))
array=[]
for i in range(a):
  array.append(int(input))

d = [10001]*(b+1)
d[0] = 0
for i in range(a):
  for j in range(array[i],b+1):
    if d[j-array[i]] != 10001:
      d[j] = min(d[j], d[j - array[i] + 1])

if d[b] == 10001:
  print(-1)
else:
  print(d[b])  


