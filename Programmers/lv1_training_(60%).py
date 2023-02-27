# # 크기가 작은 부분문자열 
# t = "500220839878"
# p = "7"
# result = 0

# for i in range(len(t)-len(p)+1):
#     num = t[i:i+len(p)]
#     if int(num) <= int(p):
#         result += 1

# print(result)


# # 소수 만들기
# import itertools

# nums = [1,2,7,6,4]
# nCr = itertools.combinations(nums, 3)

# result = 0

# for i in list(nCr):
#     count = 0
#     for j in range(sum(i)):
#         if sum(i) % (j+1) == 0:
#             count += 1
#     if count == 2:
#         result += 1
# print(result)



# # 소수 찾기   >>>>> fail
# n = 1000000
# answer = 0

# for i in range(n):
#     count = 0
#     for j in range(i+1):
#         if (i+1) % (j+1) == 0:
#             count += 1
#     if count == 2:
#         answer += 1
# print(answer)



# # 가장 가까운 같은 글자
# s = "banana"
# s_list = []
# result = []

# for i in range(len(s)):
#     if s[i] not in s_list:
#         result.append(-1)
#         s_list.append(s[i])
#     else:
#         print(s.index(s[i]), s_list.index(s[i]))
#         s_list.append(s[i])
#         result.append(s.index(s[i])-s_list.index(s[i], -1))
#     print(s_list, result)



# # 모의고사
# answers = [1,2,3,4,5]
# return_v = []

# a_1 = [1,2,3,4,5]
# a_2 = [2,1,2,3,2,4,2,5]


# 폰켓몬 
import itertools

nums = [3,1,2,3]
nPr = itertools.permutations(nums, 3)

print(set(list(nPr)[4]))