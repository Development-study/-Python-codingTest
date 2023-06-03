def solution(my_string, overwrite_string, s):
    answer = ''
    print(my_string[s:len(overwrite_string)])
    answer = my_string.replace(my_string[s:len(overwrite_string)], overwrite_string)
    return answer

print(solution("He11oWor1d", "lloWorl", 2))