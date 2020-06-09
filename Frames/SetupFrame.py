from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Frames.AdduserFrame import AdduserFrame
from Frames.EdituserFrame import EdituserFrame
from Frames.DeleteuserFrame import DeleteuserFrame
from style import textbackground


class SetupFrame(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        self.config(bg="white")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # create canvas for background image
        canvas = Canvas(self)
        img = ImageTk.PhotoImage(Image.open("/home/john/PycharmProjects/PongScoreboard/images/pingpongblur.jpeg").resize((self.winfo_screenwidth(), self.winfo_screenheight()), Image.ANTIALIAS))
        canvas.background = img
        canvas.create_image(0, 0, anchor=NW, image=img)
        canvas.grid(row=0, column=0, sticky='nesw')
        canvas.columnconfigure(0, weight=1)
        canvas.rowconfigure(0, weight=1)
        canvas.rowconfigure(1, weight=2)

        # create small frame for info selection
        InfoFrame = Frame(canvas, highlightthickness=4)
        InfoFrame.config(highlightbackground='black', highlightcolor='black')
        InfoFrame.config(background=textbackground)
        InfoFrame.grid(row=0, column=0)
        label = Label(InfoFrame, text="Select players", background=textbackground, font=("Times", 20))
        p1label = Label(InfoFrame, text="Player 1", background=textbackground, font=("Times", 14))
        p1name = StringVar(controller)
        self.p1entry = ttk.Combobox(InfoFrame, background=textbackground,
                                    textvariable=p1name, values=controller.names)

        p2label = Label(InfoFrame, text="Player 2", background=textbackground, font=("Times", 14))
        p2name = StringVar(controller)
        self.p2entry = ttk.Combobox(InfoFrame, background=textbackground,
                                    textvariable=p2name, values=controller.names)
        label.grid(row=0, column=0, pady=10, padx=10, columnspan=3)
        p1label.grid(row=1, column=0, padx=10)
        self.p1entry.grid(row=1, column=1, padx=10)
        p2label.grid(row=2, column=0, padx=10)
        self.p2entry.grid(row=2, column=1, padx=10)

        button = Button(InfoFrame, text="Start game", command=lambda: controller.start_game(self), bg=textbackground
                        , font=("Times", 14, "bold"))
        button.grid(row=3, column=1)

        newuser_button = Button(InfoFrame, text="add user", command=lambda: controller.show_frame(AdduserFrame),
                                bg=textbackground, font=("Times", 14))
        newuser_button.grid(row=4, column=0, pady=20, padx=10)

        edituser_button = Button(InfoFrame, text="edit user", command=lambda: controller.show_frame(EdituserFrame)
                                 , bg=textbackground, font=("Times", 14))
        edituser_button.grid(row=4, column=1, pady=20, padx=10)

        deleteuser_button = Button(InfoFrame, text="delete user", command=lambda: controller.show_frame(DeleteuserFrame)
                                   , bg=textbackground, font=("Times", 14))
        deleteuser_button.grid(row=4, column=2, pady=20, padx=10)
