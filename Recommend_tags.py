from tkinter import *
from tkinter import ttk, BooleanVar
import tkinter as tk
from tkinter import font
from tkinter import messagebox
from konlpy import tag
from konlpy.tag import Okt
from collections import Counter
import pickle
import keyword_counted
import gensim


def strip_e(st):
	RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
	return RE_EMOJI.sub(r'', st)


def nouns(poststr):
	with open('Dataset1/insta_counted.bin', 'rb') as f2:
		freq_data = pickle.load(f2)

	okt = Okt()
	postNouns = []
	modelResList1 = []
	modelResList2 = []
	resultList = []
	postKwords = []

	poststr = strip_e(poststr)
	poststr = (okt.nouns(poststr))
	postNouns.append(poststr)
	loop = 0

	for word in postNouns:
		if word:
			count_list = Counter(word)
			postKwords.extend(keyword_counted.search_key(count_list, freq_data, loop))

	modelDr1 = 'Model1_word2vec.model'
	modelDr2 = 'Model2_word2vec.model'
	model1 = gensim.models.Word2Vec.load(modelDr1)
	model2 = gensim.models.Word2Vec.load(modelDr2)

	for kword in postKwords:
		try:
			tempStr = model1.wv.most_similar(kword,topn= 6)
			for kwordM1 in tempStr:
				modelResList1.append(kwordM1[0])
		except KeyError as e:
			#print(e)
			continue
	modelResList1.extend(postKwords)

	for recomTag in modelResList1:
		try:	
			tempStr2 = model2.wv.most_similar(recomTag,topn= 4)
			for kword in tempStr2:
				modelResList2.append(kword[0])

		except KeyError as e:
			print(e)
			continue
	print(postKwords)
	postKwords.extend(modelResList2)
	print(modelResList1)
	print(modelResList2)

	for i in range(len(postKwords)):
		if '#' == postKwords[i][0]:
			continue
		else:
			postKwords[i] = '#' + postKwords[i]

	postKwords = list(set(postKwords))
	return postKwords


def main():
	
	resultList = []
	
	window=tk.Tk()
	window.title("Tags 추천")
	window.geometry("640x480+100+100")
	window.resizable(False, False)

	IsCheck = True
	def checkclick(IsCheck):
		'''	if IsCheck:
        IsCheck = False
    else: IsCheck = True
    return IsCheck'''


	def click():
		if chkVal.get():
			t.delete('1.0', END)
		resultList = nouns(str.get())

		if resultList:
			for x in resultList:
				t.insert(END, x + ' ')
		else:
			messagebox.showwarning(
				title="Tags 추천",
				message="2개 이상의 명사를 포함한 글을 입력해주세요."
			)



	
	str = StringVar()

	font = tk.font.Font(size=20, slant="italic")
	title = tk.Label(window, text="Instagram ###", font=font)
	title.place(x=250, y=50)

	y1 = int(180)
	label1 = tk.Label(window, text="문장을 입력하세요")
	label1.place(x=50, y=y1-25)
	textbox = ttk.Entry(window, width=60, textvariable=str)
	textbox.place(x=50, y=y1)

	action = ttk.Button(window, text="process", command=click)
	action.place(x=500, y=y1-2)

	y2 = 300
	label2 = tk.Label(window, text="추천 해쉬태그:")
	label2.place(x=50, y=y2-25)
	t = Text(window,height=3, width=77)
	t.place(x=50, y=y2)

	chkVal = tk.IntVar()
	chkVal.set(True)
	print()
	checkact = ttk.Checkbutton(window, text="auto remove", var=chkVal)
	checkact.place(x=500, y=y2-25)

	window.mainloop()
	

if __name__ == '__main__':
	main()


