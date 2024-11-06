num_inputs = int(input())
nums = [int(input()) for _ in range(num_inputs)]

def gauss(num):
    return num*(num+1)//2

def max_t_n(num):
    n = 0
    while gauss(n) < num:
        n+=1
    return n

for num in nums:
    max_T_n = max_t_n(num)
    valid = 0
    for i in range(1,max_T_n):
        for j in range(1,max_T_n):
            for k in range(1,max_T_n):
                if gauss(i) + gauss(j) + gauss(k)== num:
                    valid = 1
                    # print(gauss(i),gauss(j),gauss(k))
                    # print(i,j,k)
                if valid:
                    break
            if valid:
                break
        if valid:
            break
    print(valid)
