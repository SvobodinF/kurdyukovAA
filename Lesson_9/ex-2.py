n: int = [[1,3,5],[1,2,4],[5,11,7],[-7,5,-3]]

def func():
    maxSum = 0
    line = -1

    for i in range(len(n)):
        lineSum = 0
        for j in range(len(n[i])):
            if line == i:
                continue

            if n[i][j] % 2 == 0:
                line = i
            else:
                lineSum += my_abs(n[i][j])

        if lineSum > maxSum:
            maxSum = lineSum    
            line = i

    print(f"{line}, {maxSum}")

def my_abs(a):
    return a if a > 0 else -a

func()