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
	print("-vb: Activar el modo de analisis de vulnerabildiades.")
	print("-vbl: Añadir una lista de banners vulnerables.")
	exit()
def scannbanner(banners, vblist):
	try:
		vbfile = open(vblist, "r")
	except:
		try:
			vbfile = open("vb.txt", "r")
		except:
			print("No se ha podido abrir ninguna lista de vulnerabildiades.")
			exit()
	print("Se ha empezado el análisis de vulnerabildiades.")
	for banner in banners:
	    for b in vbfile:
	        if b.strip("\n") in banner.strip("\n"):
	        	print("\nSe ha encontrado una vulnerabilidad: {}\n".format(b.strip("\n")))
	        	break
	print("El análisis de vulnerabilidad ha acabado.")
	vbfile.close()

def scann(ip, ports): 
	vbanners = []
	print("Iniciando el análisis de puertos...\n\n")
	for port in ports:
		sock = socket(AF_INET, SOCK_STREAM)
		sock.settimeout(3)
		if (sock.connect_ex((ip, port)) == 0 ):
			print("\n[+]El puerto {} está abierto.\n".format(port))
			try:
				banner = sock.recv(1024).decode()
				print("Banner: {}\n".format(banner))
			except:
				continue
			else:
				vbanners.append(banner.strip("\n"))
		sock.close()
	return vbanners

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
		vbnner = False
		vbl = ""
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
			elif arg == "-vb":
				vbnner = True
			elif arg == "-vbl":
				vbl = argv[argvcount + 1]
			else:
				print(msghelp)
				exit()
		for num in range(mn, mx + 1):
			ports.append(num)
		banners = scann(ip, ports)
		if vbnner == True:
			scannbanner(banners, vbl)


