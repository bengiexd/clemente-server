#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  main.py
#  
#  Copyright 2013 valentin basel <valentin@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import sys

import ServerDispositivos
		
def HELP():
	print "ayuda"

def VERSION():
	print "version"

puerto = None

def main():
	puerto = None
	ip = None
	arg={"-h": HELP,"-v":VERSION,"-p":puerto}
	argumentos = sys.argv
	if len(argumentos)>1:
		for nroArg in range(1,len(argumentos)):
			parametro = argumentos[nroArg]
			if arg.has_key(parametro):
				if parametro == "-p":
					puerto = argumentos[nroArg+1]
					nroArg += 1
				elif parametro == "-ip":
					ip = argumentos[nroArg+1]
					nroArg += 1
				arg[parametro]()
			else:
				print "no se reconoce el comando ", dat
				exit()
	if puerto is not None and ip is not None:
		servidor = ServerDispositivos.Servidor(ip=ip,puerto=puerto)
	elif ip is not None:
		servidor = ServerDispositivos.Servidor(ip=ip)
	elif puerto is not None:
		servidor = ServerDispositivos.Servidor(puerto=puerto)
	else:
		servidor = ServerDispositivos.Servidor()
	return 0

if __name__ == '__main__':
	main()

