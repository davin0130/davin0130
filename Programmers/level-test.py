# # level 2
# # 문제 1
# # 순간이동을 하면 건전지 사용량이 줄지 않지만, 
# # 앞으로 K 칸을 점프하면 K 만큼의 건전지 사용량이 듭니다.
# # 단, 건전지 사용량을 줄이기 위해 점프로 이동하는 것은 최소로 하려고 합니다. 
# # 거리 N이 주어졌을 때, 사용해야 하는 건전지 사용량의 최솟값을 return하는 solution 함수를 만들어 주세요.
# n = 6
# m = 1
# answer = 1

# # 1 0 0 2
# # 1 2 4 6 >> 3
# # 1 0 1 0
# # 1 2 3 6 >> 2
# # 3 0
# # 3 6

# while m != n:
#     if m < n and m*2 < n:
#         m *= 2
#     else:
#         m += 1
#         answer += 1
#     print(m, answer)



# # # 문제 2
# # import itertools
# # numbers = [4, 1, 2, 1]
# # target = 4

# # numbers = sorted(numbers)
# # print(numbers)



# level 3
# 문제 1
import itertools
sticker = [1, 3, 2, 5, 4]
# 0 1 2 3 4 


for i in range(len(sticker)):
    temp = [i for i in sticker]
    print(temp[i-1], temp[i], temp[i+1])
    temp.pop(i-1)
    if i == len(sticker)-2:
        temp.pop(0)
    else:
        temp.pop(i+1)
    print(temp)
    tc2 = itertools.combinations(temp, 2)
    templist = [sum(i) for i in list(tc2)]
    print(max(templist), templist)
    print('===')