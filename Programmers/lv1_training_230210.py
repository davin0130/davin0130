# # 짝수 홀수 알아보기
# num = 3
# print("Even" if num%2 == 0 else "Odd")

# # 자릿수 더하기
# n = 987
# answer = 0

# for i in range(len(str(n))):
#     answer += int(str(n)[i])
# print(answer)

# # 약수 모두 더하기
# n = 12
# answer = 0
# for i in range(n):
#     if n % (i+1) == 0:
#         answer += (i+1)
# print(answer)

# # 평균 구하기
# arr = [1,2,3,4]
# print(sum(arr)/len(arr))

# # 자연수 뒤집어 배열로 출력
# n = 12345
# answer = []
# for i in range(len(str(n))):
#     answer.append(int(str(n)[i]))
# answer.reverse()
# print(answer)

# # x, y 갯수 세어 같으면 True, 다르면 False
# # 대소문자는 구분하지 않음
# s = "xXoooyY"
# x_count = 0
# y_count = 0

# for i in s:
#     if "x" in i or "X" in i:
#         x_count += 1
#     elif "y" in i or "Y" in i:
#         y_count += 1

# if x_count == y_count:
#     print("True")
# else:
#     print("False")