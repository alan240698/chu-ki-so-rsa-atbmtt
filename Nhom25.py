# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from Tkinter import *
from PIL import Image, ImageTk
import ttk
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
import tkMessageBox
import tkFileDialog

root = Tk()
root.title("Digital signature")
key = RSA.generate(1024)
public_key = key.publickey()


def create_key():
    vK.set(public_key)
    vM.set(key)

def create_signature(text):
	#băm văn hản
    hash_1= SHA256.new(text).hexdigest()
    #tạo chữ ký
    signature = key.sign(hash_1,'')
    return signature

def check(signature, text_received):
    hash_2 = SHA256.new(text_received).hexdigest()
    if public_key.verify(hash_2, signature):
        tkMessageBox.showinfo("Thông Báo", "Văn bản toàn vẹn !")
    else:
        tkMessageBox.showerror("Thông Báo", "Văn bản không toàn vẹn !")

def click_create_signature():
    a = input_vanBan.get("1.0",'end-1c')
    chuky = create_signature(a)
    input_signature1.delete("1.0",'end-1c')
    input_signature1.insert(INSERT,chuky)
    input_signature2.delete("1.0",'end-1c')
    input_signature2.insert(INSERT,chuky)

def click_check():
    signature = tuple([long(input_signature1.get("1.0",'end-1c'))])
    check(signature, input_text_received.get("1.0",'end-1c'))




image = Image.open("background1.jpg")
photo = ImageTk.PhotoImage(image)
label_header = Label(image=photo,width=100,height=300)
#label_header.image = photo # keep a reference!
#label_header.pack()
label_header.pack(fill=BOTH, pady=5)


control = ttk.Notebook(root)
control.pack(fill=BOTH, expand=True, padx=5, pady=2)


content3 = Frame(control, relief="solid", bd=1)
content3.pack(fill=BOTH,side=TOP, expand=True, padx=5, pady=2,)

content = Frame(control, relief="solid", bd=1)
content.pack(fill=BOTH,side=TOP, expand=True, padx=5, pady=2)

content2 = Frame(control, relief="solid", bd=1)
content2.pack(fill=BOTH,side=TOP, expand=True, padx=5, pady=2)

control.add(content3, text='Giới thiệu')
control.add(content, text='Tạo chữ ký số')
control.add(content2, text='Xác thực chữ ký số')


'''Giới thiệu thông tin đề tài và thông tin sinh viên thực hiện'''
labelGT = Label(content3, text="BÁO CÁO AN TOÀN BẢO MẬT THÔNG TIN", fg="red", width=20, font=("Arial Bold", 30))
labelGT.pack(fill=BOTH, padx=20, pady=10)

labelGT = Label(content3, text="CHỮ KÝ SỐ RSA VÀ HASH", width=20, font=("Arial Bold", 30))
labelGT.pack(fill=BOTH, padx=50, pady=30)

labelNhom= Label(content3, text="NHÓM 25", width=20, font=("Arial Bold",15))
labelNhom.pack(fill=BOTH, padx=50, pady=10)

mssv1 = Label(content3, text="B1609830 - LÊ THANH LƯƠNG", font=("Arial Bold", 10))
mssv1.pack(fill=BOTH, padx=10)

mssv2 = Label(content3, text="B1611134 - TRẦN SĨ ĐẠT", font=("Arial Bold", 10))
mssv2.pack(fill=BOTH, padx=10)

mssv3 = Label(content3, text="B1609847 - ÔNG MINH THUẬN", font=("Arial Bold", 10))
mssv3.pack(fill=BOTH, padx=10)

mssv4 = Label(content3, text="B1611133 - NGUYỄN PHẠM ANH DUY", font=("Arial Bold", 10))
mssv4.pack(fill=BOTH, padx=10)

''' Tạo chữ kí số '''
text_taoKhoa = Frame(content)
text_taoKhoa.pack(fill=X, expand=True)
button_taoKhoa = Button(text_taoKhoa,font = "Verdana 10 bold", bg="#00CD00",fg="white",width=10,height=2, text="Tạo Khóa", command=create_key)
button_taoKhoa.pack(fill=Y, side=TOP)
label_public_key = Label(text_taoKhoa,font = "Verdana 10 bold", bg="yellow",fg="black",text="Puclic Key")
label_public_key.pack(fill=Y,side=LEFT, padx=130)
label_private_key = Label(text_taoKhoa,font = "Verdana 10 bold", bg="yellow",fg="black", text="Private Key")
label_private_key.pack(fill=Y, side=RIGHT, padx=130)

box_key = Frame(content)
box_key.pack(fill=X,  expand=True, padx = 5, pady= 5)
vK = StringVar()
box_public_key = Label(box_key, textvariable=vK, relief="solid", bd=2, width=60, height=6)
box_public_key.pack(fill=Y,side=LEFT)
vM = StringVar()
box_private_key = Label(box_key, textvariable=vM, relief="solid", bd=2, width=60, height=6)
box_private_key.pack(fill=Y, side=RIGHT)

box_vanBan = Frame(content)
box_vanBan.pack(fill=X,  expand=True)
label_vanBan= Label(box_vanBan, text="Plain Text",
font = "Verdana 10 bold", width=20, anchor=NW)
label_vanBan.pack(fill=X,side=LEFT, padx=10)
input_vanBan = Text(box_vanBan, height=4)
input_vanBan.pack(fill=X, side=LEFT)



box_create_signature = Frame(content)
box_create_signature.pack(fill=X,  expand=True, padx = 5, pady= 5)
button_create_signature = Button(box_create_signature, text="Tạo Chữ Ký", bg="blue",fg="white", width=10,height=2, font = "Verdana 10 bold", command=click_create_signature)
button_create_signature.pack( side=TOP)

box_signature = Frame(content)
box_signature.pack(fill=X,  expand=True)
lable_signature = Label(box_signature, text="Chữ Ký Số", font = "Verdana 10 bold", width=20, anchor=NW)
lable_signature.pack(fill=X,side=LEFT, padx=10)
input_signature1 = Text(box_signature, height=5)
input_signature1.pack(fill=X, side=BOTTOM)

ft1 = Frame(content)
ft1.pack(fill=Y,  expand=True,)
lblt1 = Label(ft1, height=50, anchor=NW)
lblt1.pack(fill=Y)


''' Xác thực chữ ký số'''
box_text_received = Frame(content2)
box_text_received.pack(fill=X,  expand=True)
lable_text_received = Label(box_text_received, text="Plain Text", font = "Verdana 10 bold", width=20, anchor=NW)
lable_text_received.pack(fill=X,side=LEFT, padx=10)
input_text_received = Text(box_text_received, height=4)
input_text_received.pack(fill=X, side=LEFT)

hr = Frame(content2)
hr.pack(fill=X,  expand=True, padx = 5, pady= 5)

box_signature = Frame(content2)
box_signature.pack(fill=X,  expand=True)
lable_signature = Label(box_signature, text="Chữ ký", width=20, font = "Verdana 10 bold",anchor=NW)
lable_signature.pack(fill=X,side=LEFT, padx=10)
input_signature2 = Text(box_signature, height=4)
input_signature2.pack(fill=X, side=LEFT)


box_click_check = Frame(content2)
box_click_check.pack(fill=X,  expand=True)
button_check = Button(box_click_check, text="Kiểm Tra", bg="red",fg="white", width=10,height=2, font = "Verdana 10 bold", command=click_check)
button_check.pack( side=TOP)

ft = Frame(content2)
ft.pack(fill=Y,  expand=True,)
lblt = Label(ft, height=50, anchor=NW)
lblt.pack(fill=Y)



root.resizable(0,0)
root.geometry("900x700")
root.mainloop()