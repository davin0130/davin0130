# 업무할 때 필요해서 작업한 자동화 프로그램
# 이름, 사번, 대상자 이름, 생성할 폴더 수, 폴더명 작성 시 자동으로 폴더 생성
import os
from tkinter import *
from datetime import datetime

# 현재 날짜 년도만 가져오기 (2023년일 경우 23)
year = str(datetime.today().year)[-2:]


# 폴더 생성 함수
def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

# 폴더명 생성 함수
def createFolderName():
    # 대상자 이름 여러개 작성 시 ','로 작성하게 하고
    # 값을 가져올때는 공백제거, ',' 기준으로 분리
    taget_name_all = entry5.get().replace(' ','').split(',')
    for i in range(len(taget_name_all)):
        user =  entry2.get()
        num = str(int(entry3.get())+i).zfill(3)
        file_name = entry1.get()
        target_name = entry5.get()
        folder_name = 'CM-%s-%s-%s %s_%s' % (year, user, num, file_name, taget_name_all[i])
        print(folder_name)
        # 폴더명을 가지고 폴더 생성
        createFolder(folder_name)


# GUI 생성
window = Tk()

# GUI 명
window.title("자문비 지급 폴더 생성")
# GUI 사이즈
window.geometry("500x250+500+400")
# GUI 사이즈 수정 가능여부(세로 가로 모두 불가)
window.resizable(False, False)


label1  = Label(window,text='생성할 폴더명 : ').pack()
entry1 = Entry(window, width=50)
entry1.pack()

label2 = Label(window,text='작성자 코드 : ').pack()
entry2 = Entry(window, width=50)
entry2.pack()

label3 = Label(window,text='시작 번호 : ').pack()
entry3 = Entry(window, width=50)
entry3.pack()

label4 = Label(window,text='지급자에는 ","로 구분하여 작성해주세요.').pack()

label5 = Label(window,text='지급자 : ').pack()
entry5 = Entry(window, width=50)
entry5.pack()


# 실행버튼 클릭 시 createFolderName 함수 실행
execute = Button(window, text="실행", command=createFolderName, width=20, bg="#ffc000")
execute.pack()

        
window.mainloop()


