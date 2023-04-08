# # 최댓값 / 최솟값
# n = 15
# answer = 0 

# nlist = [i+1 for i in range(n)]
# print(nlist)


# #jadencase 문자열

# s = "for   THE  "
# slist = s.split(' ')
# print(slist)
# print(len(s))
# sstr = ""

# for i in range(len(slist)):
#     slist[i] = slist[i].lower()
#     if slist[i] != "":
#         if slist[i][0].isdigit() == False:
#             slist[i] = slist[i].replace(slist[i][0], slist[i][0].upper())

# for i in range(len(slist)):

#     if i+1 == len(slist):
#         sstr += slist[i]
#     else:
#         sstr += slist[i] + " "
# print(sstr)
# print(len(sstr))


# # 최솟값 만들기
# A = [1,2]
# B = [3,4]
# answer = 0

# A = sorted(A)
# B = sorted(B, reverse=True)
    
# for i in range(len(A)):
#     answer += A[i] * B[i]

# print(answer)


# 이진 변환 반복하기
s = "110010101001"

s_length = len(s)
count = 0
zero = 0

while s_length != 1:
    print(s)
    zero += s.count('0')
    s = s.replace('0','')
    s_length = len(s)
    s = format(len(s), 'b')
    count += 1

print(count, zero)
