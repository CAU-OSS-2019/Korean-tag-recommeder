#태그 제거
#data.txt data2.txt data3.txt data4.txt data5.txt -> DATT
import re
import json

with open('data5.txt') as f:
    line_num=1
    line = f.readline()
    while line:
        f2 = open('DATT.txt','a')
        head, sep, tail = line.partition('#')
        f2.write(head+"\n")
        
        line=f.readline()
        line_num+=1


f.close()
