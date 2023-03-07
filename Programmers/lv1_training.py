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

# # 정수와 자연수를 입력받아 정수부터 정수만큼 차이나는 수가 자연수 만큼 있는 리스트 출력
# x = 10000000
# n = 1000

# print(list(range(x, x*(n+1), x)))

# # 문자열 정수로 변경
# string = '-1234'
# print(int(string))

# # 내림차순으로 변경
# n = 118372
# answer = []
# for i in str(n):
#     answer.append(int(i))
# answer.sort()
# answer.reverse()
# for i in answer:
#     print(i, end='')

# # 더 간단한 방법 (sort 함수에 reverse=True 설정)
# ls = list(str(n))
# ls.sort(reverse = True)
# print(int("".join(ls)))

# # 나머지 1인 최소값 출력
# n = 10
# answer = []
# for i in range(n):
#     if n%(i+1) == 1:
#         answer.append(i+1)

# print(min(answer))

# # 더 간단한 방법 | 한번에 출력
# print([x for x in range(1,n+1) if n%x==1][0])


# # 두 정수 사이 값의 합 출력
# a=3
# b=3
# min = min(a,b)
# max = max(a,b)
# for i in range(min, max):
#     min += i+1

# print(min)

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


# # 중간 글자 출력
# s = "qwer"

# if len(s)%2 == 0:
#     print(s[int(len(s)/2)-1:int(len(s)/2)+1])
# else:
#     print(s[int(len(s)/2)-1:int(len(s)/2)])


# # 입력한 수만큼 글 출력
# text = "거북이"
# n = int(input("수 입력: "))
# answer = ''

# for i in range(n):
#     if i == 0:
#         answer += text[0]
#     else:
#         answer += text[i%len(text)]
# print(answer)

# # 간단한 방법!
# answer = ''
# answer = '거북이'*n
# print(answer[:n])


# # 없는 수 더하기
# numbers = [1,2,3,7,8,0]
# print(45-sum(numbers))


# # true/false : 양수/음수 처리
# true = 1
# false = -1
# absolutes = [4,7,12]
# signs = [true,false,true]

# for i in range(len(signs)):
#     absolutes[i] *= signs[i]

# print(sum(absolutes))


# # 두 리스트의 곱의 합
# a = [-1,0,1]
# b = [1,0,-1]
# answer = 0

# for i in range(len(a)):
#     answer += a[i] * b[i]
# print(answer)

# # 간단한 방법
# print(sum([a[i]*b[i] for i in range(len(a))]))

# # 더 간단한 방법
# print(sum([x*y for x, y in zip(a,b)]))


# # 문자열 내림차순으로 출력
# s = "sbecfss"
# answer = []
# result = ''
# for i in s:
#     answer.append(ord(i))

# answer.sort(reverse=True)
# for i in answer:
#     result += chr(i)
# print(result)

# # 간단한 방법
# print(''.join(sorted(s, reverse=True)))


# # 약수 개수 합
# left = 13
# right = 17
# diff= right - left
# diff_list = []
# for i in range(diff+1):
#     num = i+left
#     count = 0
#     for j in range(num):
#         if num%(j+1) == 0:
#             count += 1
#     if count % 2 == 0:
#         diff_list.append(num)
#     else:
#         diff_list.append(num * (-1))
# print(sum(diff_list))


# # 문자열 내 숫자 여부 판별 + 길이 확인
# a = "12109ue923434"

# print([i.isdigit() for i in a])
# if len(a) == 4 or len(a) == 6:
#     if False in [i.isdigit() for i in a]:
#         print("false")
#     else:
#         print("true")
# else:
#     print("false")

# # 간단한 방법
# print(a.isdigit() and len(a) in [4,6])


# # 남은 돈 계산 >>> fail
# price = 3 
# money = 20
# count = 20
# now_price = 0

# for i in range(count):
#     now_price = price * (i+1)
#     money -= now_price
#     print(now_price, money)

# if money >=0:
#     print(money)
# else:
#     print(money * -1)


# # 행렬의 각 자릿수 더하기
# arr1 = [[1,2],[2,3]]
# arr2 = [[3,4],[5,6]]

# # for in zip 함수를 이용해 리스트의 값을 각각 더해줌
# # 이중 행렬이므로 2번 활용
# answer = [[x+y for x, y in zip(a, b)] for a, b in zip(arr1, arr2)]



# # 가로세로 원하는 만큼 찍기
# n = '8 2'
# answer = ''

# for i in range(int(n[2])):
#     print('x' * int(n[0]))

# # 간단한 방법
# a, b = map(int, n.strip().split(' '))
# [print('x' * a) for i in range(b)]


# # 최대공약수 최소공배수 >>>> fail 
# n = 8
# m = 3
# meas = []
# drai = 1

# print(max(n,m), min(n,m))
# # 12 3
# # 12 약수 [1, 2, 3, 4, 6, 12]
# # 3 약수  [1, 3]
# # 최대공약수 3

# for i in range(max(n, m)):
#     meas_val = max(n, m)%(i+1)
#     if meas_val == 0:
#         if (i+1) <= min(n, m) and min(n,m)%(i+1) == 0:
#             meas.append(i+1)
# if max(n, m)%min(n, m) == 0:
#     drai = max(n, m)
# else:
#     drai = n * m
# print(meas)
# print(max(meas))
# print(drai)


# # 연속되는 중복 수 제거
# arr = [4,4,4,3,3,2,2,4,4,3,3,2,1,5,6,7]
# answer = []

# for i in range(len(arr)):
#     # 조건1 : 가장 첫번째 수의 경우 리스트에 추가
#     # 조건2 : 연속없는 리스트의 가장 마지막 수가 현재 수와 다른 경우만 추가
#     if len(answer) == 0 or answer[-1] != arr[i]:
#         answer.append(arr[i])
# print(answer)


# # 대소문자 바꾸기 >>>> fail
# string = "try hello world"
# str_list = string.split(' ')
# print(str_list)
# new_string = ''

# for i in str_list:
#     for j in range(len(i)):
#         if (j+1)%2 != 0:
#             new_string += i[j].upper()
#         else:
#             new_string += i[j]
#     new_string += ' '
# print(new_string)






# # 정해진 예산에서 최대 부서 지원하기
# d = [1,3,2,5,4]
# budget = 9
# count = 0

# for i in range(len(d)):
#     if sum(sorted(d)[0:i+1]) <= budget:
#         print(sorted(d)[0:i+1], sum(sorted(d)[0:i+1]))
#         count += 1
# print(count)
    

# # >>> fail
# sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
# answer = 0

# w = list(zip(*sizes))[0]
# h = list(zip(*sizes))[1]

# max_size = max(max(w),max(h))
# max_match = h[w.index(max_size)]


# # 숫자 문자열과 영단어  >>>> fail
# alp_dict = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
# num_dict = {v:k for k,v in alp_dict.items()}
# b_answer =[]

# s = "23four5six7"
# answer = ''
# for i in range(len(s)):
#     string = ''
#     if s[i].isdigit() == True:
#         b_answer.append(s[i])
#     else:
#         for i in range(9):
#             if num_dict.get(i) in s:
#                 b_answer.append(str(alp_dict.get(num_dict.get(i))))

# print(b_answer)
# # for i in range(9):
# #     if num_dict.get(i) in s:
# #         answer += str(alp_dict.get(num_dict.get(i)))
# # print(answer)
# # if num_dict in s:
# #     print(num_dict)