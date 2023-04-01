from tkinter import *
#from PIL import Image, ImageTk

corbg = "#101010"



main = Tk()
main.title("")
main.geometry("440x650+700+200")
main.config(bg = corbg)
main.iconphoto(False, PhotoImage(file = "./midia/dice_20_bg.png"))
main.resizable(width = False, height = False)

# Dice Icon on top
img = PhotoImage(file=fr"./midia/dice_20_icon.png")
d20_icon = Label(main, image=img, bg = corbg, compound="top", text="D&D Dice Roller", font=("Lucida Calligraphy", 18, "bold"), fg="white").pack(pady=15)


main.mainloop()