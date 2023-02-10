# 메뚜기 수
hp = 102
answer = 0

for i in range(hp//5+5):
    if hp == 0:
        break
    if hp >= 5:
        answer += 1
        hp = hp - 5
        print("1", answer, hp)
    else:
        if hp >= 3:
            answer += 1
            hp = hp - 3
            print("2", answer, hp)
        else:
            answer += hp
            hp = hp - 1
            print("3", answer, hp)