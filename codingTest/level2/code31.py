# 오픈채팅방 (프로그래머스 2단계 문제)

def solution(record):
    answer = []
    
    uidList = {}
    messageList = ([0] * len(record))
    for i in range(len(record)):
        userData = record[i].split(" ")
        
        if userData[0] == "Enter":
            uidList[userData[1]] = userData[2]
            messageList[i] = [userData[1], "님이 들어왔습니다."]
        elif userData[0] == "Leave":
            messageList[i] = [userData[1], "님이 나갔습니다."]
        elif userData[0] == "Change":
            uidList[userData[1]] = userData[2]
        
    for message in messageList:
        if not message == 0:
            answer.append(uidList[message[0]] + message[1])
    
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))