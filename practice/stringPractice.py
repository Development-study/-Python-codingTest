# 문자열

sentence = '나는 소년입니다'
print(sentence)
sentence2 = """
이 파이썬 문법은 여러 줄을
한번에 이렇게 적을 수 있는
문자열 문법입니다.
"""
print(sentence2)

python = "Python is Amazing"
print(python.lower()) # 모두 소문자로 변경
print(python.upper()) # 모두 대문자로 변경
print(python[0].isupper()) # 대문자인지 확인
print(len(python)) # 길이
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)
print(python.find("Java"))
print(python.count("n"))

print("나는 %d살입니다." % 19)
print("나는 %s을 좋아합니다." % "파이썬")
print("Apple이라는 단어는 %c로 시작해요." % "A")
print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

print("나는 {}살입니다.".format(19))
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 19, color = "빨간"))

# python v3.6 이상
age = 19
color = "퍄란"

print(f"나는 {age}살이며, {color}색을 좋아해요.")

# \n : 줄바꿈
print("줄바\n꿈")
# \", \' : 문장 내에서 ", ' 사용
print("저는 \"고용빈\"입니다.")
# \\ : 문장 내에서 \ 사용
print("C:\\Users\\Coding")
# \r : 커서를 맨앞으로 이동
print("Red Apple\rPine")
# \b : 한글자 삭제
print("Redd\bApple")
# \t : 탭
print("Red\tApple")