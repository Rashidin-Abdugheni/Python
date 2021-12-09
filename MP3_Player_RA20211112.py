from tkinter import *
from tkinter import filedialog
from pygame import mixer

class MusicPlayer:
    def __init__(self, window ):
        window.geometry('320x130'); window.title('MP3 Player By Rashidin Abdugheni'); window.resizable(0,0)
        Load = Button(window, text = 'Load',  activebackground='red', width = 10, font = ('Black', 14),bg='#A9F5F2', command = self.load)
        Play = Button(window, text = 'Play',   activebackground='red',width = 10,font = ('Black', 14), bg='#A9F5F2',command = self.play)
        Pause = Button(window,text = 'Pause',   activebackground='red',width = 10, font = ('Black',14), bg='#A9F5F2',command = self.pause)
        Stop = Button(window ,text = 'Stop',   activebackground='red',width = 10, font = ('Black', 14), bg='#A9F5F2',command = self.stop)

        Load.place(x=40,y=10);Play.place(x=160,y=10);Pause.place(x=40,y=60);Stop.place(x=160,y=60)
        self.music_file = False
        self.playing_state = False
    def load(self):
        self.music_file = filedialog.askopenfilename()
    def play(self):
        if self.music_file:
            mixer.init()
            mixer.music.load(self.music_file)
            mixer.music.play()
    def pause(self):
        if not self.playing_state:
            mixer.music.pause()
            self.playing_state=True
        else:
            mixer.music.unpause()
            self.playing_state = False
    def stop(self):
        mixer.music.stop()
root = Tk()
root.configure(bg='black')
app= MusicPlayer(root)
root.mainloop()
