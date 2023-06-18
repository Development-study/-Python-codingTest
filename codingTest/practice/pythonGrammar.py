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
array = [[0] * n for _ in range(n) ] # [[0,0,0,0],[0,0,0,0], [0,0,0,0]]

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

# 내장 함수
result = [1,2,3,4,5]

sum(result) #iterable 객체가 들어왔을 때 (반복 가능한 객체) 리스트, 사전자료형, 튜플자료형 등

min(7,3,5,2)

max(7,3,5,2)

result = eval( "(3+5) * 7" )
print(result)

result = sorted([9,1,8,5,4]) # 오름차순 정렬
result = sorted([9,1,5,1,4], reverse=True) # 기존 객체는 변경되지 않으며 return 값이 존재한다.

result.sort() # void 문이다 result가 변경된다.

data = [('홍길동', 35), ('이순신', 17), ('아무개', 88)]
result = sorted(data, key = lambda x : x[1], reverse = True)
print(result)

# 위와 같은 값을 가진다.
data.sort(key = lambda x: x[1], reverse = True)
print(data)

data = ["23", "59", "59"]
print(":".join(data))
# 23:59:59

# itertools : 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리
# permutations (순열)
# combinations (조합)
# product (중복을 허용하는 순열)
# combinations_with_replacement (중복을 허용하는 모든 조합)
from itertools import permutations, combinations, product, combinations_with_replacement

data = ['a', 'b', 'c'] # 데이터 준비

# 리스트에서 3개를 뽑아 나열하는 모든 경우를 출력
result = list(permutations(data,3)) # 모든 순열 구하기

print(result)

result = list(combinations(data,2)) # 2개를 뽑는 모든 조합 구하기

print(result)

result = list(product(data,repeat = 2)) # 2개를 뽑는 모든 순열 구하기 (중복 허용)

print (result)

result = list(combinations_with_replacement(data,2)) # 2개를 뽑는 모든 조합 구하기 (중복 허용)

print (result)

# heapq : 힙기능을 위해 heapq 라이브러리를 제공
# heapq.heappush() 삽입
# heapq.heappop() 꺼냄
import heapq

def heapsort(iterable):
      h = []
      result = []
      # 모든 원소를 차례대로 힙에 삽입
      for value in iterable:
              heapq.heappush(h, value)
      # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
      for i in range(len(h)):
              result.append(heapq.heappop(h))
      return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 부호를 사용하여 최대 힙(max heap) 구현
def heapsort(iterable):
      h = []
      result = []
      # 모든 원소를 차례대로 힙에 삽입
      for value in iterable:
              heapq.heappush(h, -value)
      # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
      for i in range(len(h)):
              result.append(-heapq.heappop(h))
      return result

result = heapsort([1,3,5,7,9,2,4,6,8,0])
print(result)
#[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# bisect : 이진탐색을 쉽게 구현할 수 있도록하는 라이브러리
# bisect_left(a,x)
#   정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# bisect_right(a,x)
#   정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
from bisect import bisect_left, bisect_right

a = [1, 2, 4, 4, 8]
x = 4

print(bisect_left(a, x))  # 2
print(bisect_right(a, x)) # 4

#'정렬된 리스트'에서 '값이 특정 범위에 속하는 원소의 개수'를 구하고자 할 때 사용

def count_by_range(a, left_value, right_value):
        right_index = bisect_right(a, right_value)
        left_index = bisect_left(a, left_value)
        return right_index - left_index

# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))       # 2

# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))      # 6

# collections : 유용한 자료구조를 제공하는 표준 라이브러리

# deque
# 스택, 큐를 구현할 때 사용하는 라이브러리
from collections import deque

data = deque([2,3,4])
data.appendleft(1)
data.append(5)

data.pop()
data.popleft()

print(data)  # deque([2, 3, 4])
print(list(data)) # [2, 3, 4]

# Counter
# 등장 횟수를 세는 기능을 제공
from collections import Counter

counter = Counter(['red', 'blue', 'green', 'blue', 'blue'])

print(counter['blue']) # 'blue'가 등장한 횟수 출력
print(dict(counter)) # 사전 자료형으로 변환 list,set도 가능하고 두개가 같은 값을 가진다

# 3
# {'red': 1, 'blue': 3, 'green': 1}

# math :수학적인 기능을 포함하고 있는 라이브러리
# 팩토리얼, 제곱근, 최대공약수(GCD) , Pi
import math

print(math.factorial(5)) # 5 팩토리얼 출력

print(math.sqrt(7)) # 7의 제곱근 출력

print(math.gcd(21,14)) # 21과 14의 최대 공약수 , 7

print(math.pi) # 파이 출력

print(math.e) # 자연상수 출력


array1 = [1, 2, 3, 4]
array2 = [4, 3, 2, 1]
print(list(zip(array1, array2))) # 앞에랑 뒤의 리스트를 인덱스끼리 합침

print(list(range(19))) # 0부터 18까지의 리스트를 생성

print(bin(2)[2:]) # 2진수로 변환
print('string'.zfill(10)) # 인수로 넘어간 길이만큼 만들기 위해 앞에 0을 추가
print('string'.replace('s', 'r')) # 문자를 변경

import re # 정규식 사용 라이브러리

pattern = re.compile(r'[0-9]|10') # 0 부터 10까지 숫자를 리스트로 추출
pattern2 = re.compile(r'([a-z])') # a 부터 z까지 문자를 리스트로 추출
pattern3 = re.compile(r'[0-9]{2}') # 0 부터 9까지 숫자를 2개씩 리스트로 추출
print(pattern.findall('12d1234dsdfa1'))
print(pattern2.findall('12d1234dsdfa1'))
print(pattern3.findall('12d1234dsdfa15'))

from collections import deque

list = [0] * 3
dequeue = deque(list, maxlen=5) # 최대 5개까지 들어갈 수 있는 deque를 생성
for i in range(1, 7): 
       dequeue.append(i) # 1부터 6까지 하나씩 넣을 때 최대 개수가 5개라 1이 빠지고 2, 3, 4, 5, 6 이 들어가게 됨
print(dequeue) # 2, 3, 4, 5, 6

from collections import Counter

list = ['ab', 'bd', 'a', 'c', 'd', 'e', 'a', 'b', 'e']
print(Counter(list)['a']) # 리스트에서 a의 개수를 셈
print(dict(Counter(list))) # 개수와 함께 사전형식으로 만듬 key가 리스트 값 value가 갯수