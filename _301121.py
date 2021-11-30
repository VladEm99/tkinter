from tkinter import *

klik=0

def klikker(event):
    global klik
    klik+=1
    lbl.configure(text=klik)

def klikker1(event):
    global klik
    if klik>0:
        klik-=1
    else:
        klik=0
    lbl.configure(text=klik)
    
def text_to_lbl(event):
    text=ent.get()
    lbl.configure(text=text)
    ent.delete(0,END)

def valik():
    val=var.get() #value 1,2 voi 3
    ent.insert(END,str(val)+", ")
aken=Tk()
aken.title("akna nimetus")
aken.geometry("1920x1080")

btn=Button(aken,text="vajuta siia",font="Arial 20",fg="green",bg="lightblue",width=20,height=3)

lbl=Label(aken,text="zzz")
ent=Entry(aken,fg="blue",width=20,font="Arial 20")
var=IntVar() #StringVar()
var.set(3) #valib kolmas button отсчет от 1
r1=Radiobutton(aken,text="Esimene",variable=var,value=1,command=valik)
r2=Radiobutton(aken,text="Teine",variable=var,value=2,command=valik)
r3=Radiobutton(aken,text="Kolmas",variable=var,value=3,command=valik)
btn.bind("<Button-1>",klikker)#left_mouse_click
btn.bind("<Button-3>",klikker1)#right_mouse_click
ent.bind("<Return>",text_to_lbl)#enter
lbl.pack()
btn.pack()
ent.pack()
r1.pack()
r2.pack()
r3.pack()
aken.mainloop()

