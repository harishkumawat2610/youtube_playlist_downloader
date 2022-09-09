#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
from pytube import YouTube
from pytube import Playlist
from pytube.contrib.channel import Channel


# In[2]:


songs_list={"haryanvi songs":'https://www.youtube.com/playlist?list=PLW3V2FvydyVPgKJjefb42kx5u0bvrW-yp',"sidhu moose wala":"https://www.youtube.com/playlist?list=PLEeZqnCbsZoTd2RvPp9WNzGZawRErbYfU","Hindu god dj song":"https://www.youtube.com/playlist?list=PL9SiqOIMEXuQr3FoIvem97X-DK1UVXN7H","Best of Bollywood Hindi Love Songs":"https://www.youtube.com/playlist?list=PL9bw4S5ePsEEqCMJSiYZ-KTtEjzVy0YvK"}


# In[ ]:


for foldername,playlist_url in songs_list.items():
    print("= "*10+str(foldername)+" ="*10)
    destination = r"/home/harish-ds/Documents/"+foldername
    try:
        os.mkdir(destination)
    except:
        print("already")
    playlist = Playlist(playlist_url)
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    for i,no in zip(playlist,range(1,len(playlist))):
        try:
            yt=YouTube(i)
            video = yt.streams.filter(only_audio=True,file_extension='mp4').first()
            out_file = video.download(output_path=destination)
            base, ext = os.path.splitext(out_file)
            new_file = base + '.mp3'
            os.rename(out_file, new_file)
            print(str(no)+" : "+yt.title + " has been successfully downloaded.")
        except Exception as e:
            print("Error :===> ",e)

