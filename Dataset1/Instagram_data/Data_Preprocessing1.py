#원본파일을 5등분 해서 #필카 들어있는 게시물만 뽑아서 각각 data.txt data2.txt data3.txt data4.txt data5.txt에 씀
import re
import json

with open('D4.txt') as f:
    line_num=1
    line = f.readline()
    while line:
        f2 = open('data4.txt','a')
        if '#필카' in line:
            f2.write(line)
        line=f.readline()
        line_num+=1


f.close()
