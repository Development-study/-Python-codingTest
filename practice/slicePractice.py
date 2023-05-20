jumin = "990120-1234567"

print("성별 : " + jumin[7]) # 7번째 자리
print("생년 : " + jumin[0:2]) # 0 ~ 2 전까지
print("월 : " + jumin[2:4])
print("일 : " + jumin[4:6])
print("생년월일 : " + jumin[:6]) # 처음부터 6 전까지
print("뒤 7자리 : " + jumin[7:]) # 7번부터 끝까지 
print("뒤 7자리 (뒤에서부터) : " + jumin[-7:])