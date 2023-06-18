# 의상 (프로그래머스 2단계 문제)

def solution(clothes):
    hash_map = {key: 0 for _, key in clothes}
    for _, type in clothes:
        hash_map[type] += 1
        
    answer = 1
    for size in hash_map.values():   
        answer *= (size + 1)
    
    return answer - 1