# 정답률 60%대 문제

# # 비밀지도 / "#"=1, " "=0 
# n = 5
# arr1 = [9, 20, 28, 18, 11]
# arr2 = [30, 1, 21, 17, 28]
# answer1 = []
# answer2 = []
# result = []

# for i in range(len(arr1)):
#     arr1[i] = format(arr1[i], 'b').zfill(n)
# for i in range(len(arr2)):
#     arr2[i] = format(arr2[i], 'b').zfill(n)

# for i in arr1:
#     count = ""
#     for j in i:
#         if j == "0":
#             j = " "
#         else:
#             j = "#"
#         count += j
#     answer1.append(count)
# for i in arr2:
#     count = ""
#     for j in i:
#         if j == "0":
#             j = " "
#         else:
#             j = "#"
#         count += j
#     answer2.append(count)

# for i in range(len(answer1)):
#     count = ''
#     for j in range(len(answer1)):
#         if answer1[i][j] == answer2[i][j]:
#             count += answer1[i][j]
#         else:
#             count += "#"
#     result.append(count)
# # 크기가 작은 부분문자열 
# t = "500220839878"
# p = "7"
# result = 0

# for i in range(len(t)-len(p)+1):
#     num = t[i:i+len(p)]
#     if int(num) <= int(p):
#         result += 1

# print(result)



# # 이중 배열 매핑하기
# array = [1, 5, 2, 6, 3, 7, 4]
# commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
# answer = []

# print(sorted(array[1:5])[2])
# print(sorted(array[3:4])[0])
# print(sorted(array[0:7])[2])
# for i in range(len(commands)):
#     answer.append(sorted(array[commands[i][0]-1:commands[i][1]])[commands[i][2]-1])
# print(answer)

# # 간단한 방법
# print([sorted(array[commands[i][0]-1:commands[i][1]])[commands[i][2]-1] for i in range(len(commands))])

# # 더 간단한 방법
# print(list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands)))



# #  >>>>> fail
# numbers = [5,0,2,7]
# result = []
# 0+1
# 0+2
# 0+3
# 1+2
# 1+3
# 2+3
# for i in range(len(numbers)):
#     for j in range(len(numbers)-i):
#         if i == len(numbers)-1:
#             result.append(numbers[i])
#         else:
#             result.append(numbers[i] + numbers[i+j])
# result.sort()
# print(list(set(result)))




# 콜라 문제 
# 정답은 아무에게도 말하지 마세요.
# 콜라 빈 병 2개를 가져다주면 콜라 1병을 주는 마트가 있다. 빈 병 20개를 가져다주면 몇 병을 받을 수 있는가?
# 단, 보유 중인 빈 병이 2개 미만이면, 콜라를 받을 수 없다.
empt_coke = 10
change_coke = 2
my_coke = 50
new_coke = 0
answer = 0


while my_coke//empt_coke != 0:
    new_coke += my_coke//empt_coke * change_coke
    my_coke -= my_coke//empt_coke * empt_coke
    answer += new_coke

    my_coke += new_coke
    new_coke = 0
    answer += new_coke
    print("my_coke = ", my_coke)
    print("new_coke = ", new_coke)
    print("answer = ", answer)


# print("처음")
# print("my_coke = ", my_coke)
# print("new_coke = ", new_coke)

# print("두번째")
# new_coke += my_coke//empt_coke
# my_coke -= new_coke * empt_coke
# answer += new_coke
# print("my_coke = ", my_coke)
# print("new_coke = ", new_coke)
# print("answer = ", answer)

# print("두번째 정리")
# my_coke += new_coke
# new_coke = 0
# answer += new_coke
# print("my_coke = ", my_coke)
# print("new_coke = ", new_coke)
# print("answer = ", answer)

# print("세번째")
# new_coke += my_coke//empt_coke
# my_coke -= new_coke * empt_coke
# answer += new_coke
# print("my_coke = ", my_coke)
# print("new_coke = ", new_coke)
# print("answer = ", answer)

# print("세번째 정리")
# my_coke += new_coke
# new_coke = 0
# answer += new_coke
# print("my_coke = ", my_coke)
# print("new_coke = ", new_coke)
# print("answer = ", answer)


# print("네번째")
# new_coke += my_coke//empt_coke
# my_coke -= new_coke * empt_coke
# answer += new_coke
# print("my_coke = ", my_coke)
# print("new_coke = ", new_coke)
# print("answer = ", answer)

# print("네번째 정리")
# my_coke += new_coke
# new_coke = 0
# answer += new_coke
# print("my_coke = ", my_coke)
# print("new_coke = ", new_coke)
# print("answer = ", answer)



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
