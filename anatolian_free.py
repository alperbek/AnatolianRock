#! /usr/bin/python3
# by @raifpy 

# pip3 install youtube-dl
# pip3 install requests
# pip3 install bs4

import requests,os,sys,json
from bs4 import BeautifulSoup as bs
import urllib.request as req

token = "" # Bot tokeni
id = ""  # Kanal , grup , chat id'si


if not os.path.exists("indirilenler"):      # indirilenler adlı bir eleman yok ise:
    os.mkdir("indirilenler")                # indirililenler adlı bir klasör aç

os.chdir("indirilenler")                    # artık varsayılan konumumuz indirilenler 
                                            # Bunu yaptık çünkü inen müziklerin yanlış yerde yer kaplamasını istemeyiz

def yolla(veri,title):                                                                                      
    print("\n"+"-"*50+"\n")
                                                                                                    # Bu eleman müziğin yapımcısını belirtiyor [Ufak reklam aracı da olabilir :)]
    kontrol = requests.post(f"https://api.telegram.org/bot{token}/sendAudio?chat_id={id}&title={title}&performer=@AnatolianRock",files={"audio":veri}).text
    _kontrol = json.loads(kontrol)
    if _kontrol["ok"] == True:
        print("\033[32mBaşarılı !\033[0m")
    else:
        print("\033[31mBaşarısız !\033[0m")
        print(kontrol)
    
    sys.exit("\nhttps://t.me/AnatolianRock | https://t.me/LinuxDepo \n") # Başına # koyarak bu yazıdan rahatlıkla kurtulabilirsin . Sinirlenme :)

argv = sys.argv

if len(argv) == 1:
    sys.exit(f"\n\tKullanım : \n\t{sys.argv[0]} https://youtu.be/link \n") # Link formatı youtu.be şeklinde olmalı . AKsi türlü upload ederken dosyayı bulamayacak , manuel olarak girmeniz istenecektir

else:
    if argv[1].startswith("https://youtube.com") or argv[1].startswith("https://www.youtube.com"):
        argv[1] = "https://youtu.be/"+argv[1][argv[1].rfind("/")+9:]
    kaynak = bs(req.urlopen(argv[1]).read(),"html.parser")
    title = kaynak.find("title").text.replace("- YouTube","").strip()+"-"+argv[1].split("/")[::-1][0]+".mp3"
    
    tit = kaynak.find("title").text.replace("- YouTube","").strip()
    tit = tit.replace("&","-")
    print(tit)
    print(f"\033[32m{title}\033[0m |Indiriliyor !")
    os.system(f"youtube-dl -x --audio-format mp3 {argv[1]}")
    if os.path.exists(title):
        print(f"\033[32m{title}\033[0m |Indirilidi !")
        print(f"\033[34m{title}\033[0m |Upload Ediliyor !")
        yolla(veri=open(title,"rb"),title=tit)




    else:
        print(f"\033[31m{title}\033[0m |Bulunamadı !")
        for i in [a for a in os.listdir() if a.startswith(title[:6])]:
            print("\033[31mOlabilir ! ---> \033[0m"+i)

        title = input("Yüklenecek mp3 tam adı : ")
        if os.path.exists(title):
            print(f"\033[34m{title}\033[0m |Upload Ediliyor !")
            yolla(veri=open(title,"rb"),title=tit)

        else:
            sys.exit("\033[31m B U L U N A M A D I\033[0m")

# Geliştirmeye açık ..

# @AnatolianRock Telegram kanalı için oluşturulmuş bot betiği örneği

# Yeterki bilgi yayalım virüs değil ..
