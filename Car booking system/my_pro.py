import random
import sqlite3
from tkinter import *
from tkinter.messagebox import *
import splash
splash.splashscreen()
admin=Tk()
a=PhotoImage(file='lpu1.gif')
Label(admin,image=a).grid(row=1,column=3)
admin.configure(bg='Black')


Label(admin,text='Login Page',font='times 20 bold italic',bd=7,relief=SUNKEN).grid(row=0,column=2,columnspan=5)
Label(admin,text='USERNAME',font='times 10 bold italic',bg='Steel Blue',bd=3).grid(row=2,column=2,sticky='W')
a1=Entry(admin,bd=5,bg='Steel Blue')
a1.grid(row=2,column=4)

Label(admin,text="PASSWORD",font='times 10 bold italic',bg='Steel Blue',bd=3).grid(row=4,column=2,sticky='W')
a2=Entry(admin,show='*',bd=5,bg='Steel Blue')
a2.grid(row=4,column=4)
def login():
    if((a1.get())=="lpucabs" and (a2.get())=='ishan'):
        showinfo('Welcome',"Your Entry is Successful")
        admin.destroy()

        root=Tk()
        root.configure(bg='Steel Blue')
        root.geometry("800x800+0+0")
        root.title('LPU CABS SERVICE')

        Tops = Frame(root,width=1600,bg='Black',relief=SUNKEN)
        Tops.pack(side=TOP)

        fm1=Frame(root,width=300,height=700,bd=5,bg='Light Steel Blue',relief=SUNKEN)
        fm1.pack()

        Label(Tops,font=('arial',30,'bold'),text='LPU CABS SERVICE',fg='Royal Blue',relief=SUNKEN,bd=20,anchor='w').grid(row=0,column=0)

        Label(Tops,font=('arial',13,),text="PHAGWARA JALANDHAR(144411)\n Contact-+91-8433130068,+91-9671896569    Email:- rvnarwal13@gmail.com\n#ROAD CHASERS",bg='Red',fg='Black',relief='ridge',anchor='w').grid(row=1,column=0)

        Label(Tops,font=('arial',15,'bold'),text='NEW THINKING. \n NEW POSSIBILITES.',bg='Green',fg='Red',anchor='w',relief='solid').grid(row=2,column=0)

        def suv():
            
            rootsuv=Toplevel()
           
            rootsuv.configure(bg='Thistle')
            rootsuv.geometry("600x600+0+0")
            rootsuv.title('CABS')

            fsuv1=Frame(rootsuv,bd=5,bg='Light Steel Blue',relief=SUNKEN)
            fsuv1.pack(side=LEFT)

            vrsuv=IntVar()

            Label(fsuv1,text="RULE THE ROAD'S WITH \nALL NEW POWERFUL LPU CAB'S",font='arial 25',fg='Indian Red',bd=5,relief=SUNKEN).grid(row=0,column=0,columnspan=7)
 
            Radiobutton(fsuv1,text='Audi',variable=vrsuv,value=1,font='times 20 bold').grid(row=3,column=3,padx=5,pady=5)
            Radiobutton(fsuv1,text='Mercedes',variable=vrsuv,value=2,font='times 20 bold').grid(row=6,column=3,padx=5,pady=5)
            Radiobutton(fsuv1,text='BMW',variable=vrsuv,value=3,font='times 20 bold').grid(row=9,column=3,padx=5,pady=5)


            def viewsuv():
                if vrsuv.get()==1:
                    FirstScreen = Toplevel()
                    FirstScreen.geometry("1920x1080+0+0")
                    FirstScreen.title("Mercedes")
                    WelcomePic = PhotoImage(file="F:\new\10-mercedes-car-png-image-thumb.png")
                    WelcomePicPlacement = Label(FirstScreen, image=WelcomePic)
                    WelcomePicPlacement.pack(side="top", fill="both")
                    FirstScreen.mainloop()
                elif vrsuv.get()==2:
                    FirstScreen = Toplevel()
                    FirstScreen.geometry("1920x1080+0+0")
                    WelcomePic = PhotoImage(file="F:\new\12.png")
                    WelcomePicPlacement = Label(FirstScreen, image=WelcomePic)
                    WelcomePicPlacement.pack(side="top")
                    FirstScreen.mainloop()
                else:
                    FirstScreen = Toplevel()
                    FirstScreen.geometry("1920x1080+0+0")
                    WelcomePic = PhotoImage(file="F:\new\15.png")
                    WelcomePicPlacement = Label(FirstScreen, image=WelcomePic)
                    WelcomePicPlacement.pack(side="top")
                    FirstScreen.mainloop()


            def exitsuv():
            
                rootsuv.destroy()
            Button(fsuv1,text='EXIT',width=10,height=5,bg='Indian Red',bd=10,command=exitsuv).grid(row=10,column=0)
            Button(fsuv1,text="VIEW",width=10,height=5,bg='Blanched Almond',bd=10,command=viewsuv).grid(row=10,column=4)

        def showlist():
            show = Tk()
            show.configure(bg='Light Steel Blue')
            Label(show,text="Booking_ID  Customer _Name Customer_UID  Car_Name  FROM      TO       Payment_Mode", font='times 20',width=150).pack()
            con = sqlite3.Connection('book')
            cur = con.cursor()
            cur.execute('select * from bookings')
            con.commit()
            a = cur.fetchall()
            j = 0
            while j < len(a):
                b = [str(i[0]) for i in a]
                b = str(b[j])
                c = [str(i[1]) for i in a]
                c = str(c[j])
                d = [str(i[2]) for i in a]
                d = str(d[j])
                e = [str(i[3]) for i in a]
                e = str(e[j])
                f = [str(i[4]) for i in a]
                f = str(f[j])
                g = [str(i[5]) for i in a]
                g = str(g[j])
                h = [str(i[6]) for i in a]
                h = str(h[j])
                Label(show,text=b + '                 ' + c + '          ' + d + '              ' + e + '               ' + f + '              ' + g + '              ' + h,bg='Light Steel Blue', font='times 18').pack()
                j = j + 1

        def booking():
            def book():
                if bk1.get() == '' or bk2.get() == '':
                    showerror("Invalid Entry", "Entry valid details")
                else:
                    con = sqlite3.Connection('book')
                    cur = con.cursor()
                    cur.execute('create table if not exists bookings(bookid number(10),cust_name varchar(20),cust_uid varchar(10),car_name varchar(20),booking_amt number(7),delivery_date varchar(9),Mode_of_payment varchar(20))')
                    if vrsuvx.get()==1:
                        x='AUDI'
                    elif vrsuvx.get()==2:
                        x='MERCEDES'
                    else:
                        x='BMW'
                    if vrsuvp.get()==1:
                        Y='UPI'
                    elif vrsuvp.get()==2:
                        Y='CREDIT CARD'
                    else:
                        Y='DEBIT CARD'
                    a = [(bid, bk1.get(), bk2.get(), x, bk5.get(), bk6.get(),Y )]
                    cur.executemany('insert into bookings values(? ,?    ,?  ,? ,?,?,?)', a)
                    con.commit()
                    cur.execute('select * from bookings')
                    a = cur.fetchall()
                    print(a)
                    showinfo("Congratulations!!", "You have successfully booked your car \n Your Cab will be on Time.")

            rootbook=Toplevel()
            rootbook.configure(bg='Beige')
            rootbook.geometry("5600x2800+0+0")
            rootbook.title('BOOKING')
            fbook1=Frame(rootbook,width=5600,height=2800,bd=20,bg='Light Steel Blue',relief=SUNKEN)
            fbook1.pack(side=LEFT)

            Label(fbook1,text="BOOK HERE",font='arial 25',fg='Indian Red',bd=5,relief=SUNKEN).grid(row=0,column=0,columnspan=7)   

            Label(fbook1,text="Booking Id:",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=1,column=1,sticky='W')
            bid = random.randint(1000, 5000)
            bk1=Label(fbook1,text=bid,fg='Black',bd=5)
            bk1.grid(row=1,column=3)
            Label(fbook1,text="Customer's Name:",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=2,column=1,sticky='W')
            bk1=Entry(fbook1,width=16,bd=5,font='arial 20')
            bk1.grid(row=2,column=3)
            Label(fbook1,text="Customer's UID:",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=3,column=1,sticky='W')
            bk2=Entry(fbook1,width=16,bd=5,font='arial 20')
            bk2.grid(row=3,column=3)

            Label(fbook1,text="Car Name:",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=4,column=1,sticky='W')
            vrsuvx = IntVar()
            Radiobutton(fbook1,text='Audi',variable=vrsuvx,value=1,font='times 20 bold').grid(row=4,column=2,padx=5,pady=5)
            Radiobutton(fbook1,text='Mercedes',variable=vrsuvx,value=2,font='times 20 bold').grid(row=4,column=3,padx=5,pady=5)
            Radiobutton(fbook1,text='BMW',variable=vrsuvx,value=3,font='times 20 bold').grid(row=4,column=4,padx=5,pady=5)

            Label(fbook1,text="Booking Amount:",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=5,column=1,sticky='W')
            bidamount=random.randint(100,500)
            bk4 = Label(fbook1, text=bidamount, fg='Black', bd=5)
            bk4.grid(row=5,column=3)
            Label(fbook1,text="From : ",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=6,column=1,sticky='W')
            bk5=Entry(fbook1,width=16,bd=5,font='arial 20')
            bk5.grid(row=6,column=3)
            Label(fbook1,text="To : ",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=7,column=1,sticky='W')
            bk6=Entry(fbook1,width=16,bd=5,font='arial 20')
            bk6.grid(row=7,column=3)
            Label(fbook1,text="Mode of Payment:",font='arial 25',fg='Black',bd=5,relief=SUNKEN).grid(row=8,column=1,sticky='W')
            vrsuvp = IntVar()
            Radiobutton(fbook1, text='UPI', variable=vrsuvp, value=1, font='times 20 bold').grid(row=8, column=2,padx=5, pady=5)
            Radiobutton(fbook1, text='CREDIT_CARD', variable=vrsuvp, value=2, font='times 20 bold').grid(row=8, column=3,padx=5, pady=5)
            Radiobutton(fbook1, text='DEBIT_CARD', variable=vrsuvp, value=3, font='times 20 bold').grid(row=8, column=4,padx=5, pady=5)

            def exitbook():
                rootbook.destroy()
            Button(fbook1,text='EXIT',font='times 20 bold',width=8,height=1,bd=10,bg='Indian Red',command=exitbook).grid(row=9,column=2)

            Button(fbook1,text='BOOK',font='times 20 bold',width=8,height=1,bd=10,bg='Pale Goldenrod',command=book).grid(row=9,column=4)

        def exitmain():
            root.destroy()
        Button(fm1,text='EXIT',font='times 20 bold',width=13,height=2,bd=10,bg='Indian Red',command=exitmain).grid(row=6,column=3)
        Button(fm1,text='GALLERY',font='times 20 bold',width=13,height=2,bd=10,bg='Thistle',command=suv).grid(row=2,column=3)
        Button(fm1,text='BOOK NOW',font='times 20 bold',width=13,height=2,bd=10,bg='Pale Goldenrod',command=booking).grid(row=5,column=5)
        Button(fm1,text='BOOKING LIST',font='times 20 bold',width=13,height=2,bd=10,bg='Pale Goldenrod',command=showlist).grid(row=5,column=2,pady=15)
    else:
         showerror('!OOPS','Invalid Username or Password')
def close():
    admin.destroy()

Button(admin,text="EXIT",command=close,width=5,height=2,bd=5,bg='Indian Red').grid(row=9,column=2)
Button(admin,text="LOGIN",command=login,width=5,height=2,bd=5,bg='Plum').grid(row=9,column=4)
admin.mainloop()




