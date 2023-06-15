# 피보나치 함수 (백준 1003번 문제)

import sys
input = sys.stdin.readline


def fibonacci(n):
    global z, o
    if n == 0:
        z += 1
        return 0
    elif n == 1:
        o += 1
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
def solution():
    global z, o
    t = int(input())
    for i in range(t):
        n = int(input())
        fibonacci(n)
        print("{0} {1}".format(z, o))
        z = 0
        o = 0

z = 0
o = 0
solution()