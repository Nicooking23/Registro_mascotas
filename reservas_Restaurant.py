menu = '''
*** MENÚ PRINCIPAL ***

1. Ingresar reserva.
2. Buscar reserva.
3. Cancelar reserva.
4. Salir.
'''
reservas = []

def ingresar_reserva():
    try:
        nombreCliente = input("Ingresa tu nombre: ").capitalize().strip()
        for cliente in reservas:
            while cliente["nombre"] == nombreCliente:
                print("El nombre que ingresaste ya tiene una reserva, intentalo nuevamente. ")
                nombreCliente = input("Ingresa tu nombre: ").capitalize().strip()

        fechaCliente = input("Ingrese la fecha de reserva (Formato xx/xx/xxxx): ").strip()
        while
    except:
        print("Error. ")