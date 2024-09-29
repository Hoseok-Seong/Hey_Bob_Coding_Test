# 1번

N, M = list(map(int, input().split()))

arr = [list(map(int, input().split())) for _ in range(N)]

print(arr)

# 2번

import sys

my_input = sys.stdin.readline

N, M = list(map(int, my_input().split()))

arr = [list(map(int, my_input().split())) for _ in range(N)]

print(arr)

# 3번

import sys

my_input = sys.stdin.readline

arr_2d = list(my_input().split() for _ in range(4))

for i in range(len(arr_2d)):
    arr_2d[i][1] = int(arr_2d[i][1])

print(sorted(arr_2d))
print(sorted(arr_2d, key= lambda x : x[1], reverse=True))
print(sorted(arr_2d, key= lambda x : x[2]))

import sys

my_input = sys.stdin.readline

N = int(my_input())

my_list = [list(map(int, my_input().split())) for _ in range(N)]

output = [0] * N

for i in range(N):
    output[i] = sum(my_list[i])

print(*output, sep="\n")