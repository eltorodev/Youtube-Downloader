from pytube import YouTube
from pytube.exceptions import *
import tkinter as tk


class MainApplication(tk.Frame):

    """Constructor containing tkinter styles and settings."""
    def __init__(self, root=None, *args, **kwargs):
        tk.Frame.__init__(self, root)

        self.root = root

        self.download_location = "downloads/"

        self.download_type = tk.IntVar()

        self.url_label = tk.Label(self.root, text="Entre com a URL do vídeo:")
        self.url_label.grid(row=0, column=0)

        self.url_entry = tk.Entry(self.root)
        self.url_entry.grid(row=1, column=0)

        self.locate_button = tk.Button(self.root, text="Localizar vídeo", command=self.locate)
        self.locate_button.grid(row=1, column=1)

        self.info = tk.Label(self.root)
        self.info.grid(row=2, column=0)

        self.type_label = tk.Label(self.root, text="Selecione o tipo:")
        self.type_label.grid(row=3, column=0)

        audio = tk.Radiobutton(self.root, text="Áudio", variable=self.download_type, value=0)
        audio.grid(row=4, column=0)

        video = tk.Radiobutton(self.root, text="Vídeo", variable=self.download_type, value=1)
        video.grid(row=5, column=0)

        self.download_button = tk.Button(self.root, text="Iniciar download", state="disabled", command=self.download)
        self.download_button.grid(row=6, column=0)

        self.author = tk.Label(self.root, text="By TheGuilherme")
        self.author.grid(row=7, column=6)

    # Function for the locating of the video
    def locate(self):
        """Finds and checks whether a video is found and valid."""
        global video_object

        try:
            video_object = YouTube(self.url_entry.get())

            self.info.configure(text=f"Video title: {video_object.title}", fg="blue")
        except RegexMatchError:
            self.info.configure(text="Error: Incorrect URL!", fg="red")
            return

        self.download_button.configure(state="normal")

    # Download the video into download
    def download(self):
        """If all goes well the video / audio will be downloaded into the downloads /."""
        if self.download_type.get() == 0:
            video_stream = video_object.streams.filter(only_audio=True).first()

        if self.download_type.get() == 1:
            video_stream = video_object.streams.filter(only_video=True).first()

        self.info.configure(text="Baixando...", fg="blue")

        video_stream.download(self.download_location)

        self.info.configure(text="Pronto!")


if __name__ == '__main__':
    # Tkinter start
    window = tk.Tk()
    window.title("Youtube Downloader v1")

    application = MainApplication(window)

    window.mainloop()
