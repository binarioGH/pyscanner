#!/usr/bin/python
#-*-coding: utf-8 -*-
from socket import *
from sys import argv
def banner():
	print('''          
         ___________     ___________
        |           |   |           |
        |    ___    |   |    ___    |
        |   |___|   |   |   |___|   |   Scanner
        |     ______|   |     ______|
        |    |          |    |
        |    |          |    |
        |    |          |    |
        |____|          |____|

        GitHub: https://github.com/binarioGH
		''')

def h():
	print("Usos:\n-i: Declarar la ip que se va a analizar.")
	print("-p: Agregar un puerto el que a la lista de analizar.")
	print("{} -p 21 -i 192.168.0.1 (Se analiza el puerto 21 de 192.168.0.1)".format(argv[0]))
	print("-min y -max es para poner un rango de puertos a analizar.")
	print("Por ejemplo: {} -min 21 -max 30 -i 192.168.0.1\nEn ese caso se analizaría del puerto 21 al 30.".format(argv[0]))
	exit()

def scann(ip, ports): 
	print("Iniciando el análisis de puertos...\n\n")
	for port in ports:
		sock = socket(AF_INET, SOCK_STREAM)
		sock.settimeout(3)
		if (sock.connect_ex((ip, port)) == 0 ):
			print("\n[+]El puerto {} está abierto.\n".format(port))
			try:
				print("Banner: {}\n".format(sock.recv(1024).strip("\n")))
			except:
				continue
	print("Se ha terminado el análisis de puertos.")

if __name__ == '__main__':
	banner()
	msghelp = "Usa {} -h para ver las opciones.".format(argv[0])
	if "-min" and "-max" and "-p" and "-h" and "-i" not in argv:
		print(msghelp)
		exit()
	else:
		mn = 0
		mx = 0
		argvcount = -1
		ports = []
		ip = str()
		for arg in argv:
			argvcount += 1
			if arg[0] != "-":
				continue
			elif arg == "-h":
				h()
			elif arg == "-min":
				mn = int(argv[argvcount + 1])
			elif arg == "-max":
				mx = int(argv[argvcount + 1])
			elif arg == "-p":
				ports.append(int(argv[argvcount + 1]))
			elif arg == "-i":
				ip = argv[argvcount + 1]
			else:
				print(msghelp)
				exit()
		print("{} {} {} {}".format(ports, mn, mx, ip))
		for num in range(mn, mx + 1):
			ports.append(num)
		print(ports)
		scann(ip, ports)
