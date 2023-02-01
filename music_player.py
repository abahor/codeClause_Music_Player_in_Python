import tkinter as tk
import fnmatch
import os
from pygame import mixer

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x800")
canvas.config(bg="black")

rootpath = r"C:\Users\abahor\OneDrive\Desktop\simple calculator\music"
pattern = '*.mp3'
mixer.init()


def select():
    label.config(text=listBox.get("anchor"))
    if not listBox.get("anchor"):
        label.config(text='Error please choose a song')
        return
    # print(mixer.get_init())
    try:
        mixer.music.play()
    except:
        mixer.music.load(rootpath + '\\' + listBox.get("anchor"))
        mixer.music.play()


def pause():
    mixer.music.pause()
    listBox.select_clear('active')


def play_next():
    next_song = listBox.curselection()
    next_song = next_song[0] + 1
    if listBox.get(next_song) == "":
        next_song = 2
    next_song_name = listBox.get(next_song)
    label.config(text=next_song_name)
    mixer.music.load(rootpath + '\\' + next_song_name)
    mixer.music.play()
    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)


def resume():
    if resumeButton['text'] == "Resume":
        resumeButton['text'] = "Pause"
        mixer.music.unpause()
    else:
        resumeButton['text'] = "Resume"
        mixer.music.pause()


def play_prev():
    next_song = listBox.curselection()
    next_song = next_song[0] - 1
    if listBox.get(next_song) == "--------------------------":
        next_song = listBox.size() - 1

    next_song_name = listBox.get(next_song)
    label.config(text=next_song_name)
    mixer.music.load(rootpath + '\\' + next_song_name)
    mixer.music.play()
    listBox.select_clear(0, 'end')
    listBox.activate(next_song)
    listBox.select_set(next_song)


listBox = tk.Listbox(canvas, fg='cyan', bg="black", width=100, font=('poppins', 14))
listBox.pack(padx=15, pady=15)

listBox.insert(0, 'Done for codeClause')
listBox.insert(1, '--------------------------')

label = tk.Label(canvas, text="", bg="black", fg="yellow", font=("Arial", 14))
label.pack(pady=15)

top = tk.Frame(canvas, bg="black")
top.pack(padx=10, pady=5, anchor="center")

prevButton = tk.Button(canvas, text="Prev", command=play_prev)
prevButton.pack(pady=15, in_=top, side="left")

stopButton = tk.Button(canvas, text="Stop", command=pause)
stopButton.pack(pady=15, padx=15, in_=top, side="left")

resumeButton = tk.Button(canvas, text="Pause", command=resume)
resumeButton.pack(pady=15, padx=15, in_=top, side="left")

playButton = tk.Button(canvas, text="Play", command=select)
playButton.pack(pady=15, padx=15, in_=top, side="left")

nextButton = tk.Button(canvas, text="Next", command=play_next)
nextButton.pack(pady=15, padx=15, in_=top, side="left")

for root, dirs, files in os.walk(rootpath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

canvas.mainloop()
