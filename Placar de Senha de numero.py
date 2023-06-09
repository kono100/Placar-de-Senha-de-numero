

from tkinter import *
counterCheck = 0
def checkClick():
    global counterCheck
    counterCheck += 1
    if counterCheck == 100:
        counterCheck = 0
    textClick.config(text=counterCheck)
root = Tk()
root.title("Placar")
root.geometry("200x200")
root.configure(background="black")
root.resizable(False,False)
textClick = Label(root, text=0, font=("Ariel","70" ),fg="red",bg="black")
textClick.place(relx=0.2,rely=0.15)
ClickCounter = Button(root, text="SEGUINTE", command=checkClick)
ClickCounter.place(relx=0.35,rely=0.8)
ClickCounter.bind("<space>", checkClick)
ClickCounter.focus_force()
root.mainloop()