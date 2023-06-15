# 나머지 합 구하기 (백준 골드3 문제) 
from itertools import combinations

def solution(m, array):
    answer = 0

    d = [0] * len(array) 

    same_list = [0] * m
    for a in range(0, len(array)):
        d[a] = (d[a - 1] + array[a]) % m
        if d[a] == 0:
            answer += 1

        same_list[d[a]] += 1

    # 구현식 사용 방식
    for i in range(m):
        if same_list[i] > 1:
            answer += (same_list[i] * (same_list[i] - 1) // 2)

    # 라이브러리 사용 방식
    # for c in combinations(d, 2):
    #     if c[0] == c[1]:
    #         answer += 1

    return answer

array = [3, 2, 1, 5, 4]
m = 3

print(solution(m, array))

# 1. 구간 합 배열을 만든다
# 2. 구간 합 배열의 요소를 m으로 나눈다
# 3. m으로 나누었을 때 0이 나오는 요소는 나누어 떨어지므로 경우의 수에 추가한다
# 4. 구간 합 배열에서 요소가 같은 것 2개씩 묶은 것은 원본 배열에서 나누어 떨어지므로 경우의 수에 추가한다

# 구간 합 배열을 이용한 식 S[i] - S[j]는 원본 배열의 j + 1부터 i까지의 구간합이다
# 구간 합 배열의 원소를 m으로 나눈 나머지로 업데이트하고 S[i], S[j]가 같은 (i, j)쌍을 찾으면 
# 원본 배열에서 j + 1부터 i까지의 구간합이 M으로 나누어 덜어진다는 것을 확인 가능하다