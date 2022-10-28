from pytube import Playlist
from source.ytdownload import dlaud, dlvid

def plls(url):
    p = Playlist(url)
    lin = []; r = [lin.append(i) for i in p.videos]
    pil = int(input("\nDownload\n\t1.Audio\n\t2.Video\n\t>> "));n=0
    if pil == 1:
        for i in lin:
            url = "https://youtu.be/"+str(i)[41:52]
            print("\n\tDownloading",n,i.title);n+=1
            print(url)
            dlaud(url)
    elif pil == 2:
        for i in lin:
            url = "https://youtu.be/"+str(i)[41:52]
            print("\n\tDownloading",n,i.title);n+=1
            dlvid(url)
    else:
        exit()
