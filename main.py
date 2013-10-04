import sys

from ServerDevices import Server
		
def HELP():
	print "help"

def VERSION():
	print "version: 0.001"

def main():
	_port = None
	_ip = None
	_arg={"-h": HELP, "-v":VERSION, "-p":_port, "-ip":_ip}	
	argumentos = sys.argv	
	if len(argumentos)>1:
		play = 0
		for nroArg in range(1,len(argumentos)):			
			if play:
				play = 0
			else:
				parametro = argumentos[nroArg]
				if _arg.has_key(parametro):
					if parametro == "-p":
						_port = argumentos[nroArg+1]
						play =1
					elif parametro == "-ip":
						_ip = argumentos[nroArg+1]
						play =1
					elif parametro == "-h" or parametro == "-v":
						_arg[parametro]()
						exit()
				else:
					print "no se reconoce el comando ", parametro
					exit()				
	
	servidor = Server(ip=_ip,port=_port)
	return 0

if __name__ == '__main__':
	main()

