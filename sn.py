import socket, threading, random
from contextlib import closing
print """
         servers scan
         
     [][][]        [][]    []
     []            [] []   []
     [][][] [][][] []  []  []
         []        []   [] []
     [][][]        []    [][]

          Termux-Lab
        Vk: @termuxlab
"""
print """
[0] - FTP
[1] - SSH
[2] - Telnet
[3] - PRIV-MAIL
[4] - SMTP
[5] - HTTP
[6] - TeamViewer
[7] - ROUTER
[8] - VNC use HTTP
[9] - LOGIN
[10] - SHELL
[11] - Microsoft SQL Server
[12] - PRINTER
[13] - LG TV
[14] - VNC 
[15] - VNC remote desktop protocol
[16] - IP Camera
[100] - Other"""
port = input(">>>> ")
if port == 0:
 ports = 21
elif port == 1:
 ports = 22
elif port == 2:
 ports = 23
elif port == 3:
 ports = 24
elif port == 4:
 ports = 25
elif port == 5:
 ports = 80
elif port == 6:
 ports = 5938
elif port == 7:
 ports = 520
elif port == 8:
 ports = 5800
elif port == 9:
 ports = 513
elif port == 10:
 ports = 514
elif port == 11:
 ports = 1433
elif port == 12:
 ports = 9100
elif port == 13:
 ports = 37904
elif port == 14:
 ports = 5500
elif port == 15:
 ports = 5900
elif port == 16:
 ports = 34567
elif port == 01:
 ports = input("You Port >>> ")
else:
 ports = input("You Port >>> ")

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
   print '>>>>>> ' + host + ' ~ port OPEN'
   break
 else:
   print host + ' ~ port CLOSED'