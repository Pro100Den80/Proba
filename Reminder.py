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
            dt = now.replace(hour=hour, minute=mnt, second=0)
            text = sd.askstring("Текст напоминания","Введите текст напоминания")
            label.config(text=f' Напоминание на {hour:02}:{mnt:02} {text}')

            t = dt.timestamp()

        except ValueError:
            if hour > 23 or mnt > 59:
                mb.showerror('Ошибка', 'Неверный формат времени')
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
window.geometry('300x160+300+300')
window.config(bg="Lime")
label = Label(text="Введите время напоминания", font='Arial 15 bold', bg='Lime',fg='Brown')
label.pack(pady=10)
set_button = Button(bg="Brown", fg="white", text="Установить напоминание", command=set)
set_button.pack(pady=10)
stop_button = Button(fg='Brown',text='Выключить музыку', command=stop_snd)
stop_button.pack(pady=10)

chek()

window.mainloop()