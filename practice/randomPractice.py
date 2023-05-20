# 랜덤 (random 라이브러리)

from random import * # random 라이브러리 안의 모든 것을 사용

print(random()) # 랜덤한 값 생성 (0.0 ~ 1.0)
print(random() * 10) # (0.0 ~ 10.0) 이하
print(int(random() * 10)) # (0 ~ 10) 이하
print(int(random() * 10) + 1) # (1 ~ 10) 이하
print(randrange(1, 46)) # (1 ~ 45) 미만
print(randint(1, 45)) # (1 ~ 45) 이하
