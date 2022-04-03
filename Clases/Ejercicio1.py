import re

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