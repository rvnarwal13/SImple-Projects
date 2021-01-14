from tkinter import *

def splash():
    root.destroy()
def splashscreen():
    global root
    root=Tk()
    q=PhotoImage(file='lpu1.gif')
    Label(root,image=q).grid(row=0,column=0)
   
    root.configure(bg='White')
    root.geometry("1000x800")
    Label(root,text="Car Booking System",font="Arial 30 ",bd=10,bg='Light Steel Blue',relief='ridge').grid(row=1,column=3)
    Label(root,text="Name",font="Arial 20 bold",bg='Light Steel Blue').grid(row=2,column=1,sticky='w',pady=10)
    Label(root,text=":",font="Arial 20 bold",bg='White').grid(row=2,column=2,pady=10)
    Label(root,text="AJAY & RAVI",font="Arial 20 bold",bg='Light Steel Blue').grid(row=2,column=3,sticky=E,pady=10)
    Label(root,text="Regestration Number",font="Arial 20 bold",bg='Light Steel Blue').grid(row=3,column=1,sticky='w',pady=10)
    Label(root,text=":",font="Aerial 20 bold",bg='White').grid(row=3,column=2,pady=10)
    Label(root,text="118013 69-75",font="Arial 20 bold",bg='Light Steel Blue').grid(row=3,column=3,sticky=E,pady=10)
    Label(root,text="Batch",font="Arial 20 bold",bg='Light Steel Blue').grid(row=4,column=1,sticky='w',pady=10)
    Label(root,text=":",font="Arial 20 bold",bg='White').grid(row=4,column=2,pady=10)
    Label(root,text="K18BH",font="Arial 20 bold",bg='Light Steel Blue').grid(row=4,column=3,sticky=E,pady=10)
    Label(root,text="Branch",font="Arial 20 bold",bg='Light Steel Blue').grid(row=5,column=1,sticky='w',pady=10)
    Label(root,text=":",font="Arial 20 bold",bg='White').grid(row=5,column=2,pady=10)
    Label(root,text="Computer Science",font="Arial 20 bold",bg='Light Steel Blue').grid(row=5,column=3,sticky=E,pady=10)
    Label(root,text="& Engineering",font="Arial 20 bold",bg='Light Steel Blue').grid(row=6,column=3,sticky=E,pady=10)
    Label(root,text="Course",font="Arial 20 bold",bg='Light Steel Blue').grid(row=7,column=1,sticky='w',pady=10)
    Label(root,text=":",font="Arial 20 bold",bg='White').grid(row=7,column=2,pady=10)
    Label(root,text="B.Tech (IInd Year)",font="Arial 20 bold",bg='Light Steel Blue').grid(row=7,column=3,sticky=E,pady=10)
    Label(root,text="EMail id",font="Arial 20 bold",bg='Light Steel Blue').grid(row=8,column=1,sticky='w',pady=10)
    Label(root,text=":",font="Arial 20 bold",bg='White').grid(row=8,column=2,pady=10)
    Label(root,text="rvnarwal13@gmail.com",font="Arial 20 bold",bg='Light Steel Blue').grid(row=8,column=3,sticky=E,pady=10)
    Label(root,text="Submitted To",font="Arial 20 bold",bg='Light Steel Blue').grid(row=9,column=1,sticky='w',pady=10)
    Label(root,text=":",font="Arial 20 bold",bg='White').grid(row=9,column=2,pady=10)
    Label(root,text="Mr. Ishaan Kumar",font="Arial 20 bold",bg='Light Steel Blue').grid(row=9,column=3,sticky=E,pady=10)
    root.after(7000,splash)
    root.mainloop()

