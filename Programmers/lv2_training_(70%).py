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


# # # 피보나치 수열
# n = 5
# # 0, 1, 1, 3, 5, 8...
# a = 0
# b = 1
# answer = 0

# while n-1 != 0:
#     answer = a + b
#     a = b
#     b = answer
#     print("a", a)
#     print("b", b)
#     print("n", n)
#     print("answer", answer)
#     print("-----")
#     n -= 1

# print(answer%1234567)


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



# # 다음 큰 숫자  >>> fail
# import itertools
# n = 15
# bn = [i for i in format(n, 'b')]
# print(bn, len(bn))
# new_bcl = []

# if len(set(bn)) == 1:
#     bn.append('0')

# bcl = list(set(itertools.permutations(bn, len(bn))))
# print(int('0b'+''.join(list(bcl[0])), 2))
# for i in bcl:
#     new_bcl.append(int('0b'+''.join(list(i)), 2))
# new_bcl.sort()
# answer = new_bcl[new_bcl.index(n)+1]

# print(answer)



# # 짝지어 제거하기 >>> fail
# s = 'baabaa'
# i = 0
# s = [i for i in s]

# while i != len(s):
#     if i < len(s):
#         print(i)
#         if s[i] == s[i+1]:
#             s[i:i+2] = ''
#             i = 0
#     else:
#         break
#     i += 1

#     print(s, len(s))

# if len(s) == 0:
#     print(1)
# else:
#     print(0)




# 영어 끝말잇기
n = 5
words = ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]

if words[0] == words[-1]:
    answer = [(len(words)-1)%n+1, len(words)//n]
else:
    for i in range(1, len(words)+1):
        if words[i-1][-1] != words[i][0]:
            answer = [i%n, i//n]
            break
        else:
            answer = [0, 0]
print(answer)