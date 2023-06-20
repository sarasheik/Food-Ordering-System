from tkinter import*
import time
#import datetime

root = Tk()

#Window Resolution
width = root.winfo_screenwidth()
height = root.winfo_screenheight()
root.geometry(f'{width}x{height}')
root.configure(background='#f7E7CE')
root.title("restaurant")

#Frames
Tops = Frame(root, width=350, height=50, bd=12, relief="raise")
Tops.pack(side=TOP)
lblTitle = Label(Tops, font=("arial", 20, 'bold'), text="             Restaurant          ")
lblTitle.grid(row=0, column=0)

#Date and Time
localtime = time.asctime(time.localtime(time.time()))
lblInfo = Label(Tops, font=('arial', 20, 'bold'), text=localtime, bd=10, anchor='w')
lblInfo.grid(row=1, column=0)

#bottom frames
BottomMainFrame = Frame(root, width=450, height=80, bd=12, relief=SUNKEN)
BottomMainFrame.place(x=100,y=280)

f1left = Frame(BottomMainFrame, width=433, height=550, bd=4, relief='raise')
f1left.pack(side=LEFT)

f1middle= Frame(BottomMainFrame,width=433,height=550,bd=4,relief='raise')
f1middle.pack(side=LEFT)

f1right=Frame(BottomMainFrame,width=433,height=550,bd=4,relief='raise')
f1right.pack(side=LEFT)

#Left Frame(Starters/MainCourse)
varPannerTikka=StringVar()
varCheeseBalls=StringVar()
varAlooTikki=StringVar()
varCaesarSalad= StringVar()
varPannerMasala=StringVar()
varButterChicken=StringVar()
varBhendiFry=StringVar()
varPaneerMussalum= StringVar()

#Middle Frame(Breads/Desert)
varChapati=StringVar()
varGarlicNaan=StringVar()
varTandooriRoti=StringVar()
varButterNaan= StringVar()
varChocoLavaCake=StringVar()
varGulabJamun=StringVar()
varRasmalai=StringVar()
varJalebi= StringVar()

#Right frame(totals)
varsubtotal=StringVar()
varTotal=StringVar()
varsercharhge= StringVar()

class Order:
        def __init__(self):
                pass
        def total(self):
                if (varPannerTikka.get() == ""):
                        cp1 = 0
                else:
                        cp1 = float(varPannerTikka.get())
                if (varCheeseBalls.get() == ""):
                        cp2 = 0
                else:
                        cp2 = float(varCheeseBalls.get())
                if (varAlooTikki.get() == ""):
                        cp3 = 0
                else:
                        cp3 = float(varAlooTikki.get())
                if (varCaesarSalad.get() == ""):
                        cp4 = 0
                else:
                        cp4 = float(varCaesarSalad.get())
                if (varPannerMasala.get() == ""):
                        cp5 = 0
                else:
                        cp5 = float(varPannerMasala.get())
                if (varButterChicken.get() == ""):
                        cp6 = 0
                else:
                        cp6 = float(varButterChicken.get())
                if (varBhendiFry.get() == ""):
                        cp7 = 0
                else:
                        cp7 = float(varBhendiFry.get())
                if (varPaneerMussalum.get() == ""):
                        cp8 = 0
                else:
                        cp8 = float(varPaneerMussalum.get())
                if (varChapati.get() == ""):
                        cp9 = 0
                else:
                        cp9 = float(varChapati.get())
                if (varGarlicNaan.get() == ""):
                        cp10 = 0
                else:
                        cp10 = float(varGarlicNaan.get())
                if (varTandooriRoti.get() == ""):
                        cp11 = 0
                else:
                        cp11 = float(varTandooriRoti.get())
                if (varButterNaan.get() == ""):
                        cp12 = 0
                else:
                        cp12 = float(varButterNaan.get())
                if (varChocoLavaCake.get() == ""):
                        cp13 = 0
                else:
                        cp13 = float(varChocoLavaCake.get())
                if (varGulabJamun.get() == ""):
                        cp14 = 0
                else:
                        cp14 = float(varGulabJamun.get())
                if (varRasmalai.get() == ""):
                        cp15 = 0
                else:
                        cp15 = float(varRasmalai.get())
                if (varJalebi.get() == ""):
                        cp16 = 0
                else:
                        cp16 = float(varJalebi.get())
                cop1 = cp1 * 150
                cop2 = cp2 * 120
                cop3 = cp3 * 100
                cop4 = cp4 * 170

                cop5 = cp5 * 220
                cop6 = cp6 * 350
                cop7 = cp7 * 180
                cop8 = cp8 * 250

                cop9 = cp9 * 12
                cop10 = cp10 * 30
                cop11 = cp11 * 20
                cop12 = cp12 * 25

                cop13 = cp13 * 100
                cop14 = cp14 * 40
                cop15 = cp15 * 55
                cop16 = cp16 * 45

                subtotal=(cop1+cop2+cop3+cop4+cop5+cop6+cop7+cop8+cop9+
                          cop10+cop11+cop12+cop13+cop14+cop15+cop16)
                sercharge=((cop1+cop2+cop3+cop4+cop5+cop6+cop7+cop8+cop9+
                            cop10+cop11+cop12+cop13+cop14+cop15+cop16)/99)

                totals = (subtotal)+(sercharge)
                varsubtotal.set(subtotal)
                varTotal.set(totals)
                varsercharhge.set(sercharge)      
        def reset(self):
                varPannerTikka.set(" ")
                varCheeseBalls.set(" ")
                varAlooTikki.set(" ")
                varCaesarSalad.set(" ")
                varPannerMasala.set(" ")
                varButterChicken.set(" ")
                varBhendiFry.set(" ")
                varPaneerMussalum.set(" ")
                varChapati.set(" ")
                varGarlicNaan.set(" ")
                varTandooriRoti.set(" ")
                varButterNaan.set(" ")
                varChocoLavaCake.set(" ")
                varGulabJamun.set(" ")
                varRasmalai.set(" ")
                varJalebi.set(" ")
                varsercharhge.set(" ")
                varTotal.set(" ")
                varsubtotal.set(" ")
        #Exit
        def qexit(self):
                root.destroy()
food_order=Order()

# Food items entry for starters
starterscat= Label(f1left,text='        Starters',font=('arial',30,'bold'))
starterscat.grid()

# List to store the entry variables
entry_variables = [varPannerTikka, varCheeseBalls, varAlooTikki, varCaesarSalad]

# Menu items and their corresponding labels
menu_items = [
    ("Paneer Tikka", 150),
    ("Cheese Balls", 120),
    ("Aloo Tikki", 100),
    ("Caesar Salad", 170),
]

# Loop to create labels and entry fields dynamically
for i, (menu_item, price) in enumerate(menu_items):
    label_text = f"{menu_item}....(Rs.{price})"
    entry_variable = entry_variables[i]

    label = Label(f1left, font=('arial', 16, 'bold'), text=label_text, bd=5, anchor="w")
    label.grid(row=i + 1, column=0)

    entry = Entry(f1left, font=('arial', 16, 'bold'), textvariable=entry_variable, bd=5, insertwidth=5,
                  bg="white", justify='right', width=4)
    entry.grid(row=i + 1, column=1)

# Food items entry for main course
maincoursecat= Label(f1left,text='       Main Course',font=('arial',30,'bold'))
maincoursecat.grid()

# List to store the entry variables
entry_variables = [varPannerMasala, varButterChicken, varBhendiFry, varPaneerMussalum]

# Menu items and their corresponding labels
menu_items = [
    ("Paneer Masala", 220),
    ("Butter Chicken", 350),
    ("Bhendi Fry", 180),
    ("Paneer Mussalum", 250),
]
# Loop to create labels and entry fields dynamically
for i, (menu_item, price) in enumerate(menu_items):
    label_text = f"{menu_item}....(Rs.{price})"
    entry_variable = entry_variables[i]

    label = Label(f1left, font=('arial', 16, 'bold'), text=label_text, bd=5, anchor="w")
    label.grid(row=i + 6, column=0)

    entry = Entry(f1left, font=('arial', 16, 'bold'), textvariable=entry_variable, bd=5, insertwidth=5,
                  bg="white", justify='right', width=4)
    entry.grid(row=i + 6, column=1)


# Food items entry for Breads
Breadscat= Label(f1middle,text='     Breads',font=('arial',30,'bold'))
Breadscat.grid()

# List to store the entry variables
entry_variables = [varChapati, varGarlicNaan, varTandooriRoti, varButterNaan]

# Menu items and their corresponding labels
menu_items = [
    ("Chapati", 12),
    ("Garlic Naan", 30),
    ("Tandoori roti", 20),
    ("Butter Naan", 25),
]
# Loop to create labels and entry fields dynamically
for i, (menu_item, price) in enumerate(menu_items):
    label_text = f"{menu_item}....(Rs.{price})"
    entry_variable = entry_variables[i]

    label = Label(f1middle, font=('arial', 16, 'bold'), text=label_text, bd=5, anchor="w")
    label.grid(row=i + 1, column=0)

    entry = Entry(f1middle, font=('arial', 16, 'bold'), textvariable=entry_variable, bd=5, insertwidth=5,
                  bg="white", justify='right', width=4)
    entry.grid(row=i + 1, column=1)

# Food items entry for deserts
desertcat= Label(f1middle,text='     Desert',font=('arial',30,'bold'))
desertcat.grid()

# List to store the entry variables
entry_variables = [varChocoLavaCake, varGulabJamun, varRasmalai, varJalebi]

# Menu items and their corresponding labels
menu_items = [
    ("Choco Lava Cake", 100),
    ("Gulab Jamun", 40),
    ("Rasmalai", 50),
    ("Jalebi", 45),
]

# Loop to create labels and entry fields dynamically
for i, (menu_item, price) in enumerate(menu_items):
    label_text = f"{menu_item}....(Rs.{price})"
    entry_variable = entry_variables[i]

    label = Label(f1middle, font=('arial', 16, 'bold'), text=label_text, bd=5, anchor="w")
    label.grid(row=i + 6, column=0)

    entry = Entry(f1middle, font=('arial', 16, 'bold'), textvariable=entry_variable, bd=5, insertwidth=5,
                  bg="white", justify='right', width=4)
    entry.grid(row=i + 6, column=1)


#Total/Subtotal/surcharge
totalcat= Label(f1right,text='           Bill',font=('arial',30,'bold'))
totalcat.grid()

# List to store the entry variables
entry_variables = [varsubtotal, varsercharhge, varTotal]

# Menu items and their corresponding labels
total_lists = [
    ("Sub Total"),
    ("Ser Charge"),
    ("Total")
]

# Loop to create labels and entry fields dynamically
for i, (total_list) in enumerate(total_lists):
    label_text = f"{total_list}"
    entry_variable = entry_variables[i]

    label = Label(f1right, font=('arial', 16, 'bold'), text=label_text, bd=5, anchor="w")
    label.grid(row=i + 1, column=0)

    entry = Entry(f1right, font=('arial', 16, 'bold'), textvariable=entry_variable, bd=5, insertwidth=5,
                  bg="white", justify='right', width=12)
    entry.grid(row=i + 1, column=1)

# Total/Reset/Exit Buttons
btntotal=Button(f1right,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),
                width=10,text="Total",bg="powder blue",command=food_order.total).grid(row=4,column=0)
btnreset=Button(f1right,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),
                width=10,text="Reset",bg="aquamarine",command=food_order.reset).grid(row=5,column=0)
btnexit=Button(f1right,padx=16,pady=8,bd=16,fg="black",font=('arial',16,'bold'),
               width=10,text="Exit",bg="red",command=food_order.qexit).grid(row=6,column=0)
root.mainloop()
