# code for the general user interface, gui
import tkinter as tk

def video_downloader():
    root = tk.Tk()
    root.geometry("350x350")
    root.title("Video Downloader")

    path_label = tk.Label(root, text="Download path").grid(row=0, column=0)
    link_label = tk.Label(root, text="video link").grid(row=1, column=0)

    path_download = tk.Entry(root).grid(row=0, column=1)
    link = tk.Entry(root).grid(row=1, column=1)

    download_btn = tk.Button(root, text="Download", width=10).grid(row=3, column=0)

    root.mainloop()















    

    
    


