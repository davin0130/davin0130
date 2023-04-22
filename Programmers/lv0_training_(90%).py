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


# # 조건에 맞게 수열 변환
# # k가 짝수면 arr 각 원소에 더하기 k
# # k가 홀수면 arr 각 원소에 곱하기 k
# arr = [1, 2, 3, 100, 99, 98]
# k = 3
# answer = [i+k if k%2==0 else i*k for i in arr]

# print(answer)



# # n의 배수
# # num이 n의 배수이면 1 아니면 0
# num = 98
# n = 2

# print(1 if num%n==0 else 0)



# # 문자열 곱하기
# my_string = "string"
# k = 3

# print(my_string * k)



# n번째 원소까지
num_list = [2, 1, 6]
n = 1
print(num_list[:n])