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


