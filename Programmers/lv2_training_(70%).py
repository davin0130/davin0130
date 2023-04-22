# # 최댓값 / 최솟값
# n = 15
# answer = 0 

# nlist = [i+1 for i in range(n)]
# print(nlist)


# # jadencase 문자열
# # 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열
# s = 'aaaa   AAAAAAA'
# answer = s.split(' ')
# print(answer)

# for i in range(len(answer)):
#     if len(answer[i]) != 0:
#         answer[i] = answer[i][0].upper() + answer[i][1:].lower()

# print(' '.join(i for i in answer))


# # 올바른 괄호 >>> fail
# s = "()()"
# num = 0
# i = 0
# s = [i for i in s]
# print(s)

# while num == 0:
#     if "(" in s and i < len(s)-2:
#         if s[i] == "(" and s[i+1] ==")":
#             s.pop(i)
#             s.pop(i)
#             i = 0
#             print(s)
#         else:
#             i += 1
#             if i == len(s):
#                 num = 1
#                 break
#         print(i, s, num)
#     else:
#         break

# print(True if len(s) == 0 else False)
    
# # 최솟값 만들기
# A = [1,2]
# B = [3,4]
# answer = 0

# A = sorted(A)
# B = sorted(B, reverse=True)
    
# for i in range(len(A)):
#     answer += A[i] * B[i]

# print(answer)


# # 이진 변환 반복하기
# s = "110010101001"

# s_length = len(s)
# count = 0
# zero = 0

# while s_length != 1:
#     print(s)
#     zero += s.count('0')
#     s = s.replace('0','')
#     s_length = len(s)
#     s = format(len(s), 'b')
#     count += 1

# print(count, zero)


# # 피보나치 수열 >>>> fail
# n = 47
# answer = 0
# # 이전 결과
# hap = 1
# # 지금
# now = 1

# for i in range(2, n):
#     answer = hap + now
#     hap = now
#     now = answer
#     print(i-1, i, "|", hap, now, answer)


# # 숫자의 표현
# n = 15
# answer = 0
# num = 1
# sumn = 0

# while num <= n:
#     for i in range(num, n+1):
#         sumn += i
#         if sumn == n:
#             answer += 1
#             break
#         elif sumn > n:
#             break
#     num += 1
#     sumn = 0


# print(answer)



# 다음 큰 숫자
import itertools
n = 15
bn = [i for i in format(n, 'b')]
print(bn, len(bn))
new_bcl = []

if len(set(bn)) == 1:
    bn.append('0')

bcl = list(set(itertools.permutations(bn, len(bn))))
print(int('0b'+''.join(list(bcl[0])), 2))
for i in bcl:
    new_bcl.append(int('0b'+''.join(list(i)), 2))
new_bcl.sort()
answer = new_bcl[new_bcl.index(n)+1]

print(answer)