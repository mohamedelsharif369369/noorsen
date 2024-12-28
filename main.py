from tkinter import *
from tkinter import ttk
from db import DataBase
from tkinter import messagebox

db = DataBase("NOOR.db")

root = Tk()
root.title('NOOR')
root.geometry('1590x800+0+0')
root.resizable(True,True)
root.configure(bg='#2c3e50')

name = StringVar()
title = StringVar()
price = StringVar()
mdfo3 = StringVar()
tarekh = StringVar()
baqi = StringVar()
me3ad= StringVar()
phone = StringVar()

#logo = PhotoImage(file='noor.jpg')
#lbl_logo = Label(root,image=logo)
#lbl_logo.place(x=80,y=520)

# =================| Entries Frame |=======================

entries_frame = Frame(
    root,
    bg='#2c3e50'
    )
entries_frame.place(
    x=1,
    y=1,
    width=360,
    height=510
    )
Title = Label(
    entries_frame,
    text='NOOR COMPANY',
    font=('Calibri',18,'bold'),
    bg='#2c3e50',fg='white'
    )
Title.place(
    x=10,
    y=1
    )

lblPersonName = Label(
    entries_frame,
    text='           العميل',
    font=('Calibri',16),
    bg='#2c3e50',
    fg='white'
    )
lblPersonName.place(
    x=10,
    y=50
    )
txtPersonName = Entry(
    entries_frame,
    textvariable=name,
    width=20,
    font=('Calibri',16)
    ) 
txtPersonName.place(
    x=120,
    y=50
    )

lblProTitle = Label(
    entries_frame,
    text='          الخدمه',
    font=('Calibri',16),
    bg='#2c3e50',
    fg='white'
    )
lblProTitle.place(
    x=10,
    y=90
    )
txtProTitle = Entry(
    entries_frame,
    textvariable=title,
    width=20,
    font=('Calibri',16)
    ) 
txtProTitle.place(
    x=120,
    y=90
    )

lblProPrice= Label(
    entries_frame,
    text='           السعر',
    font=('Calibri',16),
    bg='#2c3e50',
    fg='white'
    )
lblProPrice.place(
    x=10,
    y=130
    )
txtProPrice= Entry(
    entries_frame,
    textvariable=price,
    width=20,
    font=('Calibri',16)
    ) 
txtProPrice.place(
    x=120
    ,y=130
    )

lblMdfo3 = Label(
    entries_frame,
    text='           مدفوع',
    font=('Calibri',16),
    bg='#2c3e50',
    fg='white'
    )
lblMdfo3.place(
    x=10,
    y=170
    )
txtMdfo3 = Entry(
    entries_frame,
    textvariable=mdfo3,
    width=20,
    font=('Calibri',16)
    ) 
txtMdfo3.place(
    x=120
    ,y=170
    )

lblTarekh = Label(
    entries_frame,
    text='           بتاريخ',
    font=('Calibri',16),
    bg='#2c3e50',
    fg='white'
    )
lblTarekh.place(
    x=10,
    y=210
    )
txtTarekh = Entry(
    entries_frame,
    textvariable=tarekh,
    width=20,
    font=('Calibri',16)
    ) 
txtTarekh.place(
    x=120
    ,y=210
    )

lblBaqi = Label(
    entries_frame,
    text='            الباقى',
    font=('Calibri',16),
    bg='#2c3e50',
    fg='white'
    )
lblBaqi.place(
    x=10,
    y=250
    )
txtBaqi = Entry(
    entries_frame,
    textvariable=baqi,
    width=20,
    font=('Calibri',16)
    ) 
txtBaqi.place(
    x=120
    ,y=250
    )

lblMe3ad = Label(
    entries_frame,
    text=' ميعاد التسليم',
    font=('Calibri',16),
    bg='#2c3e50',
    fg='white'
    )
lblMe3ad.place(
    x=10,
    y=290
    )
txtMe3ad = Entry(
    entries_frame,
    textvariable=me3ad,
    width=20,
    font=('Calibri',16)
    ) 
txtMe3ad.place(
    x=120
    ,y=290
    )

lblPhone = Label(
    entries_frame,
    text='    رقم الهاتف ',
    font=('Calibri',16),
    bg='#2c3e50',
    fg='white'
    )
lblPhone.place(
    x=10,
    y=330
    )
txtPhone = Entry(
    entries_frame,
    textvariable=phone,
    width=20,
    font=('Calibri',16)
    ) 
txtPhone.place(
    x=120
    ,y=330
    )

# =================| Defines |=============================

def hide():
    root.geometry("360x510")

def show():
    root.geometry('1590x800+0+0')
    

btnHide = Button(
    entries_frame,
    text='اخفاء',
    bg='white',
    bd=1,
    relief=SOLID,
    cursor='hand2',
    command=hide)
btnHide.place(
    x=270,
    y=10
    )

btnShow = Button(
    entries_frame,
    text='اظهار',
    bg='white',
    bd=1,
    relief=SOLID,
    cursor='hand2',
    command=show
    )
btnShow.place(
    x=310,
    y=10
    )

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    name.set(row[1])
    title.set(row[2])
    price.set(row[3])
    mdfo3.set(row[4])
    tarekh.set(row[5])
    baqi.set(row[6])
    me3ad.set(row[7])
    phone.set(row[8])

def displayAll():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert(
            "",
            END,
            values=row
            )

def delete():
    db.remove(row[0])
    clear()
    displayAll()
    
def clear():
    name.set("")
    title.set("")
    price.set("")
    mdfo3.set("")
    tarekh.set("")
    baqi.set("")
    me3ad.set("")
    phone.set("")

def add_emoloyee():
    if txtPersonName.get() == "" or txtProTitle.get() == "" or txtProPrice.get() == "" :
        messagebox.showerror(
            "Error",
            "من فضلك قم بملىء كافة الحقول"
            )
        return
    db.insert(
        txtPersonName.get(),
        txtProTitle.get(),
        txtProPrice.get(),
        txtMdfo3.get(),
        txtTarekh.get(),
        txtBaqi.get(),
        txtMe3ad.get(),
        txtPhone.get())
    #messagebox.showinfo("Success"," هل تريد اضافة خدمه جديده")
    clear()
    displayAll()

def update():
    if txtPersonName.get() == "" or txtProTitle.get() == "" or txtProPrice.get() == "" :
        messagebox.showerror(
            "Error",
            "من فضلك قم بملىء كافة الحقول"
            )
        return
    db.update(
        row[0],
        txtPersonName.get(),
        txtProTitle.get(),
        txtProPrice.get(),
        txtMdfo3.get(),
        txtTarekh.get(),
        txtBaqi.get(),
        txtMe3ad.get(),
        txtPhone.get()
        )
    #messagebox.showinfo("Success","هل تريد تعديل هذه الخدمه ؟")
    clear()
    displayAll()

# ============================| Buttons Frame |===========================================================

btn_frame = Frame(
    entries_frame,
    bg='#2c3e50',
    bd=1,
    relief=SOLID
    )
btn_frame.place(
    x=10,
    y=400,
    width=335,
    height=100
    )

btnAdd = Button(
    btn_frame,
    text='اضافة خدمه',
    width=14,
    height=1,
    font=('Calibri',16),
    fg='white',
    bg='#16a085',
    bd=0,
    command=add_emoloyee
    ).place(x=4,y=5)

btnUpdate = Button(
    btn_frame,
    text='تعديل الخدمه',
    width=14,
    height=1,
    font=('Calibri',16),
    fg='white',
    bg='#2980b9',
    bd=0,
    command=update
    ).place(x=4,y=50)
    
btnDelete = Button(
    btn_frame,
    text='حذف الخدمه',
    width=14,
    height=1,
    font=('Calibri',16),
    fg='white',
    bg='#c0392b',
    bd=0,
    command=delete
    ).place(x=170,y=5)

btnClear = Button(
    btn_frame,
    text='مسح الحقول',
    width=14,
    height=1,
    font=('Calibri',16),
    fg='white',
    bg='#f39c12',
    bd=0,
    command=clear
    ).place(x=170,y=50)

# ============================| Table Frame |===========================================================

tree_Frame = Frame(
    root,
    bg='white'
    )
tree_Frame.place(
    x=365,
    y=1,
    width=1230,
    height=795
    )

style = ttk.Style()

style.configure(
    "mystyle.Treeview",
    font=('Calibri',13),
    rowheight=50
    )
style.configure(
    "mystyle.Treeview.Heading",
    font=('Calibri',13)
    )

tv = ttk.Treeview(
    tree_Frame,
    columns=(1,2,3,4,5,6,7,8,9),
    style="mystyle.Treeview"
    )

tv.heading(
    "1",
    text="مسلسل"
    )
tv.column(
    "1",
    width="10"
    )

tv.heading(
    "2",
    text="العميل"
    )
tv.column(
    "2",
    width="120"
    )

tv.heading(
    "3",
    text="الخدمه"
    )
tv.column(
    "3",
    width="180"
    )

tv.heading(
    "4",
    text="السعر"
    )
tv.column(
    "4",
    width="10"
    )

tv.heading(
    "5",
    text="مدفوع"
    )
tv.column(
    "5",
    width="10"
    )

tv.heading(
    "6",
    text="بتاريخ")
tv.column(
    "6",
    width="90"
    )

tv.heading(
    "7",
    text="الباقى"
    )
tv.column(
    "7",
    width="10"
    )

tv.heading(
    "8",
    text="ميعاد التسليم"
    )
tv.column(
    "8",
    width="90"
    )

tv.heading(
    "9",
    text="رقم الهاتف"
    )
tv.column(
    "9",
    width="90"
    )

tv['show'] = 'headings'

tv.bind(
    "<ButtonRelease-1>",
    getData
    )

tv.place(
    x=1,
    y=1,
    height=794,
    width=1230
    )

displayAll()

root.mainloop()