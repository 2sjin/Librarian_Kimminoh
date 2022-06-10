from tkinter import*
import tkinter.messagebox
import pandas as pd
from tabulate import tabulate
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import *
from datetime import datetime, timedelta
# 2번째 화면
def BOOK_MANAGEMENT():
    #공통부분 ↓---------------------------------------------------------------------
    window = Tk()
    window.title("도서관리")
    window.geometry("700x500")
    label1 = Label(window, text = '도서관리프로그램', bg = 'gray', width = 700, height = 5)
    window.configure(background = 'sky blue')
    #공통부분 ↑---------------------------------------------------------------------
    # ㉮
    BTN_REG_EDIT = Button(window, text='도서\n등록/수정', bg='orange', width='18',
                          height='8', command = BOOK_MANAGEMENT_FIRST)
    # ㉯
    BTN_SEARCH_RENT = Button(window, text='도서\n조회/대출', bg='orange', width='18',
                          height='8', command = BOOK_LOOKUP)
    # ㉰
    BTN_DELETE = Button(window, text='도서삭제', bg='orange', width='18',
                          height='8', command = BOOK_DELETE)    
      
    BTN_CANCEL = Button(window, text='뒤로가기', bg='orange'
    , width='8', height='2',command=window.destroy)    
    label1.pack()
    BTN_REG_EDIT.pack()
    BTN_SEARCH_RENT.pack()
    BTN_DELETE.pack()
    BTN_CANCEL.pack()
    
    BTN_REG_EDIT.place(x=100,y=170)
    BTN_SEARCH_RENT.place(x=300,y=170)
    BTN_DELETE.place(x=500,y=170)
    BTN_CANCEL.place(x=5,y=25)
# ㉮의 화면
# 도서 등록/수정 화면
def BOOK_MANAGEMENT_FIRST():
    #공통부분 ↓-----------------------------------------------------------------------
    window = Tk()
    window.title("도서 등록/수정")
    window.geometry("700x500")
    label1 = Label(window, text = '도서 등록/수정', bg = 'gray',width = 700, height = 5)
    window.configure(background = 'sky blue')
    #공통부분 ↑-----------------------------------------------------------------------  
    def click_item(event):
        selected=BOOK_SELECT_BOX.focus()
        print(selected)
        BOOK_EDIT(int(selected))
        
    
    BTN_NEW_REG = Button(window, text='도서 신규 등록', bg='orange', width='15', height='2',
                         command = BOOK_NEW_REG)
    BTN_CANCEL = Button(window, text='뒤로가기', bg='orange',
     width='8', height='2',command=window.destroy)





    label2 = Label(window, text='수정할 도서 검색하기 :',fg='black' ,
                   font=('맑은 고딕',10), width=20,height=1)

    label3 = Label(window, text='도서명 혹은 저자로 검색해주세요 ↓',fg='black' ,
                   font=('맑은 고딕',10), width=30,height=1) 
    BOOK_SEARCH_LABEL = Entry(window)
    BOOK_SEARCH_LABEL.place(relx=0.25,rely=0.3,relwidth=0.6,relheight=0.07)
    '''#  도서명과 저자로 검색하기 / 이거 아직 구현 안 됨
    def search ():        
        for ISBN in csv_pull.index.tolist():
            BOOK_SEARCH_LABEL = "파이썬"
            search1 = csv_pull["BOOK_TITLE"].str.contains(BOOK_SEARCH_LABEL)
            search2 = csv_pull["BOOK_AUTHOR"].str.contains(BOOK_SEARCH_LABEL)
            search_Book1 = csv_pull.loc[search1 | search2,["BOOK_TITLE"]]
            search_Book2 = csv_pull.loc[search1 | search2,["BOOK_AUTHOR"]]
            search_Book3 = csv_pull.loc[search1 | search2,["BOOK_PUBLIC"]]
            book_add = (ISBN, search_Book1,search_Book2,search_Book3)
            BOOK_SELECT_BOX.insert("","end",text="",value=book_add,iid=book_add[0]) '''
    
    BOOK_SEARCH_BTN = Button(window, text = '검색', fg='white' ,bg='black') # command=search
    BOOK_SEARCH_BTN.place(relx=0.86,rely=0.3,relwidth=0.1,relheight = 0.07)


    # 등록되어 있는 도서 리스트
    # 등록되어 있는 도서 리스트 
    csv_pull = pd.read_csv("csv/book_1.csv",encoding = "utf-8")
    csv_pull = csv_pull.set_index("BOOK_ISBN")

    BOOK_SELECT_BOX = ttk.Treeview(window, columns=(1,2,3,4), height = 13,show="headings")
    
    
    BOOK_SELECT_BTN = Button(window, text = '선택하기', fg='white', bg = 'black')
    BOOK_SELECT_BTN.place(relx=0.86,rely=0.4,relwidth=0.1,relheight=0.05)
    BOOK_SELECT_BTN.bind('<Button-1>',click_item)



    # 필드명
    BOOK_SELECT_BOX.heading(1, text='ISBN')
    BOOK_SELECT_BOX.heading(2, text='도서명')
    BOOK_SELECT_BOX.heading(3, text='저자')
    BOOK_SELECT_BOX.heading(4, text='출판사')
    # 기본 너비 
    BOOK_SELECT_BOX.column(1, width='170')
    BOOK_SELECT_BOX.column(2, width='130')
    BOOK_SELECT_BOX.column(3, width='120')
    BOOK_SELECT_BOX.column(4, width='80')
    #스크롤바 (안생기는데 왜 안생기는지 모르겠음)
    scroll = ttk.Scrollbar(window, orient="vertical", command=BOOK_SELECT_BOX.yview)
    scroll.pack(side='right', fill='y')
    BOOK_SELECT_BOX.configure(yscrollcommand=scroll.set)
    # 목록 출력할 데이터 
    # 데이터 프레임 출력
    
    for ISBN in csv_pull.index.tolist():
        book_title = csv_pull.loc[ISBN, "BOOK_TITLE"]
        book_author = csv_pull.loc[ISBN, "BOOK_AUTHOR"]
        book_publish = csv_pull.loc[ISBN, "BOOK_PUBLIC"]
        
        book_add = (ISBN, book_title, book_author, book_publish)
        BOOK_SELECT_BOX.insert("","end",text="",value=book_add,iid=book_add[0])
    

    BOOK_SELECT_BOX.bind('<Double-Button-1>', click_item)
    BOOK_SELECT_BOX.place(x=90, y=200)

    label1.pack()
    label2.place(x=15, y=155)
    label3.place(x=177, y=125)
    label2.place(x=5, y=155)
    BTN_CANCEL.place(x=5,y=25)
    BTN_NEW_REG.place(x=5,y=90)

# ㉮-1 신규 도서 추가     
def BOOK_NEW_REG():
    #공통부분 ↓-----------------------------------------------------------------------
    window = Tk()
    window.title("도서 신규등록")
    window.geometry("700x500")
    label1 = Label(window, text = '도서 신규 등록', bg = 'gray', width = 700, height = 3)
    window.configure(background = 'sky blue')    
    #공통부분 ↑-----------------------------------------------------------------------  
    label1.pack() # 창 제목 레이블
    
    def BTN_EDIT(a, b, c, d,e, f,g):
        a = Button(window, text=b, bg=c, width=d, height=e)
        a.place(x=f, y = g)    
        
    def BLANK(a,b,c,d,e):
        a = Entry(window)
        a.place(x= b, y= c,relwidth=d,relheight=e)
    # 중복확인시 이벤트 발생
    def ERROR_1():   # 예외처리 1
        tkinter.messagebox.showinfo("ERROR","해당 도서는 등록 가능 합니다 !")
    def ERROR_2():   # 예외처리 2
        tkinter.messagebox.showerror("ERROR","해당 도서는 등록 불가능 합니다 !")
        tkinter.messagebox.showinfo("ERROR","해당 도서는 등록 불가능 합니다 !")
    def ERROR_3():   # 예외처리 3
        tkinter.messagebox.showerror("ERROR","중복 확인 후 도서 등록이 가능합니다 !")
        tkinter.messagebox.showinfo("ERROR","중복 확인 후 도서 등록이 가능합니다 !")
    def ERROR_4():   # 예외처리 4
        tkinter.messagebox.showerror("ERROR","가격은 정수로만 입력 가능합니다 !")
        tkinter.messagebox.showinfo("ERROR","현재 도서는 이미 등록되어 있는 도서입니다. !")
    def ERROR_5():   # 예외처리 5
        tkinter.messagebox.showerror("ERROR","해당 정보는 숫자로만 입력이 가능합니다 !")
        tkinter.messagebox.showinfo("ERROR","해당 부분은 숫자로만 입력이 가능합니다 !")
    def ERROR_6():   # 예외처리 6
        tkinter.messagebox.showerror("ERROR","해당 정보는 필수정보 입니다. 다시 작성해주세요 !")

    def REG():  # 확인 버튼 눌렀을 시
        MSB = tkinter.messagebox.askquestion ('신규 도서 등록','도서를 등록 하시겠습니까?')
        tkinter.messagebox.showinfo("ERROR","해당 정보는 필수정보 입니다. 다시 작성해주세요 !")

        if MSB == 'yes':
            a = SEARCH_BOOK_ISBN.get()
            b = SEARCH_BOOK_TITLE.get()
            c = SEARCH_BOOK_AUTHOR.get()
            d = SEARCH_BOOK_PUBLIC.get()
            e = SEARCH_BOOK_PRICE.get()
            f = SEARCH_BOOK_LINK.get()
            g = SEARCH_IMAGE_FIND.get()
            h = SEARCH_BOOK_DESCRIPTION.get()
            #i = SEARCH_BOOK_RENTAL

            #하나라도 입력하지 않았을 때
            if a.strip()=="" or b.strip()=="" or c.strip()=="" or d.strip()=="" or e.strip()=="" \
               or f.strip()=="" or g.strip()=="" or h.strip()=="":
                ERROR_6()
                return 0

            # 중복확인 안했을 때 
            if not OVERLAP_CHECK['state'] == 'disabled' :
                ERROR_3()
    def REG():
        csv_pull = pd.read_csv("csv/book_1.csv",encoding = "utf-8")
        csv_pull = csv_pull.set_index("BOOK_ISBN")

        a = SEARCH_BOOK_ISBN.get()

            # 가격이 정수가 아닐 때
        if not e.isdigit():
                ERROR_4()

        else:
                csv_pull = pd.read_csv("csv/book_1.csv",encoding = "utf-8")
                csv_pull = csv_pull.set_index("BOOK_ISBN")
                csv_pull.loc[a, 'BOOK_TITLE']= b
                csv_pull.loc[a, 'BOOK_AUTHOR']= c  
                csv_pull.loc[a, 'BOOK_PUBLIC']= d 
                csv_pull.loc[a, 'BOOK_PRICE']= int(e)
                csv_pull.loc[a, 'BOOK_LINK']= f
                csv_pull.loc[a, 'BOOK_IMAGE']= g
                csv_pull.loc[a, 'BOOK_DESCRIPTION']= h
                #csv_pull.loc[a, 'BOOK_RENTAL']= "FALSE"
                #csv 저장하기 
                csv_pull.to_csv("csv/book_1.csv", index = True)
        b = SEARCH_BOOK_TITLE.get()
        csv_pull.loc[a, 'BOOK_TITLE']= b

        c = SEARCH_BOOK_AUTHOR.get()
        csv_pull.loc[a, 'BOOK_AUTHOR']= c

        d = SEARCH_BOOK_PUBLIC.get()
        csv_pull.loc[a, 'BOOK_PUBLIC']= d

        print(tabulate(csv_pull, headers='keys', tablefmt='psql',numalign='left',stralign='left'))
        window.destroy()
        e = SEARCH_BOOK_PRICE.get()
        csv_pull.loc[a, 'BOOK_PRICE']= int(e)

        f = SEARCH_BOOK_LINK.get()
        csv_pull.loc[a, 'BOOK_LINK']= f

        g = SEARCH_IMAGE_FIND.get()
        csv_pull.loc[a, 'BOOK_IMAGE']= g

        h = SEARCH_BOOK_DESCRIPTION.get()
        csv_pull.loc[a, 'BOOK_DESCRIPTION']= h

        #i = SEARCH_BOOK_RENTAL
        #csv_pull.loc[a, 'BOOK_RENTAL']= "FALSE"

        #csv 저장하기 
        csv_pull.to_csv("csv/book_1.csv", index = True)

        print(tabulate(csv_pull, headers='keys', tablefmt='psql',numalign='left',stralign='left'))


    def ISBN_OVERLAP():
        print(" ISBN 중복 확인 ")
        csv_pull = pd.read_csv("csv/book_1.csv",encoding = "utf-8")
        csv_pull = csv_pull.set_index("BOOK_ISBN")

        a = SEARCH_BOOK_ISBN.get()
        ISBN_OVERLAP = csv_pull.index.tolist()
        if  a in ISBN_OVERLAP:
            ERROR_2()

        elif not a.isdigit():
            ERROR_5()
        if ISBN_OVERLAP in [a] :
            print("이 ISBN은 사용하실 수 없습니다 !")
            print("")
            print("")

        else :
            ERROR_1()
            # 중복 확인 완료시 버튼 비활성화 
            OVERLAP_CHECK['state'] = 'disabled'
            SEARCH_BOOK_ISBN['state'] = 'disabled'
            print("사용가능한 ISBN입니다 !")
            print("")
            print("")


    # 사진 미리 보기 창
    # 예외처리 (사진을 등록하지 않았을 때) => 메세지 창 띄우기


    photo=PhotoImage(master=window)
    IMAGE_label = Label(window,image=photo,text="사진\n미리보기",bg="orange",width='80',height='100')
    IMAGE_label.place(x=30,y=80)
    BTN_BOOK_ISBN = Button(window, text='ISBN', bg='orange', width='8', height='1')
    BTN_BOOK_ISBN.place(x=170, y = 80)
    SEARCH_BOOK_ISBN = Entry(window)
    SEARCH_BOOK_ISBN.place(x= 250, y= 80,relwidth=0.5,relheight=0.05)
    # 중복확인시 이벤트 추가함
    OVERLAP_CHECK = Button(window, text='중복확인', bg='orange', width='7', height='1',
                           command = ISBN_OVERLAP)
    OVERLAP_CHECK.place(x=620, y = 80)    
    BTN_BOOK_TITLE = Button(window, text='도서명', bg='orange', width='8', height='1')
    BTN_BOOK_TITLE.place(x=170, y = 120)
    SEARCH_BOOK_TITLE = Entry(window)
    SEARCH_BOOK_TITLE.place(x= 250, y= 120,relwidth=0.5,relheight=0.05)
    BTN_BOOK_AUTHOR = Button(window, text='저자', bg='orange', width='8', height='1')
    BTN_BOOK_AUTHOR.place(x=170, y = 160)
    SEARCH_BOOK_AUTHOR = Entry(window)
    SEARCH_BOOK_AUTHOR.place(x= 250, y= 160,relwidth=0.5,relheight=0.05)
    BTN_BOOK_PUBLIC = Button(window, text='출판사', bg='orange', width='8', height='1')
    BTN_BOOK_PUBLIC.place(x=170, y = 200)
    SEARCH_BOOK_PUBLIC = Entry(window)
    SEARCH_BOOK_PUBLIC.place(x= 250, y= 200,relwidth=0.5,relheight=0.05)
    BTN_BOOK_PRICE = Button(window, text='가격', bg='orange', width='8', height='1')
    BTN_BOOK_PRICE.place(x=170, y = 240)
    SEARCH_BOOK_PRICE = Entry(window)
    SEARCH_BOOK_PRICE.place(x= 250, y= 240,relwidth=0.5,relheight=0.05)
    BTN_BOOK_LINK = Button(window, text='URL', bg='orange', width='8', height='1') 
    BTN_BOOK_LINK.place(x=170, y = 280)
    SEARCH_BOOK_LINK = Entry(window)
    SEARCH_BOOK_LINK.place(x= 250, y= 280,relwidth=0.5,relheight=0.05)
    
    BTN_BOOK_DESCRIPTION = Button(window, text='도서 설명', bg='orange', width='8', height='1')
    BTN_BOOK_DESCRIPTION.place(x=170, y = 320)
    SEARCH_BOOK_DESCRIPTION = Entry(window)
    SEARCH_BOOK_DESCRIPTION.place(x= 250, y= 320,relwidth=0.5,relheight=0.05)
    BTN_IMAGE_FIND = Button(window, text='사진 찾기', bg='orange', width='8', height='1')
    BTN_IMAGE_FIND.place(x=170, y = 360)
    SEARCH_IMAGE_FIND = Entry(window)
    SEARCH_IMAGE_FIND.place(x= 250, y= 360,relwidth=0.5,relheight=0.05)
    
    def find_image_name():
        file_name=askopenfilename(parent=window,filetype=(("PNG파일", "*.png"),("모든 파일","*.*")))
        photo=PhotoImage(file=file_name,master=window)
        IMAGE_label.configure(image=photo)
        IMAGE_label.image=photo
        SEARCH_IMAGE_FIND.insert(0,file_name)
    BTN_FIND=Button(window, text="찾아보기",bg='gray',width='8',height='1',command=find_image_name)
    BTN_FIND.place(x=620,y=360)
    
    BTN_OK = Button(window, text='확인', bg='gray',width='7', height='1', command = REG)
    BTN_OK.place(x=300, y = 420)
    BTN_CANCEL = Button(window, text='취소', bg='gray', width='7', height='1',
                        command=window.destroy )
    BTN_CANCEL.place(x=400, y = 420)
# ㉮-2번째 창 / 도서 수정하기
# 도서 목록중 하나 선택해서 도서 수정하기 
def BOOK_EDIT(selected):
    #공통부분 ↓-----------------------------------------------------------------------
    window = Tk()
    window.title("도서 수정하기")
    window.geometry("700x500")
    label1 = Label(window, text = '도서 수정하기', bg = 'gray', width = 700, height = 3)
    window.configure(background = 'sky blue')    
    #공통부분 ↑-----------------------------------------------------------------------
    label1.pack() # 창 제목 레이블

    # 함수안의 함수 => 버튼 형식 생성
    def BTN_EDIT(a, b, c, d,e, f,g):
        a = Button(window, text=b, bg=c, width=d, height=e)
        a.place(x=f, y = g)    
    def BLANK(a,b,c,d,e):
        a = Entry(window)
        a.place(x= b, y= c,relwidth=d,relheight=e)
    

    # 리스트 박스 목록 더블클릭시 창 띄우기 아직 구현 X
    # 선택하기 눌러야 함
    window.lift()
    # 예외처리 이벤트
    def ERROR_7():     # 예외처리 7 #수정 불가인데 에러메세지?
        tkinter.messagebox.showerror("ERROR","해당 ISBN으로 수정이 가능합니다 !")
    def ERROR_7():     # 예외처리 7
        tkinter.messagebox.showinfo("ERROR","해당 ISBN으로 수정이 가능합니다 !")
    def ERROR_8():     # 예외처리 8
        tkinter.messagebox.showerror("ERROR","해당 ISBN으로는 수정하실 수 없습니다 !")
        tkinter.messagebox.showinfo("ERROR","해당 ISBN으로는 수정하실 수 없습니다 !")
    def ERROR_9():     # 예외처리 9
        tkinter.messagebox.showerror("ERROR","변경사항을 적용 하여야지 등록/수정이 가능합니다 !")
        tkinter.messagebox.showinfo("ERROR","변경사항을 적용 하여야지 등록/수정이 가능합니다 !")
    def ERROR_10():     # 예외처리 10
        tkinter.messagebox.showerror("ERROR","해당 부분은 숫자로만 입력이 가능합니다 !")
        tkinter.messagebox.showinfo("ERROR","해당 부분은 숫자로만 입력이 가능합니다 !")


    #def APPLY():

    csv_pull = pd.read_csv("csv/book_1.csv",encoding = "utf-8")
    csv_pull = csv_pull.set_index("BOOK_ISBN")


    photo=PhotoImage(file=csv_pull.loc[selected]["BOOK_IMAGE"],master=window)
    IMAGE_label = Label(window,image=photo,text="사진\n미리보기",bg="orange",width='80',height='100')
    IMAGE_label.configure(image=photo)
    IMAGE_label.image=photo
    IMAGE_label.place(x=30,y=80)
    BTN_BOOK_ISBN = Button(window, text='ISBN', bg='orange', width='8', height='1')
    BTN_BOOK_ISBN.place(x=170, y = 80)
    SEARCH_BOOK_ISBN = Entry(window)
    SEARCH_BOOK_ISBN.place(x= 250, y= 80,relwidth=0.5,relheight=0.05)
    SEARCH_BOOK_ISBN.insert(0,selected)




    BTN_BOOK_TITLE = Button(window, text='도서명', bg='orange', width='8', height='1')
    BTN_BOOK_TITLE.place(x=170, y = 120)
    SEARCH_BOOK_TITLE = Entry(window)
    SEARCH_BOOK_TITLE.place(x= 250, y= 120,relwidth=0.5,relheight=0.05)
    SEARCH_BOOK_TITLE.insert(0,csv_pull.loc[selected]["BOOK_TITLE"])
    #SEARCH_BOOK_TITLE.insert("","end",text="",value=book_add,iid=book_add[0])
    
    BTN_BOOK_AUTHOR = Button(window, text='저자', bg='orange', width='8', height='1')
    BTN_BOOK_AUTHOR.place(x=170, y = 160)
    SEARCH_BOOK_AUTHOR = Entry(window)
    SEARCH_BOOK_AUTHOR.place(x= 250, y= 160,relwidth=0.5,relheight=0.05)
    SEARCH_BOOK_AUTHOR.insert(0,csv_pull.loc[selected]["BOOK_AUTHOR"])
    BTN_BOOK_PUBLIC = Button(window, text='출판사', bg='orange', width='8', height='1')
    BTN_BOOK_PUBLIC.place(x=170, y = 200)
    SEARCH_BOOK_PUBLIC = Entry(window)
    SEARCH_BOOK_PUBLIC.place(x= 250, y= 200,relwidth=0.5,relheight=0.05)
    SEARCH_BOOK_PUBLIC.insert(0,csv_pull.loc[selected]["BOOK_PUBLIC"])
    BTN_BOOK_PRICE = Button(window, text='가격', bg='orange', width='8', height='1')
    BTN_BOOK_PRICE.place(x=170, y = 240)
    SEARCH_BOOK_PRICE = Entry(window)
    SEARCH_BOOK_PRICE.place(x= 250, y= 240,relwidth=0.5,relheight=0.05)
    SEARCH_BOOK_PRICE.insert(0,csv_pull.loc[selected]["BOOK_PRICE"])
    BTN_BOOK_LINK = Button(window, text='URL', bg='orange', width='8', height='1') 
    BTN_BOOK_LINK.place(x=170, y = 280)
    SEARCH_BOOK_LINK = Entry(window)
    SEARCH_BOOK_LINK.place(x= 250, y= 280,relwidth=0.5,relheight=0.05)
    SEARCH_BOOK_LINK.insert(0,csv_pull.loc[selected]["BOOK_LINK"])
    
    BTN_BOOK_DESCRIPTION = Button(window, text='도서 설명', bg='orange', width='8', height='1')
    BTN_BOOK_DESCRIPTION.place(x=170, y = 320)
    SEARCH_BOOK_DESCRIPTION = Entry(window)
    SEARCH_BOOK_DESCRIPTION.place(x= 250, y= 320,relwidth=0.5,relheight=0.05)
    SEARCH_BOOK_DESCRIPTION.insert(0,csv_pull.loc[selected]["BOOK_DESCRIPTION"])
    BTN_IMAGE_FIND = Button(window, text='사진 찾기', bg='orange', width='8', height='1')
    BTN_IMAGE_FIND.place(x=170, y = 360)
    SEARCH_IMAGE_FIND = Entry(window)
    SEARCH_IMAGE_FIND.place(x= 250, y= 360,relwidth=0.5,relheight=0.05)
    #SEARCH_IMAGE_FIND.insert(0,csv_pull.loc[selected]["BOOK_IMAGE"])




    def find_image_name():
        file_name=askopenfilename(parent=window,filetype=(("PNG파일", "*.png"),("모든 파일","*.*")))
        photo=PhotoImage(file=file_name,master=window)
        IMAGE_label.configure(image=photo)
        IMAGE_label.image=photo
        SEARCH_IMAGE_FIND.insert(0,file_name)
    
    BTN_FIND=Button(window, text="찾아보기",bg='gray',width='8',height='1',command=find_image_name)
    BTN_FIND.place(x=620,y=360)
    #중복확인 시, 예외처리
    def ERROR_1():   # 예외처리 1
        tkinter.messagebox.showinfo("ERROR","해당 도서는 등록 가능 합니다 !")
    def ERROR_2():   # 예외처리 2
        tkinter.messagebox.showerror("ERROR","해당 도서는 등록 불가능 합니다 !")
    def ERROR_3():   # 예외처리 3
        tkinter.messagebox.showerror("ERROR","중복 확인 후 도서 등록이 가능합니다 !")
    def ERROR_4():   # 예외처리 4
        tkinter.messagebox.showerror("ERROR","가격은 정수로만 입력 가능합니다 !")
    def ERROR_5():   # 예외처리 5
        tkinter.messagebox.showerror("ERROR","해당 정보는 숫자로만 입력이 가능합니다 !")
    def ERROR_6():   # 예외처리 6
        tkinter.messagebox.showerror("ERROR","해당 정보는 필수정보 입니다. 다시 작성해주세요 !")
    
    def APPLY():  # 확인,적용  버튼 눌렀을 시
        MSB = tkinter.messagebox.askquestion ('도서 수정','도서를 수정 하시겠습니까?')
        if MSB == 'yes':
            a = SEARCH_BOOK_ISBN.get()
            b = SEARCH_BOOK_TITLE.get()
            c = SEARCH_BOOK_AUTHOR.get()
            d = SEARCH_BOOK_PUBLIC.get()
            e = SEARCH_BOOK_PRICE.get()
            f = SEARCH_BOOK_LINK.get()
            g = SEARCH_IMAGE_FIND.get()
            h = SEARCH_BOOK_DESCRIPTION.get()
            #i = SEARCH_BOOK_RENTAL
            #하나라도 입력하지 않았을 때
            if a.strip()=="" or b.strip()=="" or c.strip()=="" or d.strip()=="" or e.strip()=="" \
               or f.strip()=="" or g.strip()=="" or h.strip()=="":
                ERROR_6()
                return 0
            # 중복확인 안했을 때 
            if not OVERLAP_CHECK['state'] == 'disabled' :
                ERROR_3()
            # 가격이 정수가 아닐 때
            if not e.isdigit():
                ERROR_4()
                
            else:
                csv_pull = pd.read_csv("csv/book_1.csv",encoding = "utf-8")
                csv_pull = csv_pull.set_index("BOOK_ISBN")
                csv_pull.loc[selected, 'BOOK_TITLE']= b
                csv_pull.loc[selected, 'BOOK_AUTHOR']= c  
                csv_pull.loc[selected, 'BOOK_PUBLIC']= d 
                csv_pull.loc[selected, 'BOOK_PRICE']= int(e)
                csv_pull.loc[selected, 'BOOK_LINK']= f
                csv_pull.loc[selected, 'BOOK_IMAGE']= g
                csv_pull.loc[selected, 'BOOK_DESCRIPTION']= h
                #csv_pull.loc[a, 'BOOK_RENTAL']= "FALSE"
                #csv 저장하기 
                csv_pull.to_csv("csv/book_1.csv", index = True)
                print(tabulate(csv_pull, headers='keys', tablefmt='psql',numalign='left',stralign='left'))
                window.destroy()
    def ISBN_OVERLAP():
        csv_pull = pd.read_csv("csv/book_1.csv",encoding = "utf-8")
        csv_pull = csv_pull.set_index("BOOK_ISBN")
        
        a = SEARCH_BOOK_ISBN.get()
        ISBN_OVERLAP = csv_pull.index.tolist()
        if  a in ISBN_OVERLAP:
            ERROR_2()
            
        elif not a.isdigit():
            ERROR_5()
                
        else :
            ERROR_1()
            # 중복 확인 완료시 버튼 비활성화 
            OVERLAP_CHECK['state'] = 'disabled'
            SEARCH_BOOK_ISBN['state'] = 'disabled'
    # 중복확인시 이벤트 발생 추가
    OVERLAP_CHECK = Button(window, text='중복확인', bg='orange', width='7', height='1',
                           command = ISBN_OVERLAP)
    OVERLAP_CHECK.place(x=620, y = 80)

        # 적용 버튼 누를 시 수정!
    BTN_APPLY = Button(window, text='적용', bg = 'gray', width='7', height='1',command=APPLY)
    BTN_APPLY.place(x=300, y = 420)

    BTN_APPLY.place(x=300, y = 420)

    BTN_CANCEL = Button(window, text='취소', bg='gray', width='7', height='1',command=window.destroy )
    BTN_CANCEL.place(x=400, y = 420)
    
# ㉯의 화면----------------------------------------------------
def BOOK_LOOKUP():
    window = Tk()
    window.title('도서 조회/대출')
    window.geometry("700x500")
    label1 = Label(window, text = '도서 조회/대출', bg ='gray', width = 700, height = 5)
    window.configure(background = 'sky blue')
    label1.pack()
    
    def BTN_EDIT(a, b, c, d,e, f,g):
        a = Button(window, text=b, bg=c, width=d, height=e)
        a.place(x=f, y = g)    
    def BLANK(a,b,c,d,e) :
        a = Entry(window)
        a.place(x= b, y= c,relwidth=d,relheight=e)
    BTN_CANCEL = Button(window, text='뒤로가기', bg='orange',
     width='8', height='2',command=window.destroy)
    BTN_CANCEL.place(x=5,y=25)
    
    BTN_SEARCH = Button(window, text='도서 검색', bg='orange')         
    BTN_SEARCH.place(relx=0.001,rely=0.2,relwidth = 0.1,relheight=0.05)

    BLANK_SEARCH = Entry(window)
    BLANK_SEARCH.place(relx=0.11,rely=0.2,relwidth=0.7,relheight=0.05)
# Treeview---------------------------------------------------------------------
    # csv 파일 가져오기
    csv_pull = pd.read_csv("csv/book_1.csv",encoding = "utf-8")
    csv_pull = csv_pull.set_index("BOOK_ISBN")

    # 도서 목록 창 (Treeview)
    BOOK_SELECT_BOX = ttk.Treeview(window, columns=(1,2,3,4),show="headings")

    # 필드명
    BOOK_SELECT_BOX.heading(1, text='ISBN')
    BOOK_SELECT_BOX.heading(2, text='도서명')
    BOOK_SELECT_BOX.heading(3, text='저자')
    BOOK_SELECT_BOX.heading(4, text='출판사')
    # 기본 너비 
    BOOK_SELECT_BOX.column(1, width='170')
    BOOK_SELECT_BOX.column(2, width='130')
    BOOK_SELECT_BOX.column(3, width='120')
    BOOK_SELECT_BOX.column(4, width='80')
    #스크롤바 (안생기는데 왜 안생기는지 모르겠음)
    scroll = ttk.Scrollbar(window, orient="vertical", command=BOOK_SELECT_BOX.yview)
    scroll.pack(side='right', fill='y')
    BOOK_SELECT_BOX.configure(yscrollcommand=scroll.set)

    # 목록 출력할 데이터 
    # 데이터 프레임 출력

    for ISBN in csv_pull.index.tolist():
        book_title = csv_pull.loc[ISBN, "BOOK_TITLE"]
        book_author = csv_pull.loc[ISBN, "BOOK_AUTHOR"]
        book_publish = csv_pull.loc[ISBN, "BOOK_PUBLIC"]

        book_add = (ISBN, book_title, book_author, book_publish)
        BOOK_SELECT_BOX.insert("","end",text="",value=book_add,iid=book_add[0])

    def click_item(event):
        window = Tk()

    BOOK_SELECT_BOX = Listbox(window, highlightcolor = 'blue') # 선택시 파란색으로 표시
    
    BOOK_SELECT_BOX.insert(0,"도서명 : 불멸의 이순신 / 저자 : 윤도운")
    BOOK_SELECT_BOX.insert(1,"도서명 : 동물농장 / 저자 : 조지 오웰")
    BOOK_SELECT_BOX.insert(2,"도서명 : 1984 / 저자 : 조지 오웰")
    # 더블 클릭시 이벤트 발생 
    BOOK_SELECT_BOX.bind('<Double-Button-1>', click_item)

    BOOK_SELECT_BOX.place(relx=0.01,rely=0.28,relwidth=0.8,relheight = 0.4)

#--------------------------반납,대출 버튼 이벤트----------------------
    #num=0
    def event_book_rent():
        
        book_df = pd.read_csv("csv/book_1.csv",encoding = "utf-8")
        #user_df = pd.read_csv("csv/user.csv",encoding = "utf-8")
        rent_df = pd.read_csv("csv/rent.csv",encoding = "utf-8")

        today_D = datetime.now().date() # datetime 모듈이용하여 현재 날짜 저장
        return_D = today_D+timedelta(weeks=2) # timedelta 함수 이용 2주뒤 날짜 저장
        #rent_isbn = book_df[book_df['BOOK_ISBN'] == isbn] # 도서테이블에서 도서 ISBN 값이 담긴 isbn 변수로 값 저장
        #rent_phone = user_df[user_df['USER_PHONE'] == u_phone] # 회원테이블에서 회원 전화번호값이 담긴 u_phone 변수로 값 저장

        new_rent = { "RENT_NUM": 1,
                 "RENT_DATE": today_D,
                 "RENT_RDATE": return_D,
                 "RENT_RYN": False}
                 #"BOOK_ISBN": rent_isbn}# 숫자대신 (rent_isbn) 변수가 들어가야함,
                 #"USER_PHONE": rent_phone}# '숫자'대신 (rent_phone)변수가 들어가야함}

        rent_df = rent_df.append(new_rent, ignore_index=True)
        # book 데이터프레임에서 BOOK_RENTAL의 num 번째를 True로 변경
        # (임의)rent_cnt는 user테이블에서 대여권수가 담긴 변수
        print(tabulate(rent_df,headers='keys',tablefmt='pretty',showindex=False,numalign='center',stralign='center'))
       # num += 1
        tkinter.messagebox.showinfo("도서 대출", "도서 대출 완료")

    def event_book_return():
         book_df = pd.read_csv("csv/book_1.csv",encoding = "utf-8")
         #user_df = pd.read_csv("csv/user.csv",encoding = "utf-8")
         rent_df = pd.read_csv("csv/rent.csv",encoding = "utf-8")

        # idx = rent_df[rent_df['RENT_NUM'] == num].index # RENT_NUM 속성에서 num번째 값을 인덱스로 저장
         #rent_df.drop(idx,inplace=True) # num # 인덱스로 저장한 idx를 참고하여 drop(), 해당 행 삭제
         # book 데이터프레임에서 BOOK_RENTAL의 num 번째를 False로 변경
         # (임의)rent_cnt는 user테이블에서 대여권수가 담긴 변수
         tkinter.messagebox.showinfo("도서 반납", "도서 반납 완료")
#---------------------------------------------------------------------------

    BOOK_SEARCH_BTN = Button(window, text = '검색', fg='white' ,bg='black')
    BOOK_SEARCH_BTN.place(relx=0.82,rely=0.2,relwidth=0.1,relheight = 0.05)
    BOOK_INF = Button(window, text = '선택하기', fg='white', bg = 'black')
    BOOK_INF.place(relx=0.82,rely=0.28,relwidth=0.1,relheight=0.05)
    infobutton = Button(window, text = '도서 상세 정보')
    infobutton.place(relx=0.01,rely=0.7,relwidth=0.2,relheight=0.07)
    rent_button=Button(window,text='대출하기',bg='gray',command=event_book_rent)
    rent_button.place(relx=0.82,rely=0.58,relwidth=0.1,relheight=0.1)
    return_button=Button(window,text='반납하기',bg='gray',command=event_book_return)
    return_button.place(relx=0.82,rely=0.68,relwidth=0.1,relheight=0.1)
    
    
    
# ㉰의 화면----------------------------------------------------
def BOOK_DELETE():
    #공통부분 ↓-----------------------------------------------------------------------
    window = tkinter.Tk()
    window.title("도서 삭제")
    window.geometry("700x500")
    label1 = Label(window, text = '도서 삭제', bg = 'gray',width = 700, height = 5)
    window.configure(background = 'sky blue')
    #공통부분 ↑-----------------------------------------------------------------------
    label2 = Label(window, text='삭제할 도서 검색하기 :',fg='black' ,
                   font=('맑은 고딕',10), width=20,height=1)
    BTN_CANCEL = Button(window, text='뒤로가기', bg='orange'
    , width='8', height='2',command=window.destroy)
    def DLT_ASK():
        tkinter.messagebox.askquestion("도서 삭제"," (책 이름)을 삭제하시겠습니까?")
    def DLT_DONE():
        tkinter.messagebox.showinfo("삭제 완료"," (책 이름)을 삭제되었습니다 !")
        tkinter.messagebox.askquestion("삭제 완료"," (책 이름)을 삭제되었습니다 !")
    def DLT_ERROR():
        tkinter.messagebox.showerror("삭제 실패"," 해당 도서를 반납하고 삭제해주세요 !")

    def DLT_BOOK():
        csv_pull = pd.read_csv("csv/book_1.csv",encoding = "utf-8")
        csv_pull = csv_pull.set_index("BOOK_ISBN")

        MB = tkinter.messagebox.askquestion("도서 삭제", "을 삭제하시겠습니까?")
        #if MB == "yes":
        #    if BOOK_RENTAL == True :    도서 정보 가져와야함 / 아직 구현 X
        #        messagebox.showerror("삭제 오류", " 이미 대출 중인 도서입니다.")

         #   else:
         #       csv_pull.drop



    # 레이블 1 
    label3 = Label(window, text='도서명 혹은 저자로 검색해주세요 ↓',fg='black' ,
                   font=('맑은 고딕',10), width=30,height=1)         

    # 레이블 2
    #tkinter.messagebox.askquestion("삭제 실패"," 해당 도서를 반납하고 삭제해주세요 !")

    BOOK_SEARCH_LABEL = Entry(window)
    BOOK_SEARCH_LABEL.insert(END, "도서명 혹은 저자를 입력하세요")
    BOOK_SEARCH_LABEL.place(relx=0.25,rely=0.3,relwidth=0.6,relheight=0.07)

    # 버튼 1
    BOOK_SEARCH_BTN = Button(window, text = '검색', fg='white' ,bg='black')
    BOOK_SEARCH_BTN.place(relx=0.86,rely=0.3,relwidth=0.1,relheight = 0.07)

    # 버튼 2
    BOOK_SELECT_BTN = Button(window, text = '선택하기', fg='white', bg = 'black', command = DLT_BOOK)
    BOOK_SELECT_BTN.place(relx=0.86,rely=0.4,relwidth=0.1,relheight=0.05)

    # csv 파일 가져오기
    csv_pull = pd.read_csv("csv/book_1.csv",encoding = "utf-8")
    csv_pull = csv_pull.set_index("BOOK_ISBN")

    # 도서 목록 창 (Treeview)
    BOOK_SELECT_BOX = ttk.Treeview(window, columns=(1,2,3,4), height = 13,show="headings")

    BOOK_SELECT_BTN = Button(window, text = '선택하기', fg='white', bg = 'black',command=DLT_BOOK)
    BOOK_SELECT_BOX = Listbox(window, width=70, height = 8, highlightcolor = 'blue') # 선택시 파란색으로 표시
    BOOK_SELECT_BOX.place(relx=0.25,rely=0.4,relwidth=0.6,relheight = 0.5)
    BOOK_SELECT_BOX.insert(0,"도서명 : 불멸의 이순신 / 저자 : 윤도운")
    BOOK_SELECT_BOX.insert(1,"도서명 : 동물농장 / 저자 : 조지 오웰")
    BOOK_SELECT_BOX.insert(2,"도서명 : 1984 / 저자 : 조지 오웰")
    BOOK_SELECT_BTN = Button(window, text = '선택하기', fg='white', bg = 'black', command = DLT_ASK)
    BOOK_SELECT_BTN.place(relx=0.86,rely=0.4,relwidth=0.1,relheight=0.05)

    # 필드명
    BOOK_SELECT_BOX.heading(1, text='ISBN')
    BOOK_SELECT_BOX.heading(2, text='도서명')
    BOOK_SELECT_BOX.heading(3, text='저자')
    BOOK_SELECT_BOX.heading(4, text='출판사')
    # 기본 너비 
    BOOK_SELECT_BOX.column(1, width='170')
    BOOK_SELECT_BOX.column(2, width='130')
    BOOK_SELECT_BOX.column(3, width='120')
    BOOK_SELECT_BOX.column(4, width='80')
    #스크롤바 (안생기는데 왜 안생기는지 모르겠음)
    scroll = ttk.Scrollbar(window, orient="vertical", command=BOOK_SELECT_BOX.yview)
    scroll.pack(side='right', fill='y')
    BOOK_SELECT_BOX.configure(yscrollcommand=scroll.set)

    # 목록 출력할 데이터 
    # 데이터 프레임 출력

    for ISBN in csv_pull.index.tolist():
        book_title = csv_pull.loc[ISBN, "BOOK_TITLE"]
        book_author = csv_pull.loc[ISBN, "BOOK_AUTHOR"]
        book_publish = csv_pull.loc[ISBN, "BOOK_PUBLIC"]

        book_add = (ISBN, book_title, book_author, book_publish)
        BOOK_SELECT_BOX.insert("","end",text="",value=book_add,iid=book_add[0])

    def click_item(event):
        DLT_BOOK()

    # 더블 클릭시 이벤트 발생 
    BOOK_SELECT_BOX.bind('<Double-Button-1>', click_item)

    BOOK_SELECT_BOX.place(x=90, y=200)
    BTN_CANCEL.pack()
    BTN_CANCEL.place(x=5,y=25)
    label1.pack()
    label2.pack()
    label3.place(x=177, y=125)
    label2.place(x=5, y=155)


   
    
  
# 첫번째 화면(메인화면)--------------------------------------------------------------------------------
window = Tk()
window.title("도서관리 프로그램")
window.geometry("700x500")
label1 = Label(window, text = '도서관리프로그램', bg = 'gray', width = 700, height = 5)
window.configure(background = 'sky blue')
#도서관리 누르면 2번째 창으로 넘어감
BTN_BOOK = Button(window, text='도서관리',fg="black", bg="orange", width='20',
                      height='10', command=BOOK_MANAGEMENT)
                      
# 우선적으로 해당 파일에서 회원관리 클릭시 프로그램 종료!                  
BTN_MEMBER = Button(window, text='회원관리',fg="black", bg="orange", width='20',
                        height='10')
label1.pack()
BTN_BOOK.pack()
BTN_BOOK.place(x=150,y=150)
BTN_MEMBER.pack()
BTN_MEMBER.place(x=450,y=150)
window.mainloop()