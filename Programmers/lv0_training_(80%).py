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


# # 숫자 찾기
# num = 123456
# k = 7

# num = str(num)
# k = str(k)

# if k in num:
#     print(str(num).index(str(k))+1)
# else:
#     print(-1)



# # 문자열 정렬하기 
# my_string = "heLLo"
# my_string = sorted([i for i in my_string.lower()])
# answer = ''

# for i in my_string:
#     answer += i

# print(answer)

# # 간단한 방법
# print(''.join(sorted(my_string.lower())))



# # 합성수(약수가 3개 이상인 수) 찾기 
# n = 15
# answer = 0

# for i in range(1, n+1):
#     count = 0
#     for j in range(1, i+1):
#         if i%j == 0:
#             count += 1
#     if count >= 3:
#         answer += 1

# print(answer)


# # 중복된 문자 제거
# my_string = "We are the world"
# answer = ""

# for i in my_string:
#     if i not in answer:
#         answer += i
#         print(answer)

# # 간단한 방법
# print(''.join(dict.fromkeys(my_string)))



# # 모스부호(1)
# morse = { 
#     '.-':'a','-...':'b','-.-.':'c','-..':'d','.':'e','..-.':'f',
#     '--.':'g','....':'h','..':'i','.---':'j','-.-':'k','.-..':'l',
#     '--':'m','-.':'n','---':'o','.--.':'p','--.-':'q','.-.':'r',
#     '...':'s','-':'t','..-':'u','...-':'v','.--':'w','-..-':'x',
#     '-.--':'y','--..':'z'
# }

# letter = ".... . .-.. .-.. ---"
# letter = letter.split(' ')
# letter = [morse[i] for i in letter]
# print(''.join(letter))



# # A로 B 만들기
# before = "hello"
# after = "olleh"
# answer = 1

# before = [i for i in before]
# after = [i for i in after]
# for i in range(len(before)):
#     if before[i] in after:
#         after.pop(after.index(before[i]))
#         print(before, after)
#     else:
#         answer = 0
#         break

# print(answer)


# # 간단한 방법
# # sort 후 똑같은지 비교.. 
# if sorted(before) == sorted(after):
#     answer = 1
# else:
#     answer = 0
# print(answer)



# # 팩토리얼  >>> fail
# n = 3628800
# count = 0
# answer = 1
# while answer <= n:
#     for i in range(1, count+1):
#         answer *= i
#         print(i, answer)
#     count += 1
#     print(answer, count)
#     print('---')


# # 2차원으로 만들기
# num_list = [100, 95, 2, 4, 5, 6, 18, 33, 948]
# n = 3
# answer = []

# for i in range(int(len(num_list)/n)):
#     answer.append(num_list[i*n:i*n+n])

# print(answer)



# # k의 개수
# i = 1
# j = 13
# k = 1
# answer = 0


# for x in range(i, j+1):
#     if str(k) in str(x):
#         answer += str(x).count(str(k))
        
# print(answer)

# # 간단한 방법
# print(sum([str(i).count(str(k)) for i in range(i,j+1)]))



# # 가까운 수
# array = [11, 5, 28]
# n = 8
# answer = []

# array = sorted(array)

# for i in array:
#     answer.append(abs(i-n))

# print(answer)
# print(array[answer.index(min(answer))])



# # 진료 순서 정하기 
# emergency = [30, 10, 23, 6, 100]
# answer = []
# em_dict = {}

# emergency_sort = sorted(emergency, reverse=True)
# for i in range(len(emergency)):
#     em_dict[emergency_sort[i]] = i+1


# for i in range(len(emergency)):
#     answer.append(em_dict[emergency[i]])

# print(answer)


# # 숨어있는 숫자의 덧셈 (2)
# import re
# my_string = "aAb1B2cC34oOp"
# answer = []

# numbers = re.sub(r'[^0-9]', ' ', my_string).split(' ')
# for i in numbers:
#     if i != '':
#         answer.append(int(i))

# print(sum(answer))


# # 간단한 방법
# # my_string에서 숫자가 아닌 부분은 모두 공백으로 변환
# s = ''.join(i if i.isdigit() else ' ' for i in my_string)
# # 숫자인 부분이 문자열로 되어 있으니, integer로 변경 후 합계 구하기
# print(sum(int(i) for i in s.split()))



# # 한번만 등장한 문자
# s = "abdc"
# answer = ''
# slist = list(set([i for i in s]))

# for i in slist:
#     if s.count(i) == 1:
#         answer += i
# print(''.join(sorted(answer)))

# # 간단한 방법
# print(''.join(sorted([i for i in set(s) if s.count(i) == 1])))



# # 이진수 더하기
# bin1 = "10"
# bin2 = "11"

# print(format(int(bin1, 2) + int(bin2, 2), 'b'))


# # 소인수 분해
# n = 420
# count = 2
# answer = []

# while n != 1:
#     if n % count != 0:
#         count += 1
#     elif n == 1:
#         break
#     else:
#         answer.append(count)
#         n = int(n / count)
    
#     print(n, count)
# print(sorted(list(set(answer))))



# # 컨트롤 제트 >>> fail(테스트케이스 1개)
# s = "-1 -2 -3 Z"
# answer = 0
# s = s.split(' ')
# print(s)

# for i in range(len(s)):
#     print(i, s[i])
#     if str(abs(int(s[i]))).isdigit() == True:
#         answer += int(s[i])
#     else:
#         print(s[i-1])
#         answer -= int(s[i-1])

# print(answer)