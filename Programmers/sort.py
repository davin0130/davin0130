import re

my_string = "hello28436873"
answer = []

my_string = re.sub(r'[^0-9]', '', my_string)
# (0-9) 까지의 패턴이 (^) 아닌 것을 찾아 ('') 공백으로 바꾼다는 의미
for i in my_string:
    answer.append(int(i))
answer.sort()
print(answer)

# .isdigit() 메소드 : 숫자인지 확인하는 메소드
print(sorted([int(c) for c in my_string if c.isdigit()]))
# my_string의 문자 (c)하나씩 검토할 때 isdigit() 숫자이면, 
# int 타입으로 변경하여
# [] 리스트에 담는데,
# 이것을 sorted 정렬하라