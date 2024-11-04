n = int(input())
answer =0 
for i in range(n):
    print(i)
    sum=i
    if (n-i)>(9*len(str(i))):
           print("check1")
           continue
    for j in range(len(str(i))):
        sum+=int(str(i)[j])
    if sum == n:
        answer = i
        break
        
print(answer) 
