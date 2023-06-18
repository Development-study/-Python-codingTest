# 기능 개발 (프로그래머스 2단계 문제)

from math import ceil

def solution(progresses, speeds):
    progresses = [ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
    answer = []
    front = 0
    
    for idx in range(len(progresses)):
        if progresses[idx] > progresses[front]:  
            answer.append(idx - front)
            front = idx 
    answer.append(len(progresses) - front)  

    return answer