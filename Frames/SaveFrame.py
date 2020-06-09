from tkinter import *
from PIL import Image, ImageTk

textbackground = "#f5ffcf"
textcolor1 = "#8c49a3"
textcolor2 = "#4c66a8"


class SaveFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # create canvas for background image
        canvas = Canvas(self)
        img = ImageTk.PhotoImage(Image.open("/home/john/PycharmProjects/PongScoreboard/images/pingpongblur.jpeg").resize((self.winfo_screenwidth(), self.winfo_screenheight()), Image.ANTIALIAS))
        canvas.background = img
        canvas.create_image(0, 0, anchor=NW, image=img)
        canvas.grid(row=0, column=0, sticky='nesw')
        canvas.columnconfigure(0, weight=1)
        canvas.columnconfigure(1, weight=1)
        canvas.rowconfigure(0, weight=1)
        canvas.rowconfigure(1, weight=2)

        label = Label(canvas, text="Do you want to save the game?", font=("Times", 40), background=textbackground, highlightthickness=4)
        label.config(highlightbackground='black', highlightcolor='black')
        label.grid(row=0, column=0, columnspan=2)

        save_button = Button(canvas, text="Save game", command=lambda: controller.save_game(),
                             font=("Times", 20), bg=textbackground)
        discard_button = Button(canvas, text="Discard", command=lambda: controller.discard_game(),
                                font=("Times", 20), bg=textbackground)
        save_button.grid(row=1, column=0)
        discard_button.grid(row=1, column=1)