import os, subprocess
import sys, re, time

global nomer
nomer = []
def pllayed():
    if nomer[0].isdigit():
        print("="*60)
        print("\n\n\tPlaying music loop\n\tCTRL+C for exit\n\tMusic is looping now\n\n")
        print("="*60)
        for i in baca()[int(nomer[0])-1:]:
            nomer.clear()
            print("\nTime sleep",limit())
            print(f"Played music start from {i}\nto last music {baca()[len(baca())-1]}")
            os.popen("termux-media-player play \""+i+"\"")
            subprocess.call("termux-media-player info > source/lists/info.xx",shell=True)
            subprocess.call("termux-media-player info > source/lists/info.xx",shell=True)
            playy()
            for i in range(limit()):
                time.sleep(1)
def frayed():
        print("="*60)
        print("\n\n\tPlaying music loop\n\tCTRL+C for exit\n\tMusic is looping now\n\n")
        print("="*60)
        for i in baca():
            print("Time sleep",limit())
            print(f"Played music from {i} \nto last music {baca()[len(baca())-1]}")
            os.popen("termux-media-player play \""+i+"\"")
            subprocess.call("termux-media-player info > source/lists/info.xx",shell=True)
            subprocess.call("termux-media-player info > source/lists/info.xx",shell=True)
            playy()
            for i in range(limit()):
                time.sleep(1)

def limit():
    f = open("source/lists/info.xx", "r").read()
    dd = f.split("\n")
    es = dd[2].split("/")
    fn = es[1].split(":")
    times = int(fn[1])
    for i in range(100):
        if int(fn[0]) == i:
            times+=60*i
            break
    return times

def getlists():
    if getlastm():
        os.system("termux-media-player stop")
        if os.path.exists("source/lists/mp3.list"):
            os.system("clear")
            runn()
            sorted()
        else:
            scann()

def scann():
    print("Scan a mp3 music in /sdcard path")
    os.system("find -L /sdcard -type f -ipath '*.mp3' >source/lists/mp3.list")              
    print("scan compeleto")
    pil = input("want scan sdcard1/memory-card? y/n ").lower()
    if pil.strip() == 'y':
        os.system("find -L /storage/sdcard1 -type f -ipath '*.mp3' >>source/list/mp3.list")
        print("scan compeleto")
    input("Please enter to continued...")
    runn()                                                                                 
    sorted()

def getlastm():
        subprocess.call("termux-media-player info> source/lists/cek.xx",shell=True)
        f = open("source/lists/cek.xx", "r")
        ff = f.read()
        f.close()
        if len(ff) >= 20:
            return True
        else: 
            return False
        
def runn():
    judl = []
    for i in baca():
        s = i.split("/")
        for x in s:
            if (re.search(r"(.mp3)",x)):
                judl.append(x)
    return judl
    
def sorted():
    f = open("source/lists/mp3.list","r").read()
    if len(baca()) != f.count('\n'):
        af = open("source/lists/mp3.list","w")
        for i in f:
            af.write(i+"\n")
        af.close()
    os.system('sort -bfidu source/lists/mp3.list -o source/lists/mp3.list')
    print("sorting mp3.list")
    playy()

def baca():
    f = open("source/lists/mp3.list","r")
    a = f.read()
    aa = a.split("\n"); aa.remove("")
    f.close()
    return aa

def playy():
    try:
        pp = True
        while pp:
            print("""
            ▀█▀ █▀█ █▀█ █░░ ▄▀█ █▄█
            ░█░ █▀▄ █▀▀ █▄▄ █▀█ ░█░
            22-oct-22{aldyansyahcp}
            
            """)
            for n,i in enumerate(runn(),start=1):
                print(f"{n}. {i}")
            pil = input("\ntype help for command\n\n\tenter the number for play music: ")
            os.system("clear")
            if pil.isdigit():
                os.system("rm souece/lists/info.xx")
                os.popen("termux-media-player play \""+str(baca()[int(pil)-1])+"\"")    
                subprocess.call("termux-media-player info > source/lists/info.xx",shell=True)
                subprocess.call("termux-media-player info > source/lists/info.xx",shell=True)
                subprocess.call(f"echo '\n\n'Playing music {str(baca()[int(pil)-1])}",shell=True)
                if int(pil) >= len(baca()):
                    continue
            if pil == "pause":
                os.system("termux-media-player pause")
            if pil == "resume":
                os.system("termux-media-player play")
            if pil == "exit":
                os.system("termux-media-player stop")
                pp == False
                sys.exit()
            if pil == "back":
                os.system("python yts.py")
            if pil == "resc":
                scann()
            if pil == "info":
                os.system("termux-media-player info")
            if pil == "loop": frayed()
            if pil[5:].isdigit():
                nomer.append(pil[5:])
                pllayed()
            if pil == "help":
                print("""
                    pause: pause music
                    resume: resumed your last music
                    exit: exit media-player
                    back: turn-back to Youtube-Downloader
                    resc: re-scan storage path
                    info: check music played
                    loop: looping the music
                    loop (number): looping music from number start
                """)
    except KeyboardInterrupt:
        print("thank you!! \n\t termux-media-player stop for stop the music")
        exit()
        os.system("termux-media-player stop")
    except IndexError:    
        print("\n\n\tYour input out of range")
