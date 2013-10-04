import time
import socket
import H_Dispositivo


class Server(H_Dispositivo.Device):
    """ 
        servidor 
            ip: localhost
            puerto: 9000
            nroMaxDispositivos: 100
    """
    #ipDispositivos = "192.168.0.102"
    ipDispositivos = "127.0.0.1"
    puertoDispositivos = 9000
    nroMaxDispositivos = 100

    def __init__(self,ip=ipDispositivos,puerto=puertoDispositivos):
        # socket para atender a los dispositivos remotos        
        self.ipDispositivos = ip
        self.puertoDispositivos = puerto

        self.__servidorDispositivos = socket.socket()
        self.__servidorDispositivos.bind((self.ipDispositivos,self.puertoDispositivos))
        # escuchar dispositivos
        self.__servidorDispositivos.listen(self.nroMaxDispositivos)
        # iniciar Server
        print "Server iniciado"
        self.aceptar_Dispositivos()

    def aceptar_Dispositivos(self):
        """
            funcion para aceptar la conexion de cualquier dispositivo
        """
        while 1:
            # aceptar la conexion de cualquier dispositivo
            (sc, addr) = self.__servidorDispositivos.accept()
            print "cliente conectado: ",addr
            self.iniciar(sc)
            self.start()

    """
        funcion para cerrar el servidor y sus conexiones
    """
    def cerrar_Servidor(self):
        self.__servidorDispositivos.close()


if __name__ == "__main__":
    s = None
    try:
        s = Server()
    finally:
        if s is not None:
            s.cerrar_Servidor()
