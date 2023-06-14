# 추억 점수 (프로그래머스 1단계 문제)

def solution(name, yearning, photo):
    answer = []

    score = 0
    for p in photo:
        for n in p:
            if name.count(n) == 0:
                continue
            p_index = name.index(n)
            score += yearning[p_index]
        
        answer.append(score)
        score = 0

    return answer

name = ["may", "kein", "kain", "radi"]
yearning = [5, 10, 1, 3]
photo = [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]
print(solution(name, yearning, photo))