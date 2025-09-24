from Clase.Clientes import Cliente
from Clase.Proveedores import Proveedor
from Clase.Comprobantes import Comprobante
from Clase.Usuarios import GestorDeUsuarios
from Metodos.Validaciones import *
from Metodos.Importes import *

def obtener_datos_usuario():
    
    print("\n--- Ingreso de Datos del Usuario ---")
    nombre = input("Nombre completo o razón social: ")
    cuit = input("CUIT/ID Fiscal: ")
    usuario = input("Nombre de usuario para el login: ")
    clave = input("Contraseña: ")
    return nombre, cuit, usuario, clave

if __name__ == "__main__":
    
    # 1. Configuración inicial
    gestor_de_usuarios = GestorDeUsuarios()
    
    # 2. Creación y registro de usuarios
    print("--- Proceso de Registro de Cliente ---")
    nombre_c, cuit_c, user_c, pass_c = obtener_datos_usuario()
    cliente_ejemplo = Cliente(nombre_c, cuit_c, user_c, pass_c)
    gestor_de_usuarios.registrar_usuario(cliente_ejemplo)

    print("\n--- Proceso de Registro de Proveedor ---")
    nombre_p, cuit_p, user_p, pass_p = obtener_datos_usuario()
    proveedor_ejemplo = Proveedor(nombre_p, cuit_p, user_p, pass_p)
    gestor_de_usuarios.registrar_usuario(proveedor_ejemplo)
    
    print("\n" + "-" * 40)

    # 3. Simulación de un login
    print("--- Simulación de Login ---")
    user_login = input("Ingrese su nombre de usuario: ")
    pass_login = input("Ingrese su contraseña: ")
    
    usuario_ingresado = gestor_de_usuarios.login(user_login, pass_login)
    
    if not usuario_ingresado:
        print("\nLogin fallido. Terminando la aplicación.")
        exit()
        
    print("\n" + "-" * 40)

    # 4. Creación de un comprobante con datos ingresados
    print("--- Creación de Comprobante ---")
    try:
        numero_comprobante = int(input("Ingrese el número de comprobante (12 dígitos): "))
        kg = float(input("Ingrese los kilogramos del envío: "))
        tarifa = float(input("Ingrese la tarifa por kilogramo: "))
        fecha = input("Ingrese la fecha del comprobante (YYYY-MM-DD): ")
        
        if validar_comprobante_numero(numero_comprobante):
            print(f"El número de comprobante {numero_comprobante} es válido.")
            
            comprobante1 = Comprobante(
                numero=numero_comprobante,
                fecha=fecha,
                cliente=cliente_ejemplo,
                proveedor=proveedor_ejemplo,
                kg=kg,
                tarifa=tarifa
            )
            
            print("\n--- Resumen del Comprobante Creado ---")
            print(f"Número: {comprobante1.numero}")
            print(f"Cliente: {comprobante1.cliente.nombre}")
            print(f"Proveedor: {comprobante1.proveedor.nombre}")
            print(f"Importe Total: ${comprobante1.importe_total:.2f}")

        else:
            print("El número de comprobante no es válido. No se puede crear.")
            
    except ValueError:
        print("Error: Los valores de número, kg o tarifa deben ser numéricos.")