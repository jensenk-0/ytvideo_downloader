# code for the general user interface, gui
import tkinter as tk
from download import downloader




class Video_downloader(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
 
        self.geometry("350x350")
        self.title("Video Downloader")
            
        self.path_label = tk.Label(self, text="Download path").grid(row=0, column=0)
        self.link_label = tk.Label(self, text="video link").grid(row=1, column=0)

        self.path = tk.Entry(self)
        self.path.grid(row=0, column=1)
        self.link = tk.Entry(self)
        self.link.grid(row=1, column=1)
        
        


        self.download_btn = tk.Button(self, text="Download", width=10, command= lambda: downloader(self.link.get(), self.path.get())).grid(row=3, column=0)


        


    
def run_app():
    Video_downloader().mainloop()
    


    
    

        

















    

    
    


