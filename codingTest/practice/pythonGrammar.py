# 자료형

# 소수부가 0일 때 0을 생략
a = 5.0 # 5.0

# 10억의 지수 표현 방식 (최단 경로문제에서 자주 사용)
a = 1e9 # 100000000.0

a = 7
b = 3

# 나누기
a / b # 2.3333333333333

# 나머지
a % b # 1

# 몫
a // b # 2

# 거듭 연산자
a ** b  # a의 b승 / 343

# 빈 리스트 선언 방법
a = list()
a = []

# 크기가 N이고 모든 값이 0인 1차원 리스트 초기화
n = 10
a = [0] * n

a = [1,2,3,4,5,6,7,8,9]

# 인덱스에 음의 정수를 넣으면 거꾸로 탐색한다
a[-1] # 인덱싱 / 9
a[-3] # 7
a[1:4] # 슬라이싱 / [2,3,4]

# 리스트 초기화
array = [i for i in range(20) if i % 2 == 1] # 0에서 19까지 중 홀수만 포함하는 리스트

# 2차원 배열을 초기화할 때 효과적이다
array = [[0] * m for _ in range(n) ] # [[0,0,0,0],[0,0,0,0], [0,0,0,0]]

a = [1,4,3]

# 리스트에 원소 삽입
a.append(2)

# 오름차순 정렬
a.sort()

# 내림차순 정렬
a.sort(reverse = True)

# 리스트 원소 뒤집기
a.reverse()

# 특정 인덱스에 데이터 추가
a.insert(2,3) # 인덱스2에 3추가

# 특정 값인 데이터 개수 세기
a.count(3)

# 특정 값 데이터 삭제 (인덱스가 낮은 것 하나)
a.remove(1) 

# 시간복잡도를 고려해서 remove는 사용하지 않는 것을 추천

a = [1,2,3,4,5,5,5]
remove_set = {3,5}

# remove_set에 포함되지 않은 값만을 저장
result = [i for i in a if i not in remove_set] # [1,2,4]

a = "Hello"
b = "World"

a + " " + b # Hello World

a * 3 # HelloHelloHello

# 파이썬 문자열은 내부적으로 리스트와 같이 처리 (인덱싱,슬라이싱) 사용 가능

a = "ABCDEF"

a[2:4] #CD

a = (1, 2, 3, 4)

# a[2] = 7 # TypeError

data = dict()
data['사과'] = 'Apple'
data['바나나'] = 'Banana'
data['코코넛'] = 'Coconut'

# {'사과': 'Apple', '바나나': 'Banana', '코코넛': 'Coconut'}

if '사과' in data:
    print("'사과'를 키로 가지는 데이터가 존재합니다.")

key_list = data.keys()
value_list = data.values()

for key in key_list:
    print(data[key]) # Apple Banana Coconut

# Set 자료형
data = set([1,1,2,3,4,4,5])

data = {1,2,3,4,5}

# 전역 변수
a = 0

def func():
        global a
        a += 1

for i in range(10):
        func()

print(a)

# 람다식
def add(a, b):
        return a + b

print(add(3,7))

# 람다 표현식으로 구현한 add() 메서드
print( (lambda a, b: a + b)(3,7) )

# 내장 함수
#   print(), input()과 같은 기본 입출력 기능부터 sorted()와 같은 정렬 기능을 포함하고 있는 내장 라이브러리
# itertools
#   파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리, 순열과 조합 라이브러리를 제공
# heapq
#   힙(Heap) 기능을 제공하는 라이브러리. 우선순위 큐 기능을 구현하기 위해 사용한다.
# bisect
#   이진탐색/이분탐색(Binary Search) 기능을 제공하는 라이브러리
# Collections
#   덱(deque), 카운터(Counter) 등의 유용한 자료구조를 포함하고 있는 라이브러리
# math
#   필수적인 수학적 기능을 제공하는 라이브러리
#   팩토리얼, 제곱급, 최대공약수(GCD), 삼각함수, 파이(pi)