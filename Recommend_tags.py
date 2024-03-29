from tkinter import *
from tkinter import ttk, BooleanVar
import tkinter as tk
from tkinter import font
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
from konlpy.tag import Okt
from collections import Counter
import pickle
import keyword_counted
import gensim
import threading
import webbrowser


def open_instagram():
    url = 'https://www.instagram.com'
    webbrowser.open(url)


def strip_e(st):
    RE_EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
    return RE_EMOJI.sub(r'', st)


def nouns(poststr):
    with open('Dataset1/insta_counted.bin', 'rb') as f2:
        freq_data = pickle.load(f2)

    postNouns = []
    modelResList1 = []
    modelResList2 = []
    resultList = []
    postKwords = []

    poststr = strip_e(poststr)
    poststr = (okt.nouns(poststr))

    if len(poststr) < 2:
        return []

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
            tempStr = model1.wv.most_similar(kword, topn=6)
            for kwordM1 in tempStr:
                modelResList1.append(kwordM1[0])
        except KeyError as e:
            # print(e)
            continue
    modelResList1.extend(postKwords)

    for recomTag in modelResList1:
        try:
            tempStr2 = model2.wv.most_similar(recomTag, topn=4)
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
    global okt
    okt = Okt()

    resultList = []

    window = tk.Tk()
    window.title("Tags 추천")
    window.geometry("640x558+100+100")
    window.resizable(False, False)
    window.configure(background='white')

    def click():
        if chkVal.get():
            t.delete('1.0', END)
        resultList = nouns(textbox.get('1.0', END))

        if len(resultList) < 2:
            messagebox.showwarning(
                title="Tags 추천",
                message="2개 이상의 명사를 포함한 글을 입력해주세요."
            )
        else:
            for x in resultList:
                t.insert(END, x + ' ')

    def click2():
        window.clipboard_clear()
        window.clipboard_append(t.get('1.0', END))
        window.update()

    def initOktNouns():
        okt.nouns("가")
        action.config(text="process", state=NORMAL)


    # UI #

    # background
    label3 = ttk.Label(window)
    label3.img = PhotoImage(file='basetemp.gif')
    label3.pack()
    label3.config(justify=CENTER)
    label3.config(image=label3.img)

    # title
    font = tk.font.Font(size=20, slant="italic")
    title = tk.Label(window, text="Instagram ###", font=font, background='white')
    title.place(x=250, y=50)

    y1 = int(180)  # 본문 입력창 위치
    label1 = tk.Label(window, text="본문을 입력하세요:", background='white')
    label1.place(x=50, y=y1 - 25)
    textbox = ScrolledText(window, height=6, width=60)
    textbox.place(x=50, y=y1)

    # process 버튼
    action = ttk.Button(window, text="loading...", command=click, state=DISABLED)
    action.place(x=500, y=y1 - 2)

    y2 = 325  # 추천 해쉬태그 창 위치
    label2 = tk.Label(window, text="추천 해쉬태그:", background='white')
    label2.place(x=50, y=y2 - 25)
    t = ScrolledText(window, height=6, width=76)
    t.place(x=50, y=y2)

    # 클립보드로 복사 버튼
    window.update()
    action2 = ttk.Button(window, text="copy tags", command=click2, state=NORMAL)
    action2.place(x=500, y=y2 - 27)

    # 인스타그램 연결버튼
    btn = tk.Button(window, compound=TOP, command=open_instagram, height=91, width=91)
    btn.img = PhotoImage(file='insta.gif')
    btn.pack()
    btn.config(image=btn.img)
    btn.place(x=50, y=40)

    # auto remove 체크박스
    chkVal = tk.IntVar()
    chkVal.set(True)
    checkact = ttk.Checkbutton(window, text="auto remove", var=chkVal)
    checkact.place(x=400, y=y2 - 25)


    t1 = threading.Thread(target=initOktNouns)
    t1.daemon = True
    t1.start()

    window.mainloop()


if __name__ == '__main__':
    main()
