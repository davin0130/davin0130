# # 정수와 자연수를 입력받아 정수부터 정수만큼 차이나는 수가 자연수 만큼 있는 리스트 출력
# x = 10000000
# n = 1000

# print(list(range(x, x*(n+1), x)))

# # 문자열 정수로 변경
# string = '-1234'
# print(int(string))

# # 내림차순으로 변경
# n = 118372
# answer = []
# for i in str(n):
#     answer.append(int(i))
# answer.sort()
# answer.reverse()
# for i in answer:
#     print(i, end='')

# # 더 간단한 방법 (sort 함수에 reverse=True 설정)
# ls = list(str(n))
# ls.sort(reverse = True)
# print(int("".join(ls)))

# # 나머지 1인 최소값 출력
# n = 10
# answer = []
# for i in range(n):
#     if n%(i+1) == 1:
#         answer.append(i+1)

# print(min(answer))

# # 더 간단한 방법 | 한번에 출력
# print([x for x in range(1,n+1) if n%x==1][0])


# 두 정수 사이 값의 합 출력
a=3
b=3
min = min(a,b)
max = max(a,b)
for i in range(min, max):
    min += i+1

print(min)