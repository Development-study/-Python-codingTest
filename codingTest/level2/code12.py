# 연속된 부분 수열의 합 (프로그래머스 2단계 문제)

def solution(sequence, k):
    answers = []
    sum = 0
    l = 0
    r = -1
    
    while True:
        if sum < k:
            r += 1
            if r >= len(sequence):
                break
            sum += sequence[r]
        else:
            sum -= sequence[l]
            if l >= len(sequence):
                break
            l += 1
        if sum == k:
            answers.append([l, r])
    
    answers.sort(key=lambda x: (x[1]-x[0], x[0]))
    return answers[0]

sequence = 	[1, 1, 1, 2, 3, 4, 5]
k = 5
print(solution(sequence, k))
# 비내림차순으로 정렬된 수열이 주어질 때, 다음 조건을 만족하는 부분 수열을 찾으려고 합니다.

# 기존 수열에서 임의의 두 인덱스의 원소와 그 사이의 원소를 모두 포함하는 부분 수열이어야 합니다.
# 부분 수열의 합은 k입니다.
# 합이 k인 부분 수열이 여러 개인 경우 길이가 짧은 수열을 찾습니다.
# 길이가 짧은 수열이 여러 개인 경우 앞쪽(시작 인덱스가 작은)에 나오는 수열을 찾습니다.
# 수열을 나타내는 정수 배열 sequence와 부분 수열의 합을 나타내는 정수 k가 매개변수로 주어질 때, 
# 위 조건을 만족하는 부분 수열의 시작 인덱스와 마지막 인덱스를 배열에 담아 return 하는 solution 함수를 완성해주세요. 
# 이때 수열의 인덱스는 0부터 시작합니다.

# 1. l, r 인덱스를 각각 선언해준다
# 2. 반복문을 돌려 sum이 k 값보다 작다면 r 인덱스를 하나 더해서 sum에 r인덱스의 sequence 값을 더한다
# 3. sum이 k와 같은지 확인한다 같다면 answers에 l, r 인덱스 배열을 추가한다
# 4. 만약 sum이 k 보다 크다면 sum에 l 인덱스의 sequence 값을 뺀다 이후 l 인덱스를 하나 더한다
# 5. r 또는 l이 sequence 값을 넘어섰다면 반복문을 종료한다
# 6. 마지막으로 정렬을 하여 l 값이 가장 작은 값을 반환한다