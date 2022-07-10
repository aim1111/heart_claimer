import requests
from requests import session
import queue
import random
import threading
import time
from threading import Thread
from colorama import Fore
import dhooks
from dhooks import Webhook, Embed
import os
from os import system
session = requests.session()
from queue import Queue
useragents =["Mozilla/5.0 (Android; Linux armv7l; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 Fennec/10.0.1","Mozilla/5.0 (Android; Linux armv7l; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (WindowsCE 6.0; rv:2.0.1) Gecko/20100101 Firefox/4.0.1","Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1","Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2","Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/18.6.872.0 Safari/535.2 UNTRUSTED/1.0 3gpp-gba UNTRUSTED/1.0","Mozilla/5.0 (Windows NT 6.1; rv:12.0) Gecko/20120403211507 Firefox/12.0","Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1","Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2","Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1","Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3","Mozilla/5.0 (Windows; U; ; en-NZ) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.8.0","Mozilla/5.0 (Windows; U; Win98; en-US; rv:1.4) Gecko Netscape/7.1 (ax)","Mozilla/5.0 (Windows; U; Windows CE 5.1; rv:1.8.1a3) Gecko/20060610 Minimo/0.016","Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10","Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7","Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.23) Gecko/20090825 SeaMonkey/1.1.18","Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10","Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)","Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9","Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.6 (Change: )","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.1 (KHTML, like Gecko) Maxthon/3.0.8.2 Safari/533.1","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5","Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14","Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20","Mozilla/5.0 (Windows; U; Windows XP) Gecko MultiZilla/1.6.1.0a","Mozilla/5.0 (Windows; U; WinNT4.0; en-US; rv:1.2b) Gecko/20021001 Phoenix/0.2","Mozilla/5.0 (X11; FreeBSD amd64; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (X11; Linux i686) AppleWebKit/534.34 (KHTML, like Gecko) QupZilla/1.2.0 Safari/534.34","Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.1 (KHTML, like Gecko) Ubuntu/11.04 Chromium/14.0.825.0 Chrome/14.0.825.0 Safari/535.1","Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.2 (KHTML, like Gecko) Ubuntu/11.10 Chromium/15.0.874.120 Chrome/15.0.874.120 Safari/535.2","Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1","Mozilla/5.0 (X11; Linux i686 on x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1 Fennec/2.0.1","Mozilla/5.0 (X11; Linux i686; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1","Mozilla/5.0 (X11; Linux i686; rv:12.0) Gecko/20100101 Firefox/12.0 ","Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1","Mozilla/5.0 (X11; Linux i686; rv:2.0b6pre) Gecko/20100907 Firefox/4.0b6pre","Mozilla/5.0 (X11; Linux i686; rv:5.0) Gecko/20100101 Firefox/5.0","Mozilla/5.0 (X11; Linux i686; rv:6.0a2) Gecko/20110615 Firefox/6.0a2 Iceweasel/6.0a2","Mozilla/5.0 (X11; Linux i686; rv:6.0) Gecko/20100101 Firefox/6.0","Mozilla/5.0 (X11; Linux i686; rv:8.0) Gecko/20100101 Firefox/8.0","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/534.24 (KHTML, like Gecko) Ubuntu/10.10 Chromium/12.0.703.0 Chrome/12.0.703.0 Safari/534.24","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.20 Safari/535.1","Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5","Mozilla/5.0 (X11; Linux x86_64; en-US; rv:2.0b2pre) Gecko/20100712 Minefield/4.0b2pre","Mozilla/5.0 (X11; Linux x86_64; rv:10.0.1) Gecko/20100101 Firefox/10.0.1","Mozilla/5.0 (X11; Linux x86_64; rv:11.0a2) Gecko/20111230 Firefox/11.0a2 Iceweasel/11.0a2","Mozilla/5.0 (X11; Linux x86_64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1","Mozilla/5.0 (X11; Linux x86_64; rv:2.2a1pre) Gecko/20100101 Firefox/4.2a1pre","Mozilla/5.0 (X11; Linux x86_64; rv:5.0) Gecko/20100101 Firefox/5.0 Iceweasel/5.0","Mozilla/5.0 (X11; Linux x86_64; rv:7.0a1) Gecko/20110623 Firefox/7.0a1","Mozilla/5.0 (X11; U; FreeBSD amd64; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0","Mozilla/5.0 (X11; U; FreeBSD i386; de-CH; rv:1.9.2.8) Gecko/20100729 Firefox/3.6.8","Mozilla/5.0 (X11; U; FreeBSD i386; en-US) AppleWebKit/532.0 (KHTML, like Gecko) Chrome/4.0.207.0 Safari/532.0","Mozilla/5.0 (X11; U; FreeBSD i386; en-US; rv:1.6) Gecko/20040406 Galeon/1.3.15","Mozilla/5.0 (X11; U; FreeBSD; i386; en-US; rv:1.7) Gecko","Mozilla/5.0 (X11; U; FreeBSD x86_64; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.204 Safari/534.16","Mozilla/5.0 (X11; U; Linux arm7tdmi; rv:1.8.1.11) Gecko/20071130 Minimo/0.025","Mozilla/5.0 (X11; U; Linux armv61; en-US; rv:1.9.1b2pre) Gecko/20081015 Fennec/1.0a1","Mozilla/5.0 (X11; U; Linux armv6l; rv 1.8.1.5pre) Gecko/20070619 Minimo/0.020","Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527  (KHTML, like Gecko, Safari/419.3) Arora/0.10.1","Mozilla/5.0 (X11; U; Linux i586; en-US; rv:1.7.3) Gecko/20040924 Epiphany/1.4.4 (Ubuntu)","Mozilla/5.0 (X11; U; Linux i686; en-us) AppleWebKit/528.5  (KHTML, like Gecko, Safari/528.5 ) lt-GtkLauncher","Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.4 (KHTML, like Gecko) Chrome/4.0.237.0 Safari/532.4 Debian","Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.277.0 Safari/532.8","Mozilla/5.0 (X11; U; Linux i686; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Ubuntu/10.10 Chromium/10.0.613.0 Chrome/10.0.613.0 Safari/534.15","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.6) Gecko/20040614 Firefox/0.8","Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Debian/1.6-7","Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Epiphany/1.2.5","Mozilla/5.0 (X11; U; Linux; i686; en-US; rv:1.6) Gecko Galeon/1.3.14","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.7) Gecko/20060909 Firefox/1.5.0.7 MG(Novarra-Vision/6.9)","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.16) Gecko/20080716 (Gentoo) Galeon/2.0.6","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061024 Firefox/2.0 (Swiftfox)","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.11) Gecko/2009060309 Ubuntu/9.10 (karmic) Firefox/3.0.11","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.16) Gecko/20120421 Gecko Firefox/11.0","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.1.2) Gecko/20090803 Ubuntu/9.04 (jaunty) Shiretoko/3.5.2","Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9a3pre) Gecko/20070330","Mozilla/5.0 (X11; U; Linux i686; it; rv:1.9.2.3) Gecko/20100406 Firefox/3.6.3 (Swiftfox)","Mozilla/5.0 (X11; U; Linux ppc; en-US; rv:1.8.1.13) Gecko/20080313 Iceape/1.1.9 (Debian-1.1.9-5)","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0","Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.0.3) Gecko/2008092814 (Debian-3.0.1-1)","Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8","Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.17) Gecko/20110123 SeaMonkey/2.0.12","Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20091020 Linux Mint/8 (Helena) Firefox/3.5.3","Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.5) Gecko/20091107 Firefox/3.5.5","Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.2.9) Gecko/20100915 Gentoo Firefox/3.6.9","Mozilla/5.0 (X11; U; Linux x86_64; sv-SE; rv:1.8.1.12) Gecko/20080207 Ubuntu/7.10 (gutsy) Firefox/2.0.0.12","Mozilla/5.0 (X11; U; Linux x86_64; us; rv:1.9.1.19) Gecko/20110430 shadowfox/7.0 (like Firefox/7.0","Mozilla/5.0 (X11; U; NetBSD amd64; en-US; rv:1.9.2.15) Gecko/20110308 Namoroka/3.6.15","Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2  (KHTML, like Gecko) Safari/531.2  Epiphany/2.30.0","Mozilla/5.0 (X11; U; OpenBSD i386; en-US) AppleWebKit/533.3 (KHTML, like Gecko) Chrome/5.0.359.0 Safari/533.3","Mozilla/5.0 (X11; U; OpenBSD i386; en-US; rv:1.9.1) Gecko/20090702 Firefox/3.5","Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.8.1.12) Gecko/20080303 SeaMonkey/1.1.8","Mozilla/5.0 (X11; U; SunOS i86pc; en-US; rv:1.9.1b3) Gecko/20090429 Firefox/3.1b3","Mozilla/5.0 (X11; U; SunOS sun4m; en-US; rv:1.4b) Gecko/20030517 Mozilla Firebird/0.6","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.309.0 Safari/532.9","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/10.0.613.0 Safari/534.15","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7","Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/540.0 (KHTML, like Gecko) Ubuntu/10.10 Chrome/9.1.0.0 Safari/540.0","Mozilla/5.0 (Linux; Android 7.1.1; MI 6 Build/NMF26X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/043807 Mobile Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN","Mozilla/5.0 (Linux; Android 7.1.1; OD103 Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN","Mozilla/5.0 (Linux; Android 6.0.1; SM919 Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN","Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN","Mozilla/5.0 (Linux; Android 5.1; HUAWEI TAG-AL00 Build/HUAWEITAG-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043622 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/4G Language/zh_CN","Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13F69 MicroMessenger/6.6.1 NetType/4G Language/zh_CN","Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_2 like Mac https://m.baidu.com/mip/c/s/zhangzifan.com/wechat-user-agent.htmlOS X) AppleWebKit/604.4.7 (KHTML, like Gecko) Mobile/15C202 MicroMessenger/6.6.1 NetType/4G Language/zh_CN","Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1 like Mac OS X) AppleWebKit/604.3.5 (KHTML, like Gecko) Mobile/15B150 MicroMessenger/6.6.1 NetType/WIFI Language/zh_CN","Mozilla/5.0 (iphone x Build/MXB48T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/53.0.2785.49 Mobile MQQBrowser/6.2 TBS/043632 Safari/537.36 MicroMessenger/6.6.1.1220(0x26060135) NetType/WIFI Language/zh_CN",]#line:144
ua =random .choice (useragents )#line:145
proxy_list=['89.140.125.17:80','8.218.242.27:59394','139.59.1.14:3128','194.233.73.106:443','103.168.52.1:1337','194.233.69.126:443','178.124.208.8:3128','150.129.171.35:30093','212.46.230.102:6969','50.206.25.111:80','103.109.58.54:8080','139.162.78.109:3128','47.88.77.62:8080','195.191.246.198:53281','88.198.50.103:3128','5.189.165.226:9999','181.129.52.156:42648','109.167.134.253:30710','118.98.65.146:8081','190.152.5.126:53040','170.238.255.90:31113','185.142.67.23:8080','81.24.92.10:53281','195.138.73.54:44017','129.226.113.45:59394','88.198.24.108:3128','113.130.126.2:31932','88.132.34.230:53281','185.208.172.146:1080','50.206.25.106:80','94.73.239.124:55443','88.198.50.103:8080','8.218.95.237:59394','203.75.190.21:80','191.96.42.80:3128','20.47.108.204:8888','124.107.167.225:8080','43.255.113.232:83','50.206.25.104:80','83.151.2.50:3128','180.250.170.210:59778','176.9.75.42:8080','176.110.121.90:21776','139.162.78.109:8080','88.198.24.108:8080','187.108.39.64:6666','46.4.96.137:8080','94.244.28.246:31280','116.90.229.186:35561','194.233.73.104:443','195.46.164.179:8118','194.233.69.41:443','31.173.94.93:43539','50.206.25.110:80','154.16.63.16:3128','23.107.176.100:32180','43.134.200.122:59394','83.13.251.149:8080','62.205.134.57:30008','46.198.132.228:21231','109.173.102.90:8000','135.148.120.146:8088','116.103.46.15:4004','43.255.113.232:84','50.246.120.125:8080','181.129.183.19:53281','5.252.161.48:3128','68.185.57.66:80','195.209.131.19:46372','144.217.75.65:8800','13.212.167.151:8000','85.26.146.169:80','139.59.1.14:8080','005.252.161.48:8080','131.161.68.37:31264','176.9.119.170:8080','46.4.96.137:3128','49.12.43.32:5555','176.111.73.57:8081','185.201.88.128:6969','85.195.104.71:80','159.203.61.169:3128','101.32.204.67:59394','68.188.59.198:80','154.16.63.16:8080','172.107.96.30:443','93.117.72.27:43631','43.134.213.254:59394','8.218.80.41:59394','176.9.119.170:3128','77.37.157.204:8000','103.145.34.10:55443','176.9.75.42:3128','78.129.239.197:808','8.218.95.30:59394','194.32.128.66:55443','220.87.222.238:8118','191.96.42.80:8080','187.190.64.42:31442','140.227.122.55:59394','181.196.205.250:38178','116.251.214.12:443']#line:249
prox = {'http': 'http://' + (random.choice(proxy_list))}
P = []
def cls():
    os.system('cls')
cls()
users = queue.Queue()
sid = queue.Queue()
A = 0




#menu






os.system('title ~~~  Heart TikTok AutoClaimer Made with love  ~~~')
print(f'''{Fore.MAGENTA}
             ╔════════════════════════════════════╗
             ║{Fore.RESET}{Fore.WHITE}       Heart AutoClaimer <3         {Fore.RESET}{Fore.MAGENTA}║
╔════════════╩════════════════════════════════════╩════════════╗
║          {Fore.RESET}Made and developed by developer#3422{Fore.MAGENTA}                ║
║{Fore.RESET}{Fore.RED}               .....           .....{Fore.RESET}{Fore.MAGENTA}                          ║    
║{Fore.RESET}{Fore.RED}            ,ad8PPPP88b,     ,d88PPPP8ba,{Fore.RESET}{Fore.MAGENTA}                     ║       
║{Fore.RESET}{Fore.RED}           d8P"      "Y8b, ,d8P"       "Y8b{Fore.RESET}{Fore.MAGENTA}                   ║
║{Fore.RESET}{Fore.RED}           dP'           "8a8"            `Yd{Fore.RESET}{Fore.MAGENTA}                 ║
║{Fore.RESET}{Fore.RED}           8(              "               )8{Fore.RESET}{Fore.MAGENTA}                 ║
║{Fore.RESET}{Fore.RED}           I8                             8I{Fore.RESET}{Fore.MAGENTA}                  ║
║{Fore.RESET}{Fore.RED}            Yb,                         ,dP{Fore.RESET}{Fore.MAGENTA}                   ║
║{Fore.RESET}{Fore.RED}            "8a,                     ,a8"{Fore.RESET}{Fore.MAGENTA}                     ║
║{Fore.RESET}{Fore.RED}              "8a,                 ,a8"{Fore.RESET}{Fore.MAGENTA}                       ║
║{Fore.RESET}{Fore.RED}                "Yba             adP"   {Fore.RESET}{Fore.MAGENTA}                      ║
║{Fore.RESET}{Fore.RED}                  `Y8a         a8P'{Fore.RESET}{Fore.MAGENTA}                           ║
║{Fore.RESET}{Fore.RED}                    `88,     ,88'{Fore.RESET}{Fore.MAGENTA}                             ║
║{Fore.RESET}{Fore.RED}                     "8b   d8"{Fore.RESET}{Fore.MAGENTA}                                ║
║{Fore.RESET}{Fore.RED}                      "8b d8"{Fore.RESET}{Fore.MAGENTA}                                 ║
║{Fore.RESET}{Fore.RED}                       `888'{Fore.RESET}{Fore.MAGENTA}                                  ║
║{Fore.RESET}{Fore.RED}                         "{Fore.RESET}{Fore.MAGENTA}                                    ║                   
╚══════════════════════════════════════════════════════════════╝
{Fore.RESET}''')
t = 0






#variable definitions
ua = random.choice(useragents)

headers = {

                    'user-agent': f'{ua}'

                    }
rs = 0
req = 0
er = 0
p_file = 'proxies.txt'
userslist = 'users.txt'
prox = {'http': 'http://' + (random.choice(proxy_list))}
P = []
def cls():
    os.system('cls')

users = queue.Queue()
sid = queue.Queue()
A = 0















#loading files






for line in open('sessions.txt', 'r'):
    sid.put(line.strip())
    A += 1

threads = int(input(f'{Fore.RED}<{Fore.RESET}{Fore.MAGENTA}/{Fore.RESET}{Fore.RED}3 Threads: '))
cls()
mode = int(input(f'''{Fore.RED}<{Fore.RESET}{Fore.MAGENTA}/{Fore.RESET}{Fore.RED}3 
Proxy[{Fore.RESET}1{Fore.RED}] 
No-Proxies[{Fore.RESET}2{Fore.RED}]
'''))
cls()
huk = input(f'{Fore.RED}<{Fore.RESET}{Fore.MAGENTA}/{Fore.RESET}{Fore.RED}3 Webhook: ')
hook = Webhook(huk)
for line in open(userslist, 'r'):
            users.put(line.strip())
if mode == 1:
    p_file = 'proxies.txt'
    for i in open(p_file, 'r').read().splitlines():
            P.append(i)
            t += 1


url = 'https://api16-normal-useast5.us.tiktokv.com/passport/login_name/update/?iid=7057246312312293126&device_id=7053635664542713349&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=230005&version_name=23.0.5&device_platform=android&ab_version=23.0.5&ssmix=a&device_type=SM-G935F&device_brand=samsung&language=en&os_api=25&os_version=7.1.2&openudid=41310efbcad241a7&manifest_version_code=2022300050&resolution=900*1600&dpi=300&update_version_code=2022300050&_rticket=1644102101649&current_region=NF&app_type=normal&sys_region=US&mcc_mnc=50571&timezone_name=America%2FChicago&residence=US&ts=1644102100&timezone_offset=-21600&build_number=23.0.5&region=US&uoo=0&app_language=en&carrier_region=AU&locale=en&op_region=AU&ac2=wifi&host_abi=x86&cdid=ee99e3e9-148f-46b5-8884-0bac07ac7337&support_webview=1&okhttp_version=4.1.73.9-tiktok'

def claim(user):
    ssid = sid.get()
    global prox
    head = {
            'accept-encoding': 'gzip',
            'connection': 'Keep-Alive',
            'content-length': '10',
            'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'cookie': f'sessionid={ssid}',
            'host': 'api16-normal-useast5.us.tiktokv.com',
            'multi_login': '1',
            'passport-sdk-version': '19',
            'sdk-version': '2',
            'user-agent': f'com.zhiliaoapp.musically/2022300050 (Linux; U; Android 7.1.2; en_US; SM-G935F; Build/N2G48H;tt-ok/3.10.0.2)',
        }
    try:
        r = session.post(url, headers=head, proxies=prox, data=f'login_name={user}').text
    except:
        pass
    if 'success' in r:
        print(f'{Fore.RED}[{Fore.RESET}MSG{Fore.RED}] </3 success claim {user} </3', end='                                           \n')
        hook.send(f'''
        Success claim!!
        User [{user}](https://tiktok.com/@{user})
        Requests {req}        ''')
    elif 'attempts' in r:
        print(f'{Fore.RED}[{Fore.RESET}MSG{Fore.RED}] {Fore.RESET}{r}')
        sid.put(ssid)
        users.put(user)
        
    elif 'conversation' in r:
        print(f'{Fore.RED}[{Fore.RESET}MSG{Fore.RED}] {Fore.RESET}{r}')
        users.put(user)
    else:
        print(f'{Fore.RED}[{Fore.RESET}MSG{Fore.RED}] {Fore.RESET}{r}')
        users.put(user)
        sid.put(ssid)

def stats():
    global rs, req, rs, er
    rs = 0
    er = 0
    req = 0
    while True:
        print(f'{Fore.RED}[{Fore.RESET}-{Fore.RED}] Requests {Fore.RESET} {req}  |  {Fore.RESET}{Fore.RED} REQ/SEC {Fore.RESET} {rs} | {Fore.RED} ER {Fore.RESET} {er}', end='        \r')
        att = req
        time.sleep(1)
        rs = req - att
        
def check():
    global prox, req, rs, er, headers
    while True:
        Proxy = random.choice(P)
        Proxy.strip()
        taint = users.get()
        prox = {
				'http': f'http://{Proxy}',
				'https': f'http://{Proxy}'
					}
        ua = random.choice(useragents)

        headers = {

            'user-agent': f'{ua}'

            }
        url = f'https://www.tiktok.com/@{taint}?'
        session.headers.update=headers
        session.proxies = prox
        try:
            rq = session.head(url)
            req += 1
            if rq.status_code == 200:
                users.put(taint)
            elif rq.status_code == 404:
                print(f'{Fore.RED}[{Fore.RESET}MSG{Fore.RED}]{Fore.RESET} Trying to claim {taint}', end='                                           \n')
                claim(taint)
                
            elif rq.status_code == 403:
                er += 1
                users.put(taint)
            else:
                users.put(taint)
                er += 1
        except:
            pass
        
cls()
print(f'''{Fore.RESET}
{Fore.RED}
    [{Fore.RESET}STATS{Fore.RED}]

[{Fore.RESET}>{Fore.RED}] Users {users.qsize()}
[{Fore.RESET}>{Fore.RED}] Ssids {sid.qsize()}
[{Fore.RESET}>{Fore.RED}] Proxies {t}
[{Fore.RESET}>{Fore.RED}] Threads {threads}''')
time.sleep(2)
thread = []   
for i in range(threads):
                    t = threading.Thread(target=check)
                    
                    t.start()
                    thread.append(t)
threading.Thread(target=stats).start()
for threads in thread:
                    threads.join()

