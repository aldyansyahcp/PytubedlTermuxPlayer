from requests import get
from pytube import YouTube as yt
import os,time
from source.pplay import scann

def dlaud(url):
    yu = yt(url)
    aul = yu.streams.get_audio_only(); karak = "([+-_&$''#@¥{}] )|:"
    nam = "{}.mp3".format(yu.title)
    for i in karak:
        nam = nam.replace(i, "")
    aul.download(output_path="/sdcard/Download/audio",filename=nam)
    print("Berhasil Download, file saved in /sdcard/Download/audio")
    played()
    """rr = get(ul, stream=True); print(rr)
    if rr.status_code == 200:
        #print(f"File size: {bytesto(fz, 'm')}Mb")
        with open(f"download/audio/{nam}.mp3", "wb") as f:
            f.write(rr.content)
            print("Berhasil\nwith name {}.mp3".format(nam))
            f.close()
            print('Hasil durasi eksekusi kode diatas adalah = ' + str(timeEnd - timeBegin) )
            played()
            
    else:
        print("gagal")"""
        
def played():
    pl = input("Want to play this music? y/n ").lower()
    if pl == "y":
        print("TERMUX-API REQUIRED")
        if not os.path.isfile(os.environ["PREFIX"]+"/bin/termux-media-player"):
            print("You must install Termux-Api\n install from F-Droid")
            os.system("pkg install termux-api")
            exit()
        else:
            scann()
            
def dlvid(url):
    yu = yt(url)
    hr = yu.streams.get_highest_resolution(); karak = "([''+-_&$#@¥{}] )|:"
    #hrz = hr.url
    nam = "{}.mp4".format(yu.title)
    for i in karak:
        nam = nam.replace(i,"")
    hr.download(output_path="/sdcard/Download/video", filename=nam)
    print("Berhasil Download, File saved in /sdcard/Download/video")
    os.system("xdg-open {}".format("/sdcard/Download/video"+nam))
    """rr = get(hrz, stream=True); print(rr)
    if rr.status_code == 200:
        #print(f"File size: {bytesto(fz, 'm')}Mb")
        with open(f"download/video/{nam}.mp4", "wb") as f:
            f.write(rr.content)
            print("Berhasil\nwith name {}.mp4".format(nam))
            f.close()
    else:
        print("gagal")"""
    
def bytesto(bytes, to, bsize=1024):
    a = {'k' : 1, 'm': 2, 'g' : 3, 't' : 4, 'p' : 5, 'e' : 6 }
    r = float(bytes) / bsize
    for i in range(a[to]):
        sr = r / bsize
        return str(sr)[0:4]
