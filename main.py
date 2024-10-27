#Lembrem de instalar as bibliotecas com o pip caso não tenham
from pytubefix import YouTube
from pytubefix.cli import on_progress
import time

url = input("Digite a url do vídeo: ")
 
yt = YouTube(url, on_progress_callback = on_progress)
print(yt.title)
a = [0]
for i in a:
    ys = yt.streams.get_highest_resolution()
    ys.download()
    break