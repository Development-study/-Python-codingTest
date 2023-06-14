def solution(my_string, overwrite_string, s):
    answer = ''
    answer = my_string.replace(my_string[s:len(overwrite_string) + s], overwrite_string)
    return answer

print(solution("He11oWor1d", "lloWorl", 2))