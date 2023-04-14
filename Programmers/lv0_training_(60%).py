# # 다항식 더하기  >>> fail
# poly = "3x + 7 + x"
# poly = poly.split(' ')
# answer = ''

# num = 0
# count = 0

# for i in range(len(poly)):
#     if 'x' in poly[i]:
#         if poly[i] == 'x':
#             count += 1
#         else:
#             count += int(poly[i][0])
#     elif poly[i].isdigit() == True:
#         num += int(poly[i])


# if num > 0 and count > 0:
#     answer = '%sx + %s' % (count, num) 
# elif count == 0:
#     answer = num
# elif num == 0:
#     answer = '%sx' % count

# print(answer)



# # 최빈값 구하기 
# array = [1, 1, 2, 2]
# array_dict = {}

# for i in range(len(array)):
#     array_dict[array[i]] = array.count(array[i])

# print(array_dict)

# if list(array_dict.values()).count(max(list(array_dict.values()))) > 1:
#     answer = -1
# else:
#     answer = [k for k, v in array_dict.items() if v == max(list(array_dict.values()))][0]

# print(answer)


# # 간단한 방법 >> 분석 필요
# while len(array) != 0:
#     for i, a in enumerate(set(array)):
#         array.remove(a)
#     if i == 0: 
#         answer = a
# answer = -1



# # OX퀴즈
# quiz = ["3 - 4 = -3", "5 + 6 = 11"]
# answer = []

# for i in quiz:
#     qli = i.split('=')
#     print(qli)
#     if eval(qli[0]) == int(qli[1]):
#         answer.append("O")
#     else:
#         answer.append("X")
    
# print(answer)