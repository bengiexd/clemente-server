import re
import apicaro
import time

class Analizador():
    direcciones = {'ADELANTE':"Adelante",'ATRAS':"Atras",
                   'IZQUIERDA':'Izquierda','DERECHA':"Derecha"}        

    def analizarSintaxis(self,pkt_texto):
        """
            Funcion que analiza si un texto es valido
        """                
        print len(pkt_texto)
        if self.direcciones.has_key(pkt_texto):
            print "esta dentro"
            return 1
        else:
            auxMetodo2 = re.findall("[A-Za-z]+\([0-9]+,[0-9]+\)",pkt_texto)
            if len(auxMetodo2)>0:                
                return 2
            else:
                auxMetodo3 = re.findall("[A-Za-z]+\([0-9]+\)",pkt_texto)
                if len(auxMetodo3)>0:
                    return 3
        return 0


    def decodificar(self,pkt_texto):
        """
            Esta funcion decodifica un paquete de texto
        """        
        caso = self.analizarSintaxis(pkt_texto)
        print "caso: ",caso
        if caso == 1:
            return {'func':self.direcciones[pkt_texto]}
        elif caso == 2 or caso == 3:
            auxMetodo = re.findall("[A-Za-z]+\(",pkt_texto)
            auxValors = re.findall("[0-9]+",pkt_texto)
            funcion = auxMetodo[0][:-1]
            valors = auxValors
            return {'func':funcion,'valors':auxValors}
        else:
            return None

    def resolver(self,pkt_rec):
        """
            Funcion que resuelve una peticion
        """
        pkt_dec = self.decodificar(pkt_rec)
        print "pkt decodificado: ",pkt_dec
        if pkt_dec is None:
            return False

        func = pkt_dec['func']

        if func == 'Adelante':
            self.Adelante()
            return True
        elif func == 'Atras':
            self.Atras()
            return True
        return False

    def iniciar_icaro(self):
        self.icaro = apicaro.puerto()
        if self.icaro.iniciar():
            print "icaro iniciado"            
        else:
            print "no se puede iniciar icaro"        
        #time.sleep(2)
        #icaro.cerrar()
        
    def stop_icaro(self):
        
        """ parar icaro """
        
        self.icaro.cerrar()

    def Adelante(self):
        print 'Adelante'        
        icaro.activar_servo(1,200)            
        time.sleep(2)        

    def Atras(self):
        print 'valor: Atras'




