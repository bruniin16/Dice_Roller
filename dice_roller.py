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

d4_img = PhotoImage(file=fr"./midia/d4.png")
d4 = Button(main, relief="flat", image=d4_img, bg = corbg, compound="left", text="  1d4", font=("Berlin Sans FB", 15), fg="white").place(x=15, y=180)

d4 = Button(main, relief="flat", image=d4_img, bg = corbg, compound="left", text="  1d6", font=("Berlin Sans FB", 15), fg="white").place(x=15, y=240)

d4 = Button(main, relief="flat", image=d4_img, bg = corbg, compound="left", text="  1d8", font=("Berlin Sans FB", 15), fg="white").place(x=15, y=300)

d4 = Button(main, relief="flat", image=d4_img, bg = corbg, compound="left", text="  1d10", font=("Berlin Sans FB", 15), fg="white").place(x=15, y=360)

d4 = Button(main, relief="flat", image=d4_img, bg = corbg, compound="left", text="  1d12", font=("Berlin Sans FB", 15), fg="white").place(x=15, y=420)

d4 = Button(main, relief="flat", image=d4_img, bg = corbg, compound="left", text="  1d20", font=("Berlin Sans FB", 15), fg="white").place(x=15, y=480)

d4 = Button(main, relief="flat", image=d4_img, bg = corbg, compound="left", text="  1d100", font=("Berlin Sans FB", 15), fg="white").place(x=15, y=540)



main.mainloop()