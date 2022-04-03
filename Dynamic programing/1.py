a = input()

array = list(map(int,input().split()))

result = 0
cnt = 0 
for i in array:
  cnt = array[i]
  if(cnt<array[i]):
    print(cnt)

    
  
