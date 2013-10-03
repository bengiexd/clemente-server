import PTTC
import Logica

"""
    Clase que administra todos los servicios disponibles del server
"""
class Servicio():
    
    def __init__(self):
        # invocar a la clase que maneja el protocolo del servidor
        self.pttc = PTTC.PTTC()
        # invocar a la capa logica
        self.logica = Logica.Logica()

    """
        funcion que se encarga de realizar acciones de acuerdo a las peticiones del dispositivo conectado
    
        El protocolo devuelve un diccionario con los datos necesarios
           donde:
               primera clave 'method' especifica el tipo de peticion
               segunda clave 'data' es un diccionario con las especificaciones de la peticion del paquete
    """
    def atender(self,pkt_recibido):
        # decodificar paquete recibido
        pkt_datos = self.pttc.peticion(pkt_recibido)

        if pkt_datos['method']=='get':
            if self.get(pkt_datos['data']):
                return True
        elif pkt_datos['method']=='aut':
            if self.aut(pkt_datos['data']):
                return True
        elif pkt_datos['method']=='update':
            if self.update(pkt_datos['data']):
                return True
        else:
            self.reportar_error(1)

    """

    """
    def aut(self,pkt_datos):
        if 'user' in pkt_datos and 'pass' in pkt_datos:
            self.usuario = pkt_datos['user']
            self.password = pkt_datos['pass']
            self.version = pkt_datos['version']
            # consultar a la capa logica sobre la existencia del dispositivo
            if self.logica.Acceso_Dispositivo(self.usuario,self.password):
                return True
        return False

    """
        
    """
    def get(self,pkt_datos):
        if 'huella' in pkt_datos:
            huella = pkt_datos['huella']
            datos_huella = self.logica.datos_huella(huella)
            # armar paquete de huella
            """
            nombres = datos_huella[0]
            ap = datos_huella[1]
            am = datos_huella[2]
            tipo = datos_huella[3]
            data = {'nombres':nombres,'ap':ap,'am':am,'tipo':tipo}
            diccionario = {'method':'update','data':data}
            pkt_env = self.pttc.codificar(diccionario)
            return pkt_env+"\n"
            """
        if 'tema' in pkt_datos:
            tema = pkt_datos['tema']

    """
        
    """
    def update(self,nro):
        pass

    """
        funcion que crea un paquete OK
    """ 
    def ok(self):
        diccionario = {'method':'OK','data':{}}
        pkt_env = self.pttc.codificar(diccionario)
        return pkt_env+"\n"

    """
        funcion que crea un pkt de error
    """
    def error(self):
        diccionario = {'method':'ERROR','data':{}}
        pkt_env = self.pttc.codificar(diccionario)
        return pkt_env

    """
        funcion que se encarga de los errores del server
    """
    def reportar_error(self,nro):
        pass
