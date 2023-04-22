# 짝 지어 제거하기
s = "baabaa"
s_bool = True
go = True
answer = 0

while s_bool == True:
    some = ''
    while go == False:
        for i in range(len(s)):
            if i < len(s)-1:
                if s[i] == s[i+1]:
                    some = s[i:i+2]
                    s = s.replace(some, '')
                    go = False



# while s_bool == True:
#     some = ''
#     print(s, len(s))
#     for i in range(len(s)):
#         if i < len(s)-1:
#             if s[i] == s[i+1]:
#                 print(i, s[i], s[i+1])
#                 print("s[i:i+2]", s[i:i+2])
#                 some = s[i:i+2]
#                 s = s.replace(some, '')
#                 s_bool == True
#             else:
#                 s_bool = False
#         elif len(s) == 0:
#             s_bool = False

#     print("s", s)



# if len(s) == 0:
#     answer = 1
    
# print(s, answer)
