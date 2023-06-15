# 광물 캐기 (프로그래머스 2단계 문제)

def solution(picks, minerals):
    # 캘 수 있는 광물의 개수
    minerals = minerals[:sum(picks) * 5]
        
    # 광물 조사
    cnt_min = [[0, 0, 0]for x in range(10)] # dia, iron, stone
    for i in range(len(minerals)):
        if minerals[i] == 'diamond': 
            cnt_min[i//5][0] += 1
        elif minerals[i] == 'iron': 
            cnt_min[i//5][1] += 1
        else : 
            cnt_min[i//5][2] += 1

    # 피로도가 높은 순서대로 광물 정렬
    sorted_cnt_min = sorted(cnt_min, key = lambda x: (-x[0], -x[1], -x[2]))
    
    # 피로도 계산
    answer = 0
    for mineral in sorted_cnt_min:
        d, i, s = mineral
        for p in range(len(picks)):
            if p == 0 and picks[p]>0: # dia 곡괭이
                picks[p]-=1
                answer += d + i + s
                break
            elif p == 1 and picks[p]>0: # iron 곡괭이
                picks[p]-=1
                answer += 5*d + i + s
                break
            elif p == 2 and picks[p]>0: # stone 곡괭이
                picks[p]-=1
                answer += 25*d + 5*i + s
                break
                
    return answer

picks = [1, 3, 2]
minerals = ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"]

print(solution(picks, minerals))

# 일단 가지고 있는 곡갱이를 사용하여 모든 광물을 캘 수 있는지 체크합니다.
# 1) 모두 캘 수 없는 경우 : minerals를 캘 수 있는 만큼의 자원까지만 자릅니다. ex) minerals[:5 * sum(picks)]
# 2) 모두 캘 수 있는 경우 : minerals를 그대로 들고 갑니다.

# 자원을 5개 단위로 나누어 그 묶음을 다이아 곡갱이로 캘 때, 철 곡갱이로 캘 때, 돌 곡갱이로 캘 때 피로도를 계산하여 리스트로 따로 저장해줍니다. 
# [다이아 곡갱이로 5개를 다 캘 때 피로도, 철 곡갱이로 다 캘 때 피로도, 돌 곡갱이로 다 캘 때 피로도]를 저는 info라는 리스트에 넣어줬습니다. 
# 이 것을 minerals의 끝까지 돌려줍니다. -> 첫 번째 예시의 경우 info = [[5, 17, 85], [3, 7, 31]] 이런 식으로 넣어집니다.

# 리스트 안의 값을 보았을 때 돌 곡갱이로 캘 때 피로도가 제일 큰 값인 경우 -> 다이아 곡갱이로 캐는 게 효율이 좋습니다.
# 위의 예시로 보면 info에 첫 번째 묶음은 [5,17,85]이고 두 번째 묶음은 [3,7,31]인데 첫 번째 묶음의 경우 돌 곡갱이로 캐는 경우
# 피로도가 85이므로 가지고 있는 가장 좋은 곡갱이로 캐는 게 효율이 좋습니다. 
# 이를 한번의 알 기 위해 info 리스트를 돌 곡갱이 피로도, 철 곡갱이 피로도, 다이아 곡갱이 피로도 순으로 info를 정렬을 해줍니다.

# 정렬된 info 리스트를 뒤에서부터 pop 해오면서 가지고 있는 가장 좋은 곡갱이들부터 차례로 사용하면서 피로도를 계산해줍니다.