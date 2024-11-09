n,m = map(int,input().split())

table = [list(map(int,input())) for _ in range(n)]

answer = 1
valid = False
### starting axis i,j
for i in range(n-1):
    for j in range(m-1):
        for l in range(min(n-i-1,m-j-1),0,-1):
            if (table[i][j]==table[i+l][j]==table[i][j+l]==table[i+l][j+l]):
                answer = max(answer,(l+1)*(l+1))

print(answer)
