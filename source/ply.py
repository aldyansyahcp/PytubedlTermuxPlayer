from pytube import Playlist
from source.ytdownload import dlaud, dlvid
from pytube import YouTube as yt
import os
def plls(url):
    p = Playlist(url)
    lin = []; r = [lin.append(i) for i in p.videos]
    pil = int(input("\n\tDownload\n\t1.Audio\n\t2.Video\n\t>> "))
    if pil == 1:
        for n,i in enumerate(lin,1):
            url = "https://youtu.be/"+str(i)[41:52]
            yu = yt(url);aul = yu.streams.get_audio_only()
            nam = "{}.mp3".format(i.title); karak = "([+-_&$''#@¥{}] /)|:"
            for ni in karak:
                nam = nam.replace(ni,"")
            print("\n\tDownloading",n,nam)
            if os.path.exists("/sdcard/Download/audio/"+nam):
                print("\n\tFile",nam,"sudah Downloaded")
            else:
                aul.download(output_path="/sdcard/Download/audio",filename=nam)
                print("\n\tDownloaded")
        pil = input("want to play music? y/n: ").lower()
        if pil == "y":
            from source.pplay import playy
            playy()
    elif pil == 2:
        for i in lin:
            url = "https://youtu.be/"+str(i)[41:52]
            print("\n\tDownloading",n,i.title);n+=1
            dlvid(url)
    else:
        exit()
