# 달리기 경주 (프로그래머스 1단계 문제)

def solution(players, callings):
    person = {}
    
    for idx, value in enumerate(players):
        person[value] = idx
    
    for call in callings:
        call_index = person[call]
        person[call] = call_index - 1
        person[players[call_index - 1]] = call_index
        players[call_index], players[call_index - 1] = players[call_index - 1], players[call_index]

    return players

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
print(["mumu", "kai", "mine", "soe", "poe"])
print(solution(players, callings))