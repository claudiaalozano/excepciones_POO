import re

class Correo:

    def __init__ (self, error):
        self.error = error
    def set_busquedaerror (self,correo_electronico, error):
        try:
            re.search(". * @. * \ .. *", correo_electronico)
            print("")
        except:







correo_electronico = input("introduzca el correo electrónico para comenzar su registro: ")