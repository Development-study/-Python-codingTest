# 구간 합 구하기 (백준 실버1 문제)

def solution(n, m, array):

    d = [[0] * (n + 1) for _ in range(n + 1)]
    print(d)

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            d[i][j] = d[i][j-1] + d[i-1][j] - d[i-1][j-1] + array[i - 1][j - 1]


    for i in range(m):
        x1, y1, x2, y2 = array[n + i]
        result = d[x2][y2] - d[x1 - 1][y2] - d[x2][y1 - 1] + d[x1 - 1][y1 - 1]
        print(result)
        
    return 0

array = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [2, 2, 3, 4], [3, 4, 3, 4], [1, 1, 4, 4]]
n = 4
m = 3
print(solution(n, m, array))

# 1. 원본 배열에서 각 위치마다 모든 값을 더한 합 배열을 만든다
# 합 배열 공식 : D[i][j] = D[i][j - 1] + D[i - 1][j] - D[i - 1][j - 1] + A[i - 1][j - 1]
# 2. 질의를 받은 위치를 통해 합배열에서 위치를 찾고 값을 출력한다
# 위치 찾는 공식 : D[x2][y2] - D[x1 - 1][y2] - D[x2][y1 - 1] + D[x1 - 1][y1 - 1]