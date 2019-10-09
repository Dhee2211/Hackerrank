#!/bin/python3

def hour_glass(arr):
    total = []
    for i in range(4):
        for j in range(4):
            s = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            total.append(s)
    total.sort()
    print(total[15])  


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    hour_glass(arr)
