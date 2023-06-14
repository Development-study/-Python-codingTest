# 나머지가 1이 되는 수 찾기 (프로그래머스 1단계 문제)

def solution(n):
    for i in range(1, n):
        if n % i == 1:
            return i

print(solution(10))
