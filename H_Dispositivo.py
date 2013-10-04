"""
    Hilo para manejar un dispositivo conectado al servidor
"""

import threading
import analizador

"""
    Hilo que maneja a un dispositivo conectado
"""
class Dispositivo(threading.Thread):

    socket = None
    analizado = analizador.Analizador()

    def __init__(self):
        self.analizado.iniciar_icaro()
        pass

    """
        Autenticar al cliente
    """
    def iniciar(self,socket):
        # iniciar el hilo
        threading.Thread.__init__(self)
        # inicializar atributos
        self.socket = socket
        self.activo = True

    def atender(self):
        # recibir paquete
        pkt_rec = self.socket.recv(1024)
        if pkt_rec:
            print "pkt recivido:"+str(pkt_rec)
            if analizado.resolver(pkt_rec):
                print "ok enviado"
                self.socket.send("OK")
            else:
                self.socket.send("ERROR")
            return True
        else:
            # socket perdido
            return False

    # metodo que se ejecuta en el start del hilo
    def run(self):        
        while self.activo:
            if not self.atender():
                break
        # cerra socket de cliente
        self.socket.close()
        print " socket retirado -- "
