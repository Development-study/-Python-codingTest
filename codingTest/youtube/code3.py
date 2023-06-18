# 카카오 2018 공채 문제 1번
# 비밀 지도 (난이도 : 하)

arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
n = 5

for i, j in zip(arr1, arr2):
    print(bin(i | j)[2:].zfill(n).replace('1', '#').replace('0', ' '))