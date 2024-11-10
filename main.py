import tkinter
from tkinter import messagebox, ttk
from pytubefix import YouTube


def download_video():
    try:
        yt_link = link.get()
        yt_obj = YouTube(yt_link, on_progress_callback=progress_function)

        yt_obj.streams.get_highest_resolution().download()
        tkinter.messagebox.showinfo("Success", "Video downloaded successfully!")

    except Exception as err:
        tkinter.messagebox.showerror("Error", f"An error occurred: {err}")


def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    percent_complete = int((total_size - bytes_remaining) / total_size * 100)

    progress_bar["value"] = percent_complete
    app.update_idletasks()


# creating app frame
app = tkinter.Tk()
app.title("Youtube Downloader by Erik")
app.geometry("600x400")

# UI elements
title = tkinter.Label(app, text="Youtube Downloader", font=("Arial", 20))
title.pack(padx=20, pady=20)

# url label
url_label = tkinter.Label(app, text="Enter the URL below:", font=("Arial", 12), fg="grey")
url_label.pack()

# url entry
url = tkinter.StringVar()
link = tkinter.Entry(app, width=50, textvariable=url)
link.pack()


# progress bar
progress_bar = ttk.Progressbar(app, orient='horizontal', length=200, mode='determinate')
progress_bar.pack(padx=20, pady=20)


# download button
download = tkinter.Button(app, text="Download", command=download_video)
download.pack(padx=20, pady=20)

# footer
copyright = tkinter.Label(app, text=" © 2024 Erik. All rights reserved.", font=("Arial", 10), fg="grey")
copyright.pack(padx=20, pady=90)


# loop to run
app.mainloop()
