# # 삼각형 출력
# n = int(input())
# for i in range(n):
#     print('*'*(i+1))


# # Let's Roll the Dice
# # 가로, 세로, 높이 박스 안에 최대한 많은 수의 주사위 담기
# box = [10, 8, 6]
# n = 3

# print((box[0]//n) * (box[1]//n) * (box[2]//n))


# # 리스트의 수 right/left 로 돌리기 
# numbers = [4, 455, 6, 4, -1, 45, 6]
# direction = "left"
# result = []

# if direction == "right":
#     for i in range(len(numbers)):
#         if i == 0:
#             result.append(numbers[len(numbers)-1])
#         else:
#             result.append(numbers[i-1])
# else:
#     for i in range(len(numbers)):
#         if i+1 == len(numbers):
#             result.append(numbers[0])
#         else:
#             result.append(numbers[i+1])
# print(result)

# # deque 모듈 사용하기**


# # 숫자 알파벳으로 변경
# age_dic ={0:'a', 1:'b', 2:'c', 3:'d', 4:'e', 5:'f', 6:'g', 7:'h', 8:'i', 9:'j'}
# age = 23

# for i in str(age):
#     print(age_dic[int(i)], end='')