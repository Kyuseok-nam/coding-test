heights = [int(input()) for _ in range(9)]
heights.sort()
for i in range(8):
    for j in range(i+1,9):
        if (sum(heights)-heights[i]-heights[j])==100:
            for k in range(9):
                if k!=i and k!=j:
                    print(heights[k])
            exit()
