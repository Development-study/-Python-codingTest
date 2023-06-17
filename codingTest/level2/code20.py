# 뒤에 있는 큰 수 찾기 (프로그래머스 2단계 문제)

def solution(numbers):
    stack = []
    answer = [-1] * len(numbers)

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:
            answer[stack.pop()] = numbers[i]
        stack.append(i)
    
    return answer

numbers = [9, 1, 5, 3, 6, 2]
print(solution(numbers))

# 문제 설명
# 정수로 이루어진 배열 numbers가 있습니다. 
# 배열 의 각 원소들에 대해 자신보다 뒤에 있는 숫자 중에서 자신보다 크면서 가장 가까이 있는 수를 뒷 큰수라고 합니다.
# 정수 배열 numbers가 매개변수로 주어질 때, 
# 모든 원소에 대한 뒷 큰수들을 차례로 담은 배열을 return 하도록 solution 함수를 완성해주세요. 
# 단, 뒷 큰수가 존재하지 않는 원소는 -1을 담습니다.

# 제한사항
# 4 ≤ numbers의 길이 ≤ 1,000,000
# 1 ≤ numbers[i] ≤ 1,000,000

# 입출력 예
# numbers	            result
# [2, 3, 3, 5]	        [3, 5, 5, -1]
# [9, 1, 5, 3, 6, 2]	[-1, 5, 6, 6, -1, -1]