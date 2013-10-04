import time
import socket

from H_Device import Device


class Server(Device):
    
    """ 
        server
            _ip: localhost
            _port: 9000
            _nro_max_devices: 100
    """
    
    _ip = "127.0.0.1"
    _port = 9000
    _nro_max_devices = 100


    def __init__(self, ip=_ip, port=_port):        
    	
    	"""	start the server """
    	
        self._ip = ip
        self._port = port
        self._socket_server = socket.socket()
        self._socket_server.bind((self._ip,self._port))        
        self._socket_server.listen(self._nro_max_devices)
        print "server initiated"
        # accept devices
        self._accept_devices()

    def _accept_devices(self):
        
        """ accept the connection of any device """
        
        while 1:
            (sc, addr) = self._socket_server.accept()
            print "connected client: ",addr
            self.iniciar(sc)
            self.start()


    def shut_down_server(self):
    	
    	""" shut down the server """
    	
        self._socket_server.close()


