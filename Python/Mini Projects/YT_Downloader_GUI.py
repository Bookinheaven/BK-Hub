import tkinter
import customtkinter
from pytube import YouTube

class Music_Downloader(customtkinter.CTk):
    def __init__(self):
        super().__init__()
    def build(self):
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("blue")

        self.geometry("720x480")
        self.minsize(720, 480)
        self.maxsize(1080, 720)
        self.title("Youtube Downloader")

        PreFrame = customtkinter.CTkFrame(self)
        PreFrame.pack(fill=customtkinter.BOTH, expand=True, padx=10, pady=10)

        self.title_label = customtkinter.CTkLabel(master=PreFrame, text="Insert A Youtube Link")
        self.title_label.pack(padx=10, pady=10)

        self.url_link = tkinter.StringVar()
        self.link = customtkinter.CTkEntry(master=PreFrame, width=350, height=40, textvariable=self.url_link)
        self.link.pack()
        self.link.bind("<Control-a>", self.select_all_text)

        self.finished = customtkinter.CTkLabel(master=PreFrame, text="")
        self.finished.pack()

        self.ProgressP = customtkinter.CTkLabel(master=PreFrame, text='0%')
        self.ProgressP.pack()

        self.ProgressBar = customtkinter.CTkProgressBar(master=PreFrame, width=400)
        self.ProgressBar.set(0)
        self.ProgressBar.pack(padx=10, pady=10)

        self.download = customtkinter.CTkButton(master=PreFrame, text="Download", command=self.downloadstart)
        self.download.pack(padx=10, pady=20)

        self.mainloop()

    def downloadstart(self):
        try:
            ytlink = self.link.get()
            if ytlink:
                ytobject = YouTube(ytlink, on_progress_callback=self.on_progress)
                audio = ytobject.streams.get_audio_only()
                self.download.configure(state='disabled')  
                self.title_label.configure(text=f'{ytobject.title}', text_color="white")  
                self.finished.configure(text='')
                audio.download()
            else:
                return self.finished.configure(text=f"Enter the Link:", text_color="blue")
                
        except Exception as e:
            print(e)
            self.finished.configure(text=f"Download Error: {str(e)}", text_color="red")
        else:
            self.finished.configure(text="Download Completed", text_color="green")



    def on_progress(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage_of_completion = (bytes_downloaded / total_size) * 100
        per = str(int(percentage_of_completion))
        self.ProgressP.configure(text=per + "%")
        self.ProgressP.update()  
        self.ProgressBar.set(float(percentage_of_completion) / 100)

    def select_all_text(self,event):
        event.widget.select_range(0, 'end')
        event.widget.icursor('end')

if __name__ == "__main__":
    Music_Downloader().build()