def func(x, y):
    values = []
    for i in range(0,x+1):
        values.append([0]*(y+1))

    for i in range(0,y+1):
        values[i][0] = i 

    for i in range(1, x+1):
        for j in range(1, y+1):
            values[i][j] = 3*values[i-1][j] - 2* values[i][j-1]*values[i][j-1]

    return values

print(func(2,2))

