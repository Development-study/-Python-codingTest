# 사전

cabinet = {
    3: "유재석",
    100: "김태호"
}

# [], .get()에서 키 값으로 값 가져오기
print(cabinet[3])
print(cabinet.get(100))
print(cabinet.get(5, "사용 가능"))

# in 사전에 값이 있는지 확인
print(3 in cabinet)
print(5 in cabinet)

cabinet = {
    "A-3": "유재석",
    "B-100": "김태호"
}

print(cabinet["A-3"])

# 값 넣기 (존재하면 덮어쓰기)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 값 빼기
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())
# value들만 출력
print(cabinet.values())
# key, value 함께 출력
print(cabinet.items())

# 비우기
cabinet.clear()
print(cabinet)