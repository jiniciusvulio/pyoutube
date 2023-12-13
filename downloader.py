import os
import tkinter as tk
import customtkinter
from PIL import ImageTk
from pytube import YouTube

def download_video():
    try:
        yt_link = link.get()
        yt_object = YouTube(yt_link, on_progress_callback=on_progress)
        video = yt_object.streams.get_highest_resolution()

        title.configure(text=f"Downloading: {yt_object.title}", text_color="white")
        exit_message.configure(text="")
        video.download()
        exit_message.configure(text="Completed!")
    except:
        exit_message.configure(text="Error.", text_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    completion = bytes_downloaded / total_size * 100
    per = str(int(completion))
    tracker.configure(text= per + '%')
    tracker.update()

    progress_bar.set(float(completion) / 50)

# settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")

# frame
app = customtkinter.CTk()
app.geometry("720x310")
app.title("YouTube Downloader")

iconpath= ImageTk.PhotoImage(file=os.path.join("assets", "logo.png"))
app.wm_iconbitmap()
app.iconphoto(True, iconpath)


# UI
title = customtkinter.CTkLabel(app, text="Insert an YouTube video link")
title.pack(padx=10, pady=12)

# link input
video_url = tk.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=video_url)
link.pack()

# progress info
tracker = customtkinter.CTkLabel(app, text="")
tracker.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=350)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=12)

exit_message = customtkinter.CTkLabel(app, text="0%")
exit_message.pack(padx=10, pady=12)

# download btn
download = customtkinter.CTkButton(app, text="Download", command=download_video)
download.pack(padx=10, pady=12)

# run app
app.mainloop()