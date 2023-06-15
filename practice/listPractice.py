# 리스트

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석", "조세호", "박명수"]
# print(subway)

# print(subway.index("조세호"))

# # 리스트 젤 뒤에 요소 넣기
# subway.append("하하")
# print(subway)

# # 리스트 원하는 위치에 요소 넣기
# subway.insert(1, "정형돈")
# print(subway)

# # 리스트에서 마지막 요소 제거
# print(subway.pop())
# print(subway)

# subway.append("유재석")
# print(subway.count("유재석"))

# num_list = [5, 4, 1, 2, 3]

# # 정렬
# num_list.sort()
# print(num_list)

# # 순서 뒤집기
# num_list.reverse()
# print(num_list)

# # 비우기
# num_list.clear()
# print(num_list)

# mix_list = ["조세호", 20, True]
# print(mix_list)

# # 리스트 합치기
# num_list = [5, 4, 1, 2, 3]
# num_list.extend(mix_list)
# print(num_list)

test = [[2, 1, 4], [2, 3, 1], [3, 2, 1]]
d = sorted(test, key=lambda x : (x[0], x[1], -x[2]))
print(d)