from tkinter import *
from PIL import Image, ImageTk
import os
from Frames.SaveFrame import SaveFrame
from Frames.SetupFrame import SetupFrame
from Frames.BoardFrame import BoardFrame
from Frames.AdduserFrame import AdduserFrame
from Frames.EdituserFrame import EdituserFrame
from Frames.DeleteuserFrame import DeleteuserFrame
from Tables import User, Game
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

class ScoreboardController(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)
        self.title("Scoreboard")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        # boilerplate creating parent container for all frames
        container = Frame(self)
        container.config(bg="white")
        container.grid(row=0, column=0, sticky="nesw")
        container.rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)

        # create database session
        engine = create_engine('sqlite:///database.db')
        Session = sessionmaker(bind=engine)
        self.session = Session()

        # create state variables
        users = self.session.query(User).all()
        self.names = [user.name for user in users]
        self.ids = [user.id for user in users]
        self.sounds = [user.sound for user in users]
        self.details = [user.detail for user in users]
        self.player1 = StringVar()
        self.player2 = StringVar()
        self.p1totwin = StringVar()
        self.p2totwin = StringVar()
        self.p1totloss = StringVar()
        self.p2totloss = StringVar()
        self.p1head2head = StringVar()
        self.p2head2head = StringVar()
        self.p1detail = StringVar()
        self.p2detail = StringVar()
        self.p1pointsfor = StringVar()
        self.p2pointsfor = StringVar()
        self.score1 = 0
        self.score2 = 0
        self.points = 11
        self.games = 5
        self.switchserve = 2
        self.server = True  # True indicates that player1 will be the starting server
        self.gameover = False

        # create frame objects, format them, and place them into dictionary
        self.frames = {}
        for F in (SetupFrame, BoardFrame, SaveFrame, AdduserFrame, EdituserFrame, DeleteuserFrame):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nesw")

        # show the setup frame upon startup
        self.show_frame(SetupFrame)

        # for easy quitting
        self.bind("<Key>", self.key)

    def key(self, event):
        kp = str(event.char)
        if kp.__eq__("q"):
            self.destroy()

    # raise the given frame to foreground
    def show_frame(self, content):
        frame = self.frames[content]
        frame.tkraise()
        frame.focus_set()

    # get player 1 and 2 names, go to boardframe
    def start_game(self, setup):
        self.player1.set(setup.p1entry.get())
        self.player2.set(setup.p2entry.get())
        p1totwin, p1totloss,\
        p2totwin, p2totloss,\
        p1head, p2head,\
        p1detail, p2detail,\
        p1pointsfor, p2pointsfor =\
            self.get_gameinfo(setup.p1entry.get(), setup.p2entry.get())
        self.p1totwin.set(p1totwin)
        self.p1totloss.set(p1totloss)
        self.p2totwin.set(p2totwin)
        self.p2totloss.set(p2totloss)
        self.p1head2head.set(p1head)
        self.p2head2head.set(p2head)
        self.p1detail.set(p1detail)
        self.p2detail.set(p2detail)
        self.p1pointsfor.set(p1pointsfor)
        self.p2pointsfor.set(p2pointsfor)

        self.show_frame(BoardFrame)

    # reset winnerstring to empty, go to saveframe
    def exit_game(self):
        self.frames[BoardFrame].winnerstring.set("")
        self.show_frame(SaveFrame)

    # save current game and reset
    def save_game(self):
        p1 = self.get_user_by_name(self.player1.get())
        p2 = self.get_user_by_name(self.player2.get())
        if self.score1 > self.score2:
            p1wins = True
        else:
            p1wins = False

        game = Game(player1_id=p1.id, player2_id=p2.id, p1score=self.score1, p2score=self.score2, p1winner=p1wins)
        self.session.add(game)
        self.session.commit()
        self.reset_game()

    # reset game without saving
    def discard_game(self):
        self.reset_game()

    def reset_game(self):
        self.player1.set("")
        self.player2.set("")
        self.score1 = 0
        self.score2 = 0
        self.points = 11
        self.games = 1
        self.switchserve = 2
        self.gameover = False
        self.frames[BoardFrame].Score_txt1.set(0)
        self.frames[BoardFrame].Score_txt2.set(0)
        self.frames[BoardFrame].winner_label.grid_remove()
        self.show_frame(SetupFrame)

    def playmusic(self, name):
        user = self.session.query(User).filter_by(name=name).first()
        os.system("aplay /home/john/PycharmProjects/PongScoreboard/sounds/" + user.sound)

    def add_user(self, name, details, sound):
        if name not in self.names:
            new_user = User(name=name, detail=details, sound=sound)
            self.session.add(new_user)
            self.session.commit()
            self.users = self.session.query(User).all()
            self.names = [user.name for user in self.users]
            self.ids = [user.id for user in self.users]
            self.sounds = [user.sound for user in self.users]
            self.details = [user.detail for user in self.users]
            print("successfully added user!")
            self.frames[SetupFrame].p1entry.config(values=self.names)
            self.frames[SetupFrame].p2entry.config(values=self.names)
            self.frames[DeleteuserFrame].name.config(values=self.names)

        self.show_frame(SetupFrame)

    def edit_user(self, name, details, sound):
        user = self.get_user_by_name(name)
        user.detail = details
        user.sound = sound
        self.session.commit()
        self.users = self.session.query(User).all()
        self.names = [user.name for user in self.users]
        self.ids = [user.id for user in self.users]
        self.sounds = [user.sound for user in self.users]
        self.details = [user.detail for user in self.users]
        self.frames[SetupFrame].p1entry.config(values=self.names)
        self.frames[SetupFrame].p2entry.config(values=self.names)
        self.show_frame(SetupFrame)

    def delete_user(self, name):
        user = self.get_user_by_name(name)
        self.session.delete(user)
        self.session.commit()
        self.users = self.session.query(User).all()
        self.names = [user.name for user in self.users]
        self.ids = [user.id for user in self.users]
        self.sounds = [user.sound for user in self.users]
        self.details = [user.detail for user in self.users]
        self.frames[SetupFrame].p1entry.config(values=self.names)
        self.frames[SetupFrame].p2entry.config(values=self.names)
        self.show_frame(SetupFrame)

    def get_user_by_name(self, name):
        user = self.session.query(User).filter_by(name=name).first()
        return user

    def get_gameinfo(self, name1, name2):
        player1 = self.session.query(User).filter_by(name=name1).first()
        player2 = self.session.query(User).filter_by(name=name2).first()

        p1totalwins = 0
        p1totallosses = 0
        games1a = self.session.query(Game).filter_by(player1=player1)
        for game in games1a:
            if game.p1winner:
                p1totalwins += 1
            else:
                p1totallosses += 1
        games1b = self.session.query(Game).filter_by(player2=player1)
        for game in games1b:
            if not game.p1winner:
                p1totalwins += 1
            else:
                p1totallosses += 1

        p2totalwins = 0
        p2totallosses = 0
        games2a = self.session.query(Game).filter_by(player1=player2)
        for game in games2a:
            if game.p1winner:
                p2totalwins += 1
            else:
                p2totallosses += 1
        games2b = self.session.query(Game).filter_by(player2=player2)
        for game in games2b:
            if not game.p1winner:
                p2totalwins += 1
            else:
                p2totallosses += 1

        p1head2headwins = 0
        p2head2headwins = 0
        p1pointsfor = 0
        p2pointsfor = 0
        games12a = self.session.query(Game).filter_by(player1=player1, player2=player2)
        for game in games12a:
            if game.p1winner:
                p1head2headwins += 1
            else:
                p2head2headwins += 1
            p1pointsfor += game.p1score
            p2pointsfor += game.p2score

        games12b = self.session.query(Game).filter_by(player1=player2, player2=player1)
        for game in games12b:
            if not game.p1winner:
                p1head2headwins += 1
            else:
                p2head2headwins += 1
            p1pointsfor += game.p2score
            p2pointsfor += game.p1score

        return p1totalwins, p1totallosses, p2totalwins, p2totallosses, p1head2headwins,\
               p2head2headwins, player1.detail, player2.detail, p1pointsfor, p2pointsfor




