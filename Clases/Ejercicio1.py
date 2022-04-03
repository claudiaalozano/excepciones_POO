import re

class Correo:

    def __init__ (self, error,correo):
        self.error = error
        self.correo = ["vicente@gmail.com" , "claudia@gmail.com"]
    def error (self, correo_electronico, error):
        try:
            re.search(" @ * . * .com *", correo_electronico)
            print("El correo electronico es correcto, bienvenido a la página web.")
        except:
            ataque = re.search(" @ * . * .com *", correo_electronico)
            if correo_electronico != ataque:
                print ("Se ha producido un ciber ataque.")  
        else:
            

        


            
correo_electronico = input("introduzca el correo electrónico para el inicio de sesión: ")