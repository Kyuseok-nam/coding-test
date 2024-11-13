def check_bingo(bin_table):
    count = 0
    #check rows
    for i in range(5):
        row_bingo = True
        for j in range(5):
            if bin_table[i][j] == 0:
                row_bingo = False
                break
        if row_bingo:
            count +=1
    #check columns
    for i in range(5):
        col_bingo = True
        for j in range(5):
            if bin_table[j][i] == 0:
                col_bingo = False
                break
        if col_bingo:
            count+=1
    #check diagonal right
    diag_r_bingo = True
    for i in range(5):
        if bin_table[i][i]==0:
            diag_r_bingo = False
            break
    if diag_r_bingo:
        count+=1

    #check diagonal left
    diag_l_bingo = True
    for i in range(5):
        if bin_table[4-i][i]==0:
            diag_l_bingo = False
            break
    if diag_l_bingo:
        count+=1
        
    if count>=3:
        return True
    else:
        return False

table = [list(map(int,input().split())) for _ in range(5)]
bin_table = [[0,0,0,0,0] for _ in range(5)]
nums = []
for _ in range(5):
    nums += list(map(int,input().split()))


for n in range(len(nums)):
    num = nums[n]
    for i in range(5):
        for j in range(5):
            if table[i][j]==num:
                bin_table[i][j] = 1
                if check_bingo(bin_table) == True:
                    print(n+1)
                    exit()

            

        



