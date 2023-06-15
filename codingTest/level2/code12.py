# 연속된 부분 수열의 합 (프로그래머스 2단계 문제)

from itertools import combinations

def solution(sequence, k):
    answer = []

    partical_sequence_result = []
    for i in range(1, len(sequence)):
        partial_sequence = combinations(sequence, i)

        for ps in partial_sequence:
            if sum(ps) == k:
                partical_sequence_result.append(list(ps))

    min = 999999999
    result = []
    for psr in partical_sequence_result:
        if len(psr) <= min:
            result = []
            result = psr
            min = len(psr)

    f_idx = 0
    for idx, x in enumerate(sequence):
        print('{0} / {1}'.format(result[0], x))
        if result[0] == x:
            f_idx = idx

    # print(len(result))
    # print(f_idx + len(result))
    answer.append(f_idx)
    answer.append(f_idx + len(result))

    return answer

sequence = [1, 2, 3, 4, 5]
k = 7
print(solution(sequence, k))
# 비내림차순으로 정렬된 수열이 주어질 때, 다음 조건을 만족하는 부분 수열을 찾으려고 합니다.

# 기존 수열에서 임의의 두 인덱스의 원소와 그 사이의 원소를 모두 포함하는 부분 수열이어야 합니다.
# 부분 수열의 합은 k입니다.
# 합이 k인 부분 수열이 여러 개인 경우 길이가 짧은 수열을 찾습니다.
# 길이가 짧은 수열이 여러 개인 경우 앞쪽(시작 인덱스가 작은)에 나오는 수열을 찾습니다.
# 수열을 나타내는 정수 배열 sequence와 부분 수열의 합을 나타내는 정수 k가 매개변수로 주어질 때, 
# 위 조건을 만족하는 부분 수열의 시작 인덱스와 마지막 인덱스를 배열에 담아 return 하는 solution 함수를 완성해주세요. 
# 이때 수열의 인덱스는 0부터 시작합니다.

# 1. 수열의 합이 k 인 수열은 구한다
# 2. 그 수열 중 가장 길이가 짧은 수열을 구한다
# 3. 가장 길이가 짧은 수열의 인덱스를 배열에 담는다