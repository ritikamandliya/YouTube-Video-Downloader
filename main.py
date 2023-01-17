import os
from tkinter import *
from tkinter import filedialog
from moviepy import *
from moviepy.editor import AudioFileClip
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil
# functions
def select_path():
    # allows user to select path
    path = filedialog.askdirectory()
    path_label.config(text=path)
def download_file():
    # get user path
    get_link = link_enter.get()
    # get selected path
    user_path = path_label.cget("text")
    screen.title("Downloading...")

    # download video
    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()



    # move file to selected directory
    shutil.move(vid_clip,user_path)
    screen.title("Download Complete! Download Another File...")



screen = Tk()
title = screen.title ("Youtube Video Downloader")


canvas = Canvas(screen,width=500,height=500)
canvas.pack()
# image logo
logo_img = PhotoImage(file = 'img.png')
# resize image
logo_img= logo_img.subsample(2,2)
canvas.create_image(250,80,image=logo_img)

# links
link_enter = Entry(screen,width=50)
link_label = Label(screen, text = "Enter Download Link: ", font={'Arial',16})
# path for saving file
path_label = Label(screen , text='Select Path For Download' ,font ={'Arial',16} )
select_btn = Button(screen, text='Select' ,command=select_path)
# add to window
canvas.create_window(250,280,window=path_label)
canvas.create_window(250,330,window=select_btn)

# widgets to window
canvas.create_window(250,170,window=link_label)
canvas.create_window(250,220,window=link_enter)
# download button
download_btn = Button(screen,text='Download File',command=download_file)

# add to canvas
canvas.create_window(250,390,window= download_btn)

screen.mainloop()

