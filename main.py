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

