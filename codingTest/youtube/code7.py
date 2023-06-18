# 카카오 2018 공채 문제 5번
# 뉴스 클러스터링 (난이도 : 중)

import re

def solution(str1, str2):
    if len(str1) <= 1 and len(str2) <= 1:
        return 65536
    str1 = str1.lower()
    str2 = str2.lower()

    str1List = []
    str2List = []

    pattern = re.compile(r'[a-z]{2}')

    for i in range(len(str1) - 1):
        str = str1[i]+str1[i+1]
        if pattern.findall(str):
            str1List.append(str)

    for i in range(len(str2) - 1):
        str = str2[i]+str2[i+1]
        if pattern.findall(str):
            str2List.append(str)

    intersection = set(str1List) & set(str2List)
    combination = set(str1List) | set(str2List)

    intersection_plus = 0
    combination_plus = 0

    for i in intersection:
        if str1List.count(i) > 1 and str2List.count(i) > 1:
            if str1List.count(i) > str2List.count(i):
                intersection_plus += str2List.count(i) - 1
            else:
                intersection_plus += str1List.count(i) - 1

    for i in combination:
        if str1List.count(i) > 1 or str2List.count(i) > 1:
            if str1List.count(i) > str2List.count(i):
                combination_plus += str1List.count(i) - 1
            else:
                combination_plus += str2List.count(i) - 1

    if (len(intersection) + intersection_plus) == 0:
        return 65536
    if (len(combination) + combination_plus) == 0:
        return 0

    return int((len(intersection) + intersection_plus) / (len(combination) + combination_plus) * 65536)

str1 = "FRANCE"
str2 = "french"

print(solution(str1, str2))