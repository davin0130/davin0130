# 최댓값 만들기(2)
# from itertools import permutations, combinations
# from functools import reduce

# numbers = [10, 20, 30, 5, 5, 20, 5]
# re_list = []
# result = 0

# # 조합 : 중복을 허용하지 않고 2개의 값을 뽑음
# nc2 = list(combinations(numbers, 2))

# # 각 튜플의 곱셈을 리스트에 추가
# for i in nc2:
#     re_list.append(reduce(lambda x, y: x*y, i))

# # 가장 큰 값 출력
# print(max(re_list))

# # 더 쉬운 방법
# numbers = [10, 20, 30, 5, 5, 20, 5]

# print(sorted(numbers)[-1] * sorted(numbers)[-2])



# # 인덱스 바꾸기 >>> fail
# my_string = "I love you"
# num1 = 3
# num2 = 6

# print(my_string[num1])
# print(my_string[num2])

# my_string[num1] = my_string[num2]
# print(my_string)



# # 가장 큰 수 찾기
# array = [9, 10, 11, 8]

# list에서 가장 큰 값 찾기, 그 값의 인덱스 구하기 >> list로 묶어주기
# print([max(array), array.index(max(array))])



# # 피자 나눠 먹기 
# # 6과 n의 최소공배수
# n = 10
# pizza_piece = 0

# for i in range(max(6, n), (6*n)+1):
#     if i%6==0 and i%n == 0:
#         pizza_piece = i
#         break

# # 한 판에 6조각이므로 피자는 조각 수 * 6
# print(pizza_piece / 6)


# # 369게임
# order = 29423
# answer = 0

# for i in range(len(str(order))):
#     if "3" in str(order)[i] or "6" in str(order)[i] or "9" in str(order)[i]:
#         answer += 1

# print(answer)

# # 더 쉬운 방법 
# order = str(order)
# print(sum([order.count('3'), order.count('6'), order.count('9')]))



# # 약수 구하기 
# n = 29
# answer = []

# for i in range(1, n+1):
#     if n % i == 0:
#         answer.append(i)
# print(answer)


# 숫자 찾기
num = 123456
k = 7

num = str(num)
k = str(k)

if k in num:
    print(str(num).index(str(k))+1)
else:
    print(-1)