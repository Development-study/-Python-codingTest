# 카카오 2018 공채 문제 4번
# 셔틀버스 (난이도 : 중)

def solution(n, t, m, timetable):
    timetable = sorted([int(i[:2]) * 60 + int(i[3:]) for i in timetable])
    
    con_time = 540
    suttle_time = 540

    for i in range(n):
        for j in range(m):
            if timetable and timetable[0] <= suttle_time:
                con_time = timetable.pop(0) - 1
            else:
                con_time = suttle_time
        suttle_time += t
    
    return f'{str(con_time//60).zfill(2)}:{str(con_time%60).zfill(2)}'

n = 1
t = 1
m = 5
timetable = ['08:00', '08:01', '08:02', '08:03']
print(solution(n, t, m, timetable))