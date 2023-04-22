# 정답률 50%대 문제

# # 과일 장수
# k = 3
# m = 4
# count = 0
# score = [1, 2, 3, 1, 2, 3, 1]
# sort_scr = sorted(score, reverse=True)

# for i in range(len(score)//m):
#     count += min(sort_scr[m*i:m*i+m])*m

# print(count)


# # 간단한 방법
# print(sum(sorted(score)[len(score)%m::m])*m)


# # 체육복
# n = 5
# lost = [2, 4]
# reserve = [1, 3, 5]

# answer = n - len(lost)
# print(answer)

# for i in range(len(lost)):
#     if lost[i]-1 in reserve:
#         print(lost[i]-1, reserve)
#         reserve.pop(reserve.index(lost[i]-1))
#         answer += 1
#     elif lost[i]+1 in reserve:
#         print(lost[i]+1, reserve)
#         reserve.pop(reserve.index(lost[i]+1))
#         answer += 1

#     print(answer, reserve)

# print(answer)



# # 로또 확률 구하기 >>>> fail
# lotto_dict ={6:1, 5:2, 4:3, 3:4, 2:5, 0:6}
# lottos = [46, 1, 32, 10, 5, 7]
# win_nums = [20, 9, 3, 45, 4, 35]

# result = []

# min_rank = set(lottos).intersection(win_nums)

# print(min_rank)
# print(len(min_rank))
# print(lottos.count(0))
# print(lotto_dict[len(min_rank)+lottos.count(0)])
# print(lotto_dict[len(min_rank)])
# result.append(lotto_dict[len(min_rank)+lottos.count(0)])
# result.append(lotto_dict[len(min_rank)])

# print(result)



# 기사 단원의 무기 
number = 5
limit = 3
power = 2
result = 10

answer = 0
num_list = []

# for i in range(1, number+1):
#     count = 0
#     for j in range(1, i+1):
#         if i%j == 0:
#             count += 1
#     num_list.append(count)

# for i in range(len(num_list)):
#     if num_list[i] > limit:
#         num_list[i] = power

# print(num_list)
# print(sum(num_list))


for i in range(1, number+1):
    if (i ** 1/2) == int(i ** 1/2):
        print(i ** 1/2)