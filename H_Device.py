
import threading
import analizador

class Device(threading.Thread, analizador.Analizador):
    
    """
        thread that handles a device connected
    """
    
    socket = None    

    def __init__(self):
        self.iniciar_icaro()
        pass

    
    def iniciar(self,socket):
        
        """ starting the thread """
        
        threading.Thread.__init__(self)
        # initialize attributes
        self.socket = socket
        self.activo = True

    def atender(self):
        # recibir paquete
        pkt_rec = self.socket.recv(1024)
        
        if pkt_rec:
            print "pkt recivido:"+str(pkt_rec)
            if self.resolver(pkt_rec):
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
