from tkinter import *
from turtle import *

window = Tk()
window.geometry("700x600")
window.title("Bill")

# Destroy alert

def delete():
    screen.destroy()

# Define global variable

i1 = 0
i2 = 0
i3 = 0
i4 = 0
i5 = 0

# Alert window
def alert():
    global screen
    screen = Toplevel(window)
    screen.geometry("218x70")
    screen.title("Warning!")
    Label(screen, text="Please enter a number.", font='times 13 bold', fg='red').pack(anchor="center")
    # screen1.place(x=100, y=90).pack()
    button2 = Button(screen, text="Ok", command=delete).pack()
    # button2.place(x=180, y=60).pack()

# Calculate the Bill
def calculate():
    parata = item1.get()
    daal_bhaji = item2.get()
    egg = item3.get()
    chicken_curry = item4.get()
    tea = item5.get()

    try:
        global i1
        if parata == "":
            parata = 0
        i1 = int(float(parata))
    except ValueError:
        alert()
        print(parata, "is not a number")

    try:
        global i2
        if daal_bhaji == "":
            daal_bhaji = 0
        i2 = int(float(daal_bhaji))
    except ValueError:
        print(daal_bhaji, "is not a number")
        alert()

    try:
        global i3
        if egg == "":
            egg = 0
        i3 = int(float(egg))
    except ValueError:
        print(egg, "is not a number")
        alert()

    try:
        global i4
        if chicken_curry == "":
            chicken_curry = 0
        i4 = int(float(chicken_curry))
    except ValueError:
        print(chicken_curry, "is not a number")
        alert()

    try:
        global i5
        if tea == "":
            tea = 0
        i5 = int(float(tea))
    except ValueError:
        print(tea, "is not a number")
        alert()

    total = (i1 * 10 + i2 * 15 + i3 * 20 + i4 * 80 + i5 * 10)
    # total = (
    #     int(parata) * 10 + float(daal_bhaji) * 15 + float(egg) * 20 + float(chicken_curry) * 80 + float(tea) * 10
    # )
    vat = (total * 15) / 100
    final_total = total + vat

    label19 = Label(window, text=float(total), font=("times 15 bold"))
    label19.place(x=550, y=340)

    label20 = Label(window, text=float(vat), font=("times 15 bold"))
    label20.place(x=550, y=370)

    label21 = Label(window, text=float(final_total), font=("times 15 bold"))
    label21.place(x=550, y=400)

# ------------- Hotel name -----------------
label0 = Label(window, text="The Italian Hotel", font="times 30 bold", width=12,  foreground='dark blue')
label0.place(x=170, y=30)

#---------MENU----------

label1 = Label(window, text="MENU", font="times 16 bold", foreground='dark blue')
label1.place(x=50, y=100)

label2 = Label(window, text="Parata              : 10 Tk", font="times 15")
label2.place(x=50, y=140)

label3 = Label(window, text="Daal-Bhaji       : 15 Tk", font="times 15")
label3.place(x=50, y=170)

label4 = Label(window, text="Egg                   : 20 Tk", font="times 15")
label4.place(x=50, y=200)

label5 = Label(window, text="Chicken Curry  : 80 Tk", font="times 15")
label5.place(x=50, y=230)

label6 = Label(window, text="Tea                   : 10 Tk", font="times 15")
label6.place(x=50, y=260)

#-----------Billing Section------------

label7 = Label(window, text="BILL", font="times 16 bold", foreground='dark blue')
label7.place(x=400, y=100)

label8 = Label(window, text="Item", font="times 17 bold")
label8.place(x=350, y=130)

label9 = Label(window, text="Quantity", font="times 17 bold")
label9.place(x=518, y=130)

label10 = Label(window, text="Parata", font="times 15")
label10.place(x=350, y=170)

item1 = Entry(window)
item1.place(x=500, y=170)

label11 = Label(window, text="Daal-Bhaji", font="times 15")
label11.place(x=350, y=210)

item2 = Entry(window)
item2.place(x=500, y=210)

label12 = Label(window, text="Egg", font="times 15")
label12.place(x=350, y=240)

item3 = Entry(window)
item3.place(x=500, y=240)

label13 = Label(window, text="Chicken Curry", font="times 15")
label13.place(x=350, y=270)

item4 = Entry(window)
item4.place(x=500, y=270)

label14 = Label(window, text="Tea", font="times 15")
label14.place(x=350, y=300)

item5 = Entry(window)
item5.place(x=500, y=300)

label15 = Label(window, text="-----------------------------------------", font=("times 15 bold", 15))
label15.place(x=350, y=320)


label16 = Label(window, text="Total", font=("times 15 bold"))
label16.place(x=350, y=340)

label17 = Label(window, text="VAT 15%", font=("times 13 bold"))
label17.place(x=350, y=370)

label18 = Label(window, text="Payable Amount", font=("times 13 bold"))
label18.place(x=350, y=400)

button1 = Button(window, text="Calculate Bill", width=13, background='dark blue', foreground='white',
font=("times 15 bold"), command=calculate)
button1.place(x=230, y=500)

window.mainloop()
