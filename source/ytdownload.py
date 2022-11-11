from requests import get
from pytube import YouTube as yt
import os,time
from source.pplay import getlists

def dlaud(url):
    yu = yt(url)
    aul = yu.streams.get_audio_only(); karak = "([+-_&$''#@¥,{}] /)|:"
    nam = "{}.mp3".format(yu.title)
    for i in karak:
        nam = nam.replace(i, "")
    aul.download(output_path="/sdcard/Download/audio",filename=nam)
    print("Berhasil Download, file saved in /sdcard/Download/audio")
    p = input("Want to play music?y/n: ").lower()
    if p == "y":
        if os.path.isfile(os.environ["PREFIX"]+"/bin/termux-media-player"):
            os.system("termux-media-player play /sdcard/Download/audio/"+nam)
            print("Trying to run music plauer\ninput resc to scan new file downloaded")
            time.sleep(3)
            played()
    else:
        print("\tTermux media player not installed \n\tYou must install termux-api from F-Droid")
        time.sleep(3)
        os.system("python3 yts.py")
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
        print("\n\t---TERMUX-API REQUIRED---")
        if not os.path.isfile(os.environ["PREFIX"]+"/bin/termux-media-player"):
            print("\n\tYou must install Termux-Api\n install from F-Droid")
            pp = input("\n\tWant to Install termux-api? y/n: ").lower()
            if pp == "y":
                url = "https://f-droid.org/repo/com.termux.api_51.apk"
                print("First Install termux-api & \nopen termux and input command in termux $pkg install termux-api -y \n then input command $termux-setup-storage Accept acces sdcard")
                os.system("xdg-open "+url)
            else:
                os.system("python3 yts.py")
        else:
            getlists()
            
def dlvid(url):
    yu = yt(url)
    hr = yu.streams.get_highest_resolution(); karak = "([''+-_&$#@,¥{}] /)|:"
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
