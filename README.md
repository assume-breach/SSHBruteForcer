# SSHBruteForcer
A simple SSH brute force tool written in Python3 that can return a meterpreter reverse shell. 

Usage:

git clone https://github.com/assume-breach/SSHBruteForcer.git

pip install -r requirements.txt

Edit the source code for your hostname, username, password, MSF reverse shell.

(There is also functionality to automatically download /etc/passwd and /etc/shadow from the host, but the user must have access)

python3 SSHBruteForcer.py
