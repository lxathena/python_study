# Script Name   : nslookup_check.py 
# Description   : This very simple script opens a file including server list and does a nslookup for each one


import subprocess

fileName = input("input a file name including server list: ")
for server in open(fileName):
    #print("Server: %s" % server)
    subprocess.Popen(('nslookup ' + server))