# 집합 (set)

my_set = {1, 2, 3, 3, 3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java, python 모두)
print(java & python)
print(java.intersection(python))

# 합집합 (java 또는 python)
print(java | python)
print(java.union(python))

# 차집합 (java는 가능하지만 python은 안되는)
print(java - python)
print(java.difference(python))

# 추가
python.add("김태호")
print(python)

# 삭제
java.remove("김태호")
print(java)