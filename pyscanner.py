#!/usr/bin/python
#-*-coding: utf-8 -*-
from socket import *
from sys import argv
from optparse import OptionParser as opt
from os import path

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

def scanbanners(banners, file):
	print("Iniciando analisis de banners.")
	if not path.isfile(file):
		print("El archivo {} no fue encontrado.".format(file))
		exit()
	else:
		print("Archivo de banners vulnerables encontrados...")
		with open(file, "r") as vfile:
			vbanners = vfile.read()
		vbanners = vbanners.split()
	for banner in banners:
		for vbanner in vbanners:
			if vbanner.strip() in banner:
				print("[+]Banner vulnerable: {}".format(banner))
				vbanners.remove(vbanner)				

def scann(ip, ports, timeout): 
	vbanners = []
	print("Iniciando el análisis de puertos...\n\n")
	for port in ports:
		sock = socket(AF_INET, SOCK_STREAM)
		sock.settimeout(timeout)
		if (sock.connect_ex((ip, port)) == 0 ):
			print("\n[+]El puerto {} está abierto.\n".format(port))
			try:
				banner = sock.recv(1024).decode()
				print("Banner: {}\n".format(banner))
			except:
				continue
			else:
				vbanners.append(banner.strip())
		sock.close()
	return vbanners

	print("Se ha terminado el análisis de puertos.")

if __name__ == '__main__':
	banner()
	op = opt("Uso: %prog [banderas] [valores]")
	op.add_option("-i", "--ip", dest="ip", default="none",help="Declarar la ip que se desea analizar.");
	op.add_option("-p", "--port", dest="port", default=-1, type="int",help="Añadir un puerto a la lista de puertos a analizar.")
	op.add_option("-m", "--min", dest="minimo", default=1, type="int", help="Escoger el puerto donde se empezará a analizar.")
	op.add_option("-x", "--max", dest="maximo", default=25, type="int",help="Escoger el puerto donde se acabará de analizar.")
	op.add_option("-v", "--vulbanner", dest="vulns", action="store_true", default=False, help="Activar el modo de analizar vulnerabilidades.")
	op.add_option("-f", "--vulnfile", dest="vfile", default="vb.txt", help="Declarar el archivo con banners vulnerables.")
	op.add_option("-t", "--timeout", dest="timeout", default=5, type="int",help="Declarar el tiempo de espera de un puerto [por default es 5 segundos].")
	(o, argv) = op.parse_args()
	ports = []
	if not o.port == -1:
		ports.append(o.port)
	for num in range(o.minimo, o.maximo+1):
		ports.append(num)

	banners = scann(o.ip, ports, o.timeout)
	if o.vulns:
		scanbanners(banners, o.vfile)
