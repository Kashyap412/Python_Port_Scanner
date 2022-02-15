#!/bin/python
#python3 scanner.py 127.0.0.1

import sys
import socket
from datetime import datetime

def Banner(a,target):
	print("\n"+"#"*57)
	print("#\t\tWelcome to KashY "+a+"\t\t#")
	print("#\t\tScanning Target	: "+target+"\t\t#")
	print("#\tTime started at\t: "+str(datetime.now())+"\t#")
	print("#"*57+"\n\n")


try:
	#Defining Target
	if len(sys.argv)==2:
		target = socket.gethostbyname(sys.argv[1])	#Translates Hostname to IPv4
	else:
		print("[*] Invalid Arguments !")
		print("Syntax	: python3 scanner.py <ip>")
		print("Example	: python3 scanner.py 127.0.0.1")
		sys.exit()

	#Banner
	Banner("Port Scanner",target)
	
	start_time = datetime.now()
	
	for port in range(0,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target, port))
		if result == 0:
			print("[*] Port {} is open.".format(port))
		s.close()
	End_time = datetime.now()
	elapsed = End_time - start_time
	print("\n\n\tTotal Time Taken:\t"+str(elapsed))
	

except KeyboardInterrupt: 
	print("\nExiting...\n")
	sys.exit()
	
except socket.gaierror:
	print("[*] Hostname can't be resovled.")
	print("Example: ")
	print("\t[*] python3 scanner.py <ip>")
	print("\t[*] python3 scanner.py <domain_name>")
	sys.exit()

except socket.error:
	print("[*] Couldn't connect to Server.")
	sys.exit()