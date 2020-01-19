import socket, threading, random, colorama
from contextlib import closing
print("""
\033[47m\033[31            servers scan\033[0m
  \033[32m       
 _______         _       
(  ____ \       ( (    /|
| (    \/       |  \  ( |
| (_____  _____ |   \ | |
(_____  )(_____)| (\ \) |
      ) |       | | \   |
/\____) |       | )  \  | 𝓣𝓮𝓻𝓶𝓾𝔁-𝓛𝓪𝓫
\_______)       |/    )_) Vk: @termuxlab

""")
print("""\033[33m
0 - 𝓕𝓣𝓟
1 - 𝓢𝓢𝓗
2 - 𝓣𝓮𝓵𝓷𝓮𝓽
3 - 𝓟𝓡𝓘𝓥-𝓜𝓐𝓘𝓛
4 - 𝓢𝓜𝓣𝓟
5 - 𝓗𝓣𝓣𝓟
6 - 𝓣𝓮𝓪𝓶𝓥𝓲𝓮𝔀𝓮𝓻
7 - 𝓡𝓞𝓤𝓣𝓔𝓡
8 - 𝓥𝓝𝓒 𝓾𝓼𝓮 𝓗𝓣𝓣𝓟
9 - 𝓛𝓞𝓖𝓘𝓝
10 - 𝓢𝓗𝓔𝓛𝓛
11 - 𝓜𝓲𝓬𝓻𝓸𝓼𝓸𝓯𝓽 𝓢𝓠𝓛 𝓢𝓮𝓻𝓿𝓮𝓻
12 - 𝓟𝓡𝓘𝓝𝓣𝓔𝓡
13 - 𝓛𝓖 𝓣𝓥
14 - 𝓥𝓝𝓒
15 - 𝓥𝓝𝓒 𝓻𝓮𝓶𝓸𝓽𝓮 𝓭𝓮𝓼𝓴𝓽𝓸𝓹 𝓹𝓻𝓸𝓽𝓸𝓬𝓸𝓵
16 - 𝓘𝓟 𝓒𝓪𝓶𝓮𝓻𝓪
100 - 𝓞𝓽𝓱𝓮𝓻""")
port = input("\033[35m>>>> ")
if port == 0:
 ports = 21
 names = 'FTP'
elif port == 1:
 ports = 22
 names = 'SSH'
elif port == 2:
 ports = 23
 names = 'Telnet'
elif port == 3:
 ports = 24
 names = 'PRIV-MAIL'
elif port == 4:
 ports = 25
 names = 'SMTP'
elif port == 5:
 ports = 80
 names = 'HTTP'
elif port == 6:
 ports = 5938
 names = 'TeamViewer'
elif port == 7:
 ports = 520
 names = 'Router'
elif port == 8:
 ports = 5800
 names = 'VNC use HTTP'
elif port == 9:
 ports = 513
 names = 'LOGIN'
elif port == 10:
 ports = 514
 names = 'SHELL'
elif port == 11:
 ports = 1433
 names = 'Microsoft SQL Server'
elif port == 12:
 ports = 9100
 names = 'Printer'
elif port == 13:
 ports = 37904
 names = 'LG TV'
elif port == 14:
 ports = 3389
 names = 'VNC'
elif port == 15:
 ports = 5900
 names = 'VNC remote desktop protocol'
elif port == 16:
 ports = 34567
 names = 'IP Camera'
elif port == 100:
 ports = input("You Port >>> ")
 names = ports
else:
 ports = input("You Port >>> ")
 names = ports
downl = 0
print('Search servers...')
print('')
while True:
 qrand = random.randint(1,225)
 wrand = random.randint(0,255)
 erand = random.randint(0,255)
 rrand = random.randint(0,255)
 host  = str(qrand)+"."+ str(wrand)+"."+ str(erand)+"."+str(rrand)
 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 sock.settimeout(1)
 result = sock.connect_ex((host,ports))
 if result == 0:
   print('\033[F\033[36m>>>>>> ' + host + ' ~ port OPEN     ')
   break
 else:
    print("\033[F\033[31m"+host+" - Close         ")
