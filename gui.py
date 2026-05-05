# code for the general user interface, gui
import tkinter as tk

def Video_downloader():
    root = tk.Tk()
    root.geometry("300x300")
    root.title("ytvideo downloader")

    path_label = tk.Label(root, text="download\npath").grid(row=0, column=0)
    download_path = tk.Entry(root).grid(row=0, column=1)

    link_label = tk.Label(root, text="video\nlink").grid(row=1, column=0)
    link = tk.Entry(root).grid(row=1, column=1)

    download_btn = tk.Button(root, text="Download", width=10).grid(row=3, column=1)

    root.mainloop()









    

    
    


