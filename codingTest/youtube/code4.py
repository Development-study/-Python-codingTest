# 카카오 2018 공채 문제 2번
# 다트 게임 (난이도 : 하)

import re

def solution(dartResult):
    answer = []
    pattern = re.compile(r'([0-9]|10)([SDT])([\*\#]?)')
    calculation = {
        'S': lambda v:v,
        'D': lambda v:v**2,
        'T': lambda v:v**3
    }

    score = 0
    for num, i, j in pattern.findall(dartResult):
        if i == 'S':
            score = calculation['S'](int(num))
        elif i == 'D':
            score = calculation['D'](int(num))
        elif i == 'T':
            score = calculation['T'](int(num))
        if j == '*':
            score *= 2
            if answer:
                answer[-1] *= 2
        elif j == '#':
            score *= -1
        
        answer.append(score)

    return sum(answer)

print(solution('1S2D*3T'))