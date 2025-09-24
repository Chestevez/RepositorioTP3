from .Clientes import Cliente
from .Proveedores import Proveedor

class GestorDeUsuarios:
    def __init__(self):
        self.usuarios = {}

    def registrar_usuario(self, usuario):
        self.usuarios[usuario.usuario] = usuario
        print(f"Usuario '{usuario.usuario}' registrado con éxito.")

    def login(self, usuario, clave):
        if usuario in self.usuarios and self.usuarios[usuario].clave == clave:
            print(f"Login exitoso para {self.usuarios[usuario].nombre}.")
            return self.usuarios[usuario]
        else:
            print("Error: Usuario o contraseña incorrectos.")
            return None