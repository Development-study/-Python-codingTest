# 최댓값과 최솟값 (프로그래머스 2단계 문제)

def solution(s):
    answer = ''
    numbers = list(map(int, s.split(" ")))
    numbers.sort()
    min = numbers[0]
    max = numbers[len(numbers) - 1]
    answer = f'{min} {max}'
    return answer

print(solution("-1 -1"))