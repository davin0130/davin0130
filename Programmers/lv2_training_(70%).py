# # 최댓값 / 최솟값
# n = 15
# answer = 0 

# nlist = [i+1 for i in range(n)]
# print(nlist)


#jadencase 문자열

s = "for   THE  "
slist = s.split(' ')
print(slist)
print(len(s))
sstr = ""

for i in range(len(slist)):
    slist[i] = slist[i].lower()
    if slist[i] != "":
        if slist[i][0].isdigit() == False:
            slist[i] = slist[i].replace(slist[i][0], slist[i][0].upper())

for i in range(len(slist)):

    if i+1 == len(slist):
        sstr += slist[i]
    else:
        sstr += slist[i] + " "
print(sstr)
print(len(sstr))