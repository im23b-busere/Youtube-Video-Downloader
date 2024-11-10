import tkinter


def download_video():
    pass


# creating app frame
app = tkinter.Tk()
app.title("Youtube Downloader")
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

# download button
download = tkinter.Button(app, text="Download", command=download_video)
download.pack(padx=20, pady=20)

# loop to run
app.mainloop()
