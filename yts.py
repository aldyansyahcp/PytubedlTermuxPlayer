#coding=utf-8
#aldyansyahcp
#mulai gawene mbuh kapan lali cok
#yagitulah
#hari-hari ngojek ngoding dikira heker kontol
#sampe diresto buka hp terus ngoding dikira ngehek wifi ealah asw
#tapi ya dibawa enjoy aje yekan bab1
#hari-hari duit - terus jirr anjinf
#yang penting udut selalu redi yekan
#kejarlah semua keingin tahuanmu jangan yg keingin tempeanmu su
#thanks for me, for anything about myself, illbe stay standing in here
import pytube, time
from os import system as ss
from source.ytdownload import dlaud, dlvid, played
from source.ply import plls
from source.pplay import getlists

def searc(q):
    s = pytube.Search(q)
    s.results;n=1;s.get_next_results()
    global link
    link = []
    for n,i in enumerate(s.results,start=1):
        print(n,i.title)
        link.append(str(i)[41:52])
    dl()
    
def dl():
    pil = int(input("\npilih no brp? "))-1
    url = "https://youtu.be/"+link[pil]
    ss("clear")
    print(f"\n\n {url} ||",pytube.YouTube(url).title)
    pil = int(input("\nPilih download \n1.Audio\n2.Video \n1/2?> "))
    if pil == 1:
        dlaud(url)
    elif pil == 2:
        dlvid(url)

def main():
    ss("clear")
    print("""
    \n\t 
    █▀█ █▄█ ▀█▀ █░█ █▄▄ █▀▀
    █▀▀ ░█░ ░█░ █▄█ █▄█ ██▄
    
    █▀▄ █▀█ █░█░█ █▄░█ █░░ █▀█ ▄▀█ █▀▄ █▀▀ █▀█
    █▄▀ █▄█ ▀▄▀▄▀ █░▀█ █▄▄ █▄█ █▀█ █▄▀ ██▄ █▀▄
    {22-oct-22}                  {aldyansyahcp}
    \n\t1.Download lagu/video dari link
    \n\t2.Download lagu/video dari playlist
    \n\t3.Download lagu/video dari search query
    \n\t4.Play some music from download playlists
    """)
    try:
        d = int(input("\n\tpilih no? "))
        if d == 1:
            sp = int(input("\n\n\tPilih Download\n\n\t1.Audio\n\t2.Video\n\n\tPilih 1/2>  "))
            url = input("\n\tMasukan link: ")
            if sp == 1:
                dlaud(url)
            elif sp ==2:
                dlvid(url)
        elif d == 2:
            sp = input("\n\n\tMasukan link playlistnya: ")
            plls(sp)
        elif d == 3:
            sp = input("\n\n\tCari lagu apa? ")
            searc(sp)
        elif d == 4:
            played()
        else:
            print("\nYour input out of range")
            time.sleep(2)
            main()
        """except Exception as ex:
            print("something wrong {}\n{}".format(ex,ex.__traceback__.tb_lineno))
            print(ex)"""
    except ValueError: print("Please input a number");time.sleep(2); main()
    except IndexError: print("Please input a number in the session");time.sleep(2); main()
    except FileNotFoundError: print("Run some music first input the number");time.sleep(2);getlists()
    except KeyboardInterrupt: print("Thank you")
if __name__ == "__main__":
    ss("clear")
    main()
