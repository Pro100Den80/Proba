from tkinter import *
from tkinter import messagebox as mb
from tkinter import simpledialog as sd
import  datetime
import time
import pygame

t = 0
music = False

def set():
    global t
    rem = sd.askstring("Время напоминания","Введите время напоминания в формате ЧЧ:ММ")
    if rem:
        try:
            hour = int(rem.split (":")[0])
            mnt = int(rem.split (":")[1])
            now = datetime.datetime.now()
            print(now)
            dt = now.replace(hour=hour, minute=mnt, second=0)
            label.config(text=f'Установлено напоминание на {hour:02}:{mnt:02}')
            print(dt)
            t = dt.timestamp()
            print(t)
        except Exception as e:
            mb.showerror("Ошибка",f"Произошла ошибка{e}")


def chek():
    global t
    if t:
        now = time.time()
        if now >=t:
            play_snd()
            t = 0
    window.after(10000, chek)


def play_snd():
    global music
    music = True
    pygame.mixer.init()
    pygame.mixer.music.load('reminder.mp3')
    pygame.mixer.music.play()


def stop_snd():
    global music
    if music:
        pygame.mixer.music.stop()
    music = False
    label.config(text='Новое напоминание')


window = Tk()
window.title("Напоминание")
label = Label(text="Введите время напоминания", font='Arial 15')
label.pack(pady=10)
set_button = Button(text="Установить напоминание", command=set)
set_button.pack(pady=10)
stop_button = Button(text='Выключить музыку', command=stop_snd)
stop_button.pack(pady=10)

chek()

window.mainloop()