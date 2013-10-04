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
	arguments = sys.argv	
	if len(arguments)>1:
		play = 0
		for nroArg in range(1,len(arguments)):			
			if play:
				play = 0
			else:
				parameter = arguments[nroArg]
				if _arg.has_key(parameter):
					if parameter == "-p":
						_port = arguments[nroArg+1]
						play =1
					elif parameter == "-ip":
						_ip = arguments[nroArg+1]
						play =1
					elif parameter == "-h" or parameter == "-v":
						_arg[parameter]()
						exit()
				else:
					print "unknown parameter", parameter
					exit()				
	
	servidor = Server(ip=_ip,port=_port)
	return 0

if __name__ == '__main__':
	main()

