# CTF 문제 풀이
# Toy Project

#1 Christmas Tree
import zipfile

# 500번 압축된 폴더 해제 후 안의 flag 찾기
FileName = 'flag_499.zip'


for i in range(498):
    count = int(FileName[5:8])-i
    file1 = FileName[:5]+str(count)+".zip"
    file2 = FileName[:5]+str(count-1)+".zip"
    
    print(file1)
    print(file2)
    
    jungle_zip = zipfile.ZipFile('C:/Users/Owner/Downloads/'+file1)
    jungle_zip.extract(file2, 'C:/Users/Owner/Downloads')

jungle_zip.close()



#2 flag.png Black Bit
import numpy as np
from PIL import Image

# 이미지 불러오기
img_name = ('C:/Users/Owner/Downloads/flag.png')
im = Image.open('python_img/'+img_name)

pix = np.array(im)

# 이미지 픽셀 값 확인 후 흰 부분은 0, 검정인 부분은 1로 변환
# 그 외는 모두 3으로 처리
for i in range(229):
    for j in range(102):
        if (pix[i,j] == [0,0,0,255]).all():
            if j % 7 == 0:
                print('\n')
            print('1', end='')
        elif (pix[i,j] == [255,255,255,255]).all():
            print('0', end='')
        else:
            print(i,j, end='')
            print('3', end='')



