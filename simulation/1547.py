n = int(input())
changes = [list(map(int,input().split())) for _ in range(n)]

current_pos = 1
for change in changes:
    if change[0] == current_pos:
        current_pos = change[1]
    elif change[1] == current_pos:
        current_pos = change[0]
print(current_pos)
