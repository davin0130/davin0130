# # 분수의 덧셈 >>> fail(테스트 케이스)
# numer1 = 1
# denom1 = 2
# numer2 = 3
# denom2 = 4

# j = numer1*denom2 + numer2*denom1
# m = denom1 * denom2

# print(j, m, j/m)

# jy = [i for i in range(2, j+1) if j%(i) == 0]
# my = [i for i in range(2, m+1) if m%(i) == 0]
# print(jy, my)

# gyo = set(jy) & set(my)
# print(gyo)

# for i in list(gyo):
#     j = int(j/i)
#     m = int(m/i)

# print([j, m])



# # 연속된 수의 합 >>> fail
# num = 5
# total = 15
# count = 0
# num_sum = 0

# while num_sum != total:
#     num_sum = num*count + sum(1, num-1)
#     print([i for i in range(count, count+num)], num*(count+1))
#     if num*(count+1) == total:
#         answer = [i for i in range(count, count+num)]
#         break
#     else:
#         num_sum = 0
#         count += 1
    
# print(answer)