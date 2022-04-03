# excepciones_POO
Mi dirección de Github es: https://github.com/claudiaalozano/excepciones_POO.git

### Enunciado: 
Escriba un programa que simule la conexión de un usuario a un sitio web para el que ya se ha registrado, solo con su dirección de correo electrónico (la gestión de una contraseña está fuera del alcance de esta sección). Este programa debe ofrecer la posibilidad al usuario de introducir una dirección de correo electrónico, y mostrará diferentes mensajes de error en función de la cadena introducida. El programa debe continuar si el correo electrónico indicado tiene un formato incorrecto y finalizar si no se reconoce el correo electrónico, ya que se podría tratar de un ciberataque. Importante: el método que analiza la cadena de caracteres no debe devolver ningún valor.

Comportamiento esperado: la ejecución del programa en una consola se debe desarrollar de la siguiente manera:

vicente: $ python exceptions.py 
--> 
'' es una entrada incorrecta. Introduzca una dirección de correo 
electrónico 
--> t 
Una dirección de correo electrónico debe tener el formato xxx@xxx.xx 
--> t@t.t 
Cuenta bloqueada a causa de un ataque 
vicente: $ python exceptions.py 
--> vicente@eni.es 
¡Bienvenido Vicente!

``` import re

class Correo:

    def __init__ (self, error,correo):
        self.error = error
        
    def error (self, correo_electronico, error):
        try:
            re.search(" @ * . * .com *", correo_electronico)
            if correo_electronico == correo:
                print("El correo electronico es correcto, bienvenido a la página web.")
        except:
            re.search(" @ * . * .com *", correo_electronico)
            if correo_electronico != correo:
                print ("Se ha producido un ciber ataque.")  
        else:
            re.search(" @ * . * .com *", correo_electronico)
            if correo_electronico == None:
                print("El correo intruducido no es valido, hay algún error en la ortografía.")
            

        
correo = ["vicente@gmail.com" , "claudia@gmail.com"]
```
