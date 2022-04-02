from cgi import print_directory
import re

class Correo:

    def __init__ (self, error):
        self.error = error
    def set_busquedaerror (self,correo_electronico, error):
        try:
            re.search(". * @. * \ .. *", correo_electronico)
            print("El correo electronico es correcto, bienvenido a la página web.")
        except:
            error_ortografia = re.search(". * @. * \ .. *", correo_electronico)
            if correo_electronico != error_ortografia:
                print("Lo sentimos, introduzca una direccion de correo valida.")  
        
    def get_busquedaerror (self):
        print(set.busquedaerror)


            








correo_electronico = input("introduzca el correo electrónico para el inicio de sesión: ")