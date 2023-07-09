from tkinter import *

corbg = "#101010"


main = Tk()
main.title("")
main.geometry("440x650+700+200")
main.config(bg = corbg)
main.iconphoto(False, PhotoImage(file = "./midia/dice_20_bg.png"))
main.resizable(width = False, height = False)

# Dice Icon on top
d20_img = PhotoImage(file=fr"./midia/d20icon.png")
d20_icon = Label(main, image=d20_img, bg = corbg, compound="bottom", text="D&D Dice Roller", font=("Lucida Calligraphy", 18, "bold underline"), fg="white").pack(pady=15)

d4_img = PhotoImage(file=fr"./midia/buttons/d4.png")
d4 = Button(main, relief="flat", image=d4_img, bg = corbg, compound="left", text="  1d4", font=("Berlin Sans FB", 15), fg="white", activebackground=corbg, activeforeground="white").place(x=15, y=180)

d6_img = PhotoImage(file=fr"./midia/buttons/d6.png")
d6 = Button(main, relief="flat", image=d6_img, bg = corbg, compound="left", text="  1d6", font=("Berlin Sans FB", 15), fg="white", activebackground=corbg, activeforeground="white").place(x=15, y=240)

d8_img = PhotoImage(file=fr"./midia/buttons/d8.png")
d8 = Button(main, relief="flat", image=d8_img, bg = corbg, compound="left", text="  1d8", font=("Berlin Sans FB", 15), fg="white", activebackground=corbg, activeforeground="white").place(x=15, y=300)

d10_img = PhotoImage(file=fr"./midia/buttons/d10.png")
d10 = Button(main, relief="flat", image=d10_img, bg = corbg, compound="left", text="  1d10", font=("Berlin Sans FB", 15), fg="white", activebackground=corbg, activeforeground="white").place(x=15, y=360)

d12_img = PhotoImage(file=fr"./midia/buttons/d12.png")
d12 = Button(main, relief="flat", image=d12_img, bg = corbg, compound="left", text="  1d12", font=("Berlin Sans FB", 15), fg="white", activebackground=corbg, activeforeground="white").place(x=15, y=420)

d20b_img = PhotoImage(file=fr"./midia/buttons/d20.png")
d20 = Button(main, relief="flat", image=d20b_img, bg = corbg, compound="left", text="  1d20", font=("Berlin Sans FB", 15), fg="white", activebackground=corbg, activeforeground="white").place(x=15, y=480)

d100 = Button(main, relief="flat", image=d10_img, bg = corbg, compound="left", text="  1d100", font=("Berlin Sans FB", 15), fg="white", activebackground=corbg, activeforeground="white").place(x=15, y=540)



main.mainloop()