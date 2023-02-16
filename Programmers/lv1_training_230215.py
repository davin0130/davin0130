# # Collatz 의 논리 : "아래 작업을 반복하면 모든 수를 1로 만들 수 있다"
# # 수가 짝수면 2로 나누고, 홀수면 3을 곱하고 1을 더한다
# # 1이 될 때까지 반복한다. // 여기서의 조건은 500회까지만 한다.
# n = 16
# count = 0


# if n == 1:
#     count = 0
# else:
#     while count <= 500:
#         if count < 500:
#             if n == 1:
#                 break
#             elif n % 2 == 0:
#                 n = n/2
#                 count += 1
#             else:
#                 n = n*3 + 1
#                 count += 1
#         else:
#             count = -1
#             break
# print(count)


# # 리스트에서 특정 값 위치 찾기
# city = ["usa", "japan", "taiwan", "china", "france", "italy", "korea", "switzerland"]
# print("%s번째에 한국 있다" % str(city.index("korea")+1))


# # 배열 안에 특정 숫자로 나누어지는 값만 추출하여 정렬
# # 없을 경우 -1 
# array = [3,2,6]
# num = 5
# answer = []

# for i in array:
#     if i%num == 0:
#         answer.append(i)
# if len(answer) == 0:
#         answer.append(-1)
# answer.sort()
# print(answer)

# # 간단한 방법
# print(sorted([n for n in array if n%num == 0]) or [-1])


# # 전화번호 개인정보 유출 방지 : 마스킹 처리
# # 뒤 네자리 제외 모두 '*' 표시
# phone_number = "021234567"
# print("%s%s" % ("*"*(len(phone_number)-4), phone_number[-4:]))


# 배열에서 가장 작은 수 제거
# 만약 제거했을 때 배열에 아무것도 없다면 -1을 출력
# arr = [2,5,7,8,3]
# arr.pop(arr.index(min(arr)))
# if len(arr) == 0:
#     arr.append(-1)
# print(arr)
