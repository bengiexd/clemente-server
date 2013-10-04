import sys

import ServerDispositivos
		
def HELP():
	print "help"

def VERSION():
	print "version: 0.001"

_puerto = None

def main():
	_puerto = None
	ip = None
	arg={"-h": HELP,"-v":VERSION,"-p":_puerto}
	argumentos = sys.argv
	if len(argumentos)>1:
		for nroArg in range(1,len(argumentos)):
			parametro = argumentos[nroArg]
			if arg.has_key(parametro):
				if parametro == "-p":
					_puerto = argumentos[nroArg+1]
					nroArg += 1
				elif parametro == "-ip":
					ip = argumentos[nroArg+1]
					nroArg += 1
				arg[parametro]()
			else:
				print "no se reconoce el comando ", dat
				exit()
	if _puerto is not None and ip is not None:
		servidor = ServerDispositivos.Server(ip=ip,_puerto=_puerto)
	elif ip is not None:
		servidor = ServerDispositivos.Server(ip=ip)
	elif _puerto is not None:
		servidor = ServerDispositivos.Server(_puerto=_puerto)
	else:
		servidor = ServerDispositivos.Server()
	return 0

if __name__ == '__main__':
	main()

