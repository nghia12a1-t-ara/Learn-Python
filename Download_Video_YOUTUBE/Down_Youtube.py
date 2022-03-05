###
#from pytube import YouTube
#yt = YouTube('https://www.youtube.com/watch?v=tsh3rbC8UrE')
#video = yt.streams
#videos = list(enumerate(video))
#for i in videos:
#    print(i)
#    a = videos[3][1]
#    b = str(a)

#dn_video = video[3]
#dn_video.download("D:\\IOT\\Embedded_AI\\Embedded_AI_Udemy")

from __future__ import unicode_literals
import youtube_dl
ydl_opts = {}
with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download("https://youtu.be/L1k1ahYY3Bk")

