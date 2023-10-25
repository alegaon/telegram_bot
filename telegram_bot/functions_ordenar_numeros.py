#!/usr/bin/env python

class FuncionesParaElBot:

    def __init__(self):
        self.numeros_lista_nueva = []


    def ordenar_numeros_mayor_a_menor(self, numeros):
        """
        Return a list number
        """        
        for i in numeros.split():
            self.numeros_lista_nueva.append(int(i))

        resultado = sorted(self.numeros_lista_nueva)

        return resultado
    
    
class BotMessages(FuncionesParaElBot):
    
    def __init__(self):
        self.bienvenida = "hola! estoy para ayudarte a ordenar esos numeros, socio"
        self.instructivo_1 = """
        Escribe solo numeros enteros
        Serapa cada numero con un espacio
        Envia el mensaje
        """

    def mensaje_bienvenida(self, message_text):
        if message_text in ('hola', 'hi', 'perro'):
            return self.bienvenida , self.instructivo_1
        return "i don't understand you"

        
    def mensaje_instrucciones(self):
        pass