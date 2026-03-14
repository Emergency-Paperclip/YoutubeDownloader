from pytubefix import YouTube
from pytubefix.cli import on_progress
import tkinter as tk
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename
from time import sleep

def download_mp4():
    # Get text from the entry box
    text = entry.get()
    print(text)
    sleep(3)
    name = ""
    path = ""
    yt = YouTube(text)
    stream = yt.streams.get_highest_resolution()
    if stream:
        path = asksaveasfilename(initialfile = 'video.mp4', defaultextension = ".mp4", filetypes = [("Videos", "*.mp4")])
        name = path.split('/')[-1] # get just the file name
        path = path[:-len(name)] # should be all of the path except the file name

    stream.download(path, name)

def download_mp3():
    text = entry.get()
    print(text)
    sleep(3)
    name = ""
    path = ""
    yt = YouTube(text)
    stream = yt.streams.get_audio_only()
    if stream:
        path = asksaveasfilename(initialfile = 'audio.mp3', defaultextension = ".mp3", filetypes = [("Audio", "*.wav", "*.ogg", "*.mp3")])
        name = path.split('/')[-1]
        path = path[:-len(name)]
    
    print(f"{path}, {name}")
    stream.download(path, name)

# Create the main window
root = tk.Tk()
root.title("Youtube 2 Mp3+4 (real (no virus))")
root.geometry("500x150")

main_frame = tk.Frame(root)
# Create a label for the entry box
label = tk.Label(main_frame, text = "Enter url:", font = 24)
label.pack(pady = 10)

# Create the entry box (text box)
entry = tk.Entry(main_frame, font = 16)
entry.pack(padx = 20, fill="x", pady = 10)

button_frame = tk.Frame(main_frame)
mp3button = tk.Button(button_frame, text = "Audio", command = download_mp3, font = 20)
button = tk.Button(button_frame, text = "Video", command = download_mp4, font = 20)
button.pack(side=tk.LEFT, padx = 10)
mp3button.pack(side=tk.LEFT, padx = 10)
button_frame.pack(pady = 15)
main_frame.pack(expand=True, fill="both")

# Start the Tkinter event loop
root.mainloop()