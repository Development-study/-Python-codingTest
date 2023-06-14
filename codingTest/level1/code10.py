# 신고 결과 받기 (프로그래머스 1단계 문제)

def solution(id_list, report, k):
    answer = []

    report_count = {id : 0 for id in id_list}

    report_set = set(report)
    for re in report_set:
        report_id = re.split(" ")[1]
        report_count[report_id] += 1

    stop = {}
    for key, v in report_count.items():
        if v >= k:
            stop[key] = v

    report_count.clear()
    report_count = {id : 0 for id in id_list}
    for re in report_set:
        reported_id, report_id = re.split(" ")
        if report_id in stop:
            report_count[reported_id] += 1

    answer = list(report_count.values())

    return answer

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2
print(solution(id_list, report, k))