import socket, threading, random, colorama
from contextlib import closing
os.system("clear")
print """
\033[47m\033[31 servers scan\033[0m
\033[32m
__ ___/ _______
_____ \________ __ \     Termux-Lab
____/ //_____/ / / /   VK: @termuxlab
/____/ /_/ /_/

"""
print """\033[33m
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
port = input("\033[35m >>>> ")
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
 ports = input("You port >>> ")
 names = ports
else:
 ports = input("You port >>> ")
 names = ports
downl = 0
count = 0
print 'Search servers...'
print ''
print ''
while True:
 qrand = random.randint(1,225)
 wrand = random.randint(0,255)
 erand = random.randint(0,255)
 rrand = random.randint(0,255)
 host = str(qrand)+"."+ str(wrand)+"."+ str(erand)+"."+str(rrand)
 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 sock.settimeout(1)
 result = sock.connect_ex((host,ports))
 if result == 0:
  print "\033[F\033[36m Servers:"+str(count)+" " + host + """ ~ port OPEN        """
  count += 1
  print ""
  save_file = open("scan.txt", "a+")
  save_file.write("\n "+host+":"+str(ports)+"\n")
  save_file.close()
 else:
  print "\033[F\033[31m Servers:"+str(count)+" "+ str(host)+" - Close\033[0m      "
  
