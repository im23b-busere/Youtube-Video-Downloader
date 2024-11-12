import tkinter
from tkinter import messagebox, ttk, filedialog
from PIL import Image, ImageTk
import requests
from pytubefix import YouTube
from io import BytesIO


def download_video():
    try:
        # show hidden progress bar
        progress_bar.pack()
        app.update_idletasks()

        yt_link = link.get()
        yt_obj = YouTube(yt_link, on_progress_callback=progress_function)


        # saving thumbnail into memory and displaying it
        thumbnail_path = yt_obj.thumbnail_url

        response = requests.get(thumbnail_path)
        img_data = response.content

        img = Image.open(BytesIO(img_data)).resize((200, 140))

        img_tk = ImageTk.PhotoImage(img)

        thumbnail_label.configure(image=img_tk)
        thumbnail_label.image = img_tk

        # avoid garbage collection
        thumbnail_label.image = img_tk

        # get selected video quality
        selected_quality = quality_var.get()
        vid_sel_qual = yt_obj.streams.filter(res=selected_quality, progressive=True).first()

        if vid_sel_qual != None:
            vid_sel_qual.download(output_path=save_location.get())
            tkinter.messagebox.showinfo("Success", "Video downloaded successfully!")

        elif selected_quality == "select quality":
            tkinter.messagebox.showerror(f"Error", "No video quality selected.")

        else:
            tkinter.messagebox.showerror(f"Error", f"Selected video quality ({selected_quality}) not available.")

    except Exception as err:
        tkinter.messagebox.showerror("Error", f"An error occurred: {err}")

    finally:
        progress_bar.pack_forget()
        app.update_idletasks()


def progress_function(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    percent_complete = int((total_size - bytes_remaining) / total_size * 100)

    progress_bar["value"] = percent_complete
    app.update_idletasks()


def choose_directory():
    folder_path = tkinter.filedialog.askdirectory()
    save_location.set(folder_path)


# creating app frame
app = tkinter.Tk()
app.title("Youtube Downloader by Erik")
app.geometry("720x480")

# UI elements
title = tkinter.Label(app, text="Youtube Downloader", font=("Arial", 20))
title.pack(padx=20, pady=20)

# thumbnail label
thumbnail_label = tkinter.Label(app)
thumbnail_label.pack(pady=5)

# url label
url_label = tkinter.Label(app, text="Enter the URL below:", font=("Arial", 12), fg="grey")
url_label.pack()

# url entry
url = tkinter.StringVar()
link = tkinter.Entry(app, width=50, textvariable=url)
link.pack()

# Quality selection and file location frame
quality_frame = tkinter.Frame(app)
quality_frame.pack(pady=10)

# Quality selection dropdown
quality_var = tkinter.StringVar(app)
quality_options = ["144p", "360p", "480p", "720p", "1080p"]
quality_dropdown = tkinter.OptionMenu(quality_frame, quality_var, * quality_options)
quality_var.set("select quality")
quality_dropdown.pack(side="left")

# file location
save_location = tkinter.StringVar()
folder_button = tkinter.Button(quality_frame, text="Choose Save Folder", command=choose_directory)
folder_button.pack(side="left", padx=10)


# progress bar
progress_bar = ttk.Progressbar(app, orient='horizontal', length=200, mode='determinate')
progress_bar.pack(padx=20, pady=20)
progress_bar.pack_forget()

# download button
download = tkinter.Button(app, text="Download", command=download_video)
download.pack(padx=20, pady=20)

# footer
copyright = tkinter.Label(app, text=" © 2024 Erik. All rights reserved.", font=("Arial", 10), fg="grey")
copyright.pack(padx=20, pady=0)

# loop to run
app.mainloop()