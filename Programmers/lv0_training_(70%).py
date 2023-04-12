# # 7의 개수
# array = [10, 29]
# print(sum([str(i).count("7") for i in array]))


# # 영어가 싫어요 
# num = {
#     "one": 1, "two": 2, "three": 3, 
#     "four": 4, "five": 5, "six": 6, 
#     "seven": 7, "eight": 8, "nine": 9, 
#     "zero": 0
# }

# numbers = "onetwothreefourfivesixseveneightnine"
# string = ''
# answer = ''

# for i in range(len(numbers)):
#     string += numbers[i]
#     if string in num.keys():
#         print(string, num[string])
#         answer += str(num[string])
#         string = ''
#     print(string)

# print(int(answer))


# # 간단한 방법
# # enumerate() 함수 >> 인덱스와 원소로 이루어진 튜플을 생성해줌
# for num, eng in enumerate(["zero", "one", "two", 
# "three", "four", "five", 
# "six", "seven", "eight", "nine"]):
#     numbers = numbers.replace(eng, str(num))
# print(int(numbers))




# # 잘라서 배열로 저장하기
# import math
# my_str = "abc1Addfggg4556b"
# n = 6
# answer = []
# for i in range(math.ceil(len(my_str)/n)):
#     answer.append(my_str[i*n:(i+1)*n])

# print(answer)



# # 문자열 계산하기
# my_string = "3 + 7"

# my_string = my_string.split(' ')

# for i in range(len(my_string)):
#     print(i, my_string[i])
#     if my_string[i] == "+":
#         my_string[i] = 0
#     elif my_string[i] == "-":
#         my_string[i+1] = int(my_string[i+1])*(-1)
#         my_string[i] = 0
#     else:
#         my_string[i] = int(my_string[i])

# print(sum(my_string))

# # 간단한 방법
# print(eval(my_string))



# # 구슬을 나누는 경우의 수 >>> fail (시간초과.. )
# import itertools
# balls = 30
# share = 15

# bcs = list(itertools.combinations([i for i in range(balls)], share))

# print(len(bcs))



# # 삼각형의 완성조건(2)
# sides = [11, 7]
# answer = 0

# # 가장 긴 변이 나머지 하나인 경우
# for i in range(max(sides)+1, sum(sides)):
#     answer += 1
# # 가장 긴 변이 max(sides)인 경우 
# for i in range(max(sides)-min(sides)+1, max(sides)+1):
#     answer += 1

# print(answer)



# # 외계어 사전
# spell = ["z", "d", "x"]
# dic = ["def", "dww", "dzx", "loveaw"]

# spell.sort()

# for i in dic:
#     print(sorted(i))
#     if sorted(i) == spell:
#         print(1)
#         break
#     else:
#         print(2)



# 종이 자르기 
# 1*1 짜리로 자르기 위해 해야할 가위질
m = 3
n = 5

print((m-1) + m * (n-1))



# 캐릭터의 좌표
keyinput = ["left", "right", "up", "right", "right"]
board = [3, 9]
answer = [0, 0]
key = {"left": -1, "right": 1, "up":1, "down":-1}

print("최대 이동 가능 값 ", board[0]//2, board[1]//2)
w = board[0]//2
h = board[1]//2

r = key['right'] * keyinput.count('right')
l = key['left'] * keyinput.count('left')
u = key['up'] * keyinput.count('up')
d = key['down'] * keyinput.count('down')

print(r, l, u, d)

answer[0] = r + l
answer[1] = u + d

if abs(answer[0]) > w:
    if answer[0] < 0:
        answer[0] = (-1) * w
    else:
        answer[0] = w
elif abs(answer[1]) > h:
    if answer[1] < 0:
        answer[1] = (-1) * h
    else:
        answer[1] = h


print(answer)
