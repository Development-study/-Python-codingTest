# def solution(s, N):
#     answer = 0

#     fan_digital = -1

#     for i in range(len(s)):
#         sub_string = s[i:i + N]

#         if len(sub_string) < N:
#             break

#         check = True
#         for j in range(0, N):
#             if int(sub_string.count(str(j + 1))) > 1:
#                 check = False
#                 break

#             if int(sub_string[j]) > N:
#                 check = False
#                 break

#         if check:
#             if fan_digital < int(sub_string):
#                 fan_digital = int(sub_string)

#     return fan_digital

# def solution(s, N):
#     if len(s) < N:
#         return -1

#     stylish_fans = []
#     for i in range(len(s) - N + 1):
#         substring = s[i:i+N]
#         if is_stylish_fan(substring, N):
#             stylish_fans.append(int(substring))

#     if not stylish_fans:
#         return -1

#     return max(stylish_fans)


# def is_stylish_fan(substring, N):
#     digits = set()
#     for digit in substring:
#         if digit in digits or int(digit) > N:
#             return False
#         digits.add(digit)

#     return len(digits) == N

# def solution(s, N):
#     if len(s) < N:
#         return -1

#     stylish_fans = []
#     digits = [str(i) for i in range(1, N + 1)]

#     for i in range(len(s) - N + 1):
#         substring = s[i:i+N]
#         if "".join(sorted(substring)) == "".join(digits):
#             stylish_fans.append(int(substring))

#     if not stylish_fans:
#         return -1

#     return max(stylish_fans)

# print(solution("1451232125", 2))

def solution(relationships, target, max_step):
    money = 0
    new_friend_count = 0

    friends_dict = {}
    friends = []
    new_friends = []
    for relationship in relationships:
        if target in relationship:
            friends_dict[relationship[0] if relationship.index(target) != 0 else relationship[1]] = 1
            friends.append(relationship)
        else:
            new_friends.append(relationship)

    for new in new_friends:
        if new[0] in friends_dict.keys():
            if friends_dict[new[0]] <= max_step:
                friends_dict[new[1]] = friends_dict[new[0]] + 1
        elif new[1] in friends_dict.keys():
            if friends_dict[new[1]] <= max_step:
                friends_dict[new[0]] = friends_dict[new[1]] + 1
    
    new_friends.clear()
    for friend, step in friends_dict.items():
        if step <= max_step and step != 1:
            new_friends.append(friend)

    new_friend_count = len(new_friends)
    money = (len(friends) * 5) + (new_friend_count * 10)

    return new_friend_count + money



relationships = [[1, 2], [2, 3], [2, 6], [3, 4], [4, 5]]
target = 2
limit = 3
print(solution(relationships, target, limit))