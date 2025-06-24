menu = '''
*** MENÚ PRINCIPAL ***

1. Ingresar mascota.
2. Buscar mascota.
3. Eliminar mascota.
4. Salir.
'''
pets_Register = []
tipo = ["perro","gato","ave"]

def ingresar_mascota(pets_Register,tipo):
    try:
        namePets = input("Ingrese el nombre de la mascota: ").lower().strip()
        for mascota in pets_Register:
            while mascota["nombre"] == namePets:
                print("La mascota que desea ingresar ya existe, vuelve a intentarlo. ")
                namePets = input("Ingrese el nombre de la mascota: ").lower().strip()

        tipoPets = input("Raza de la mascota: ").lower().strip()
        while tipoPets not in tipo:
            print("La raza que ingresaste no está dentro del tipo. Vuelve a intentarlo. ")
            print(tipo)
            tipoPets = input("Raza de la mascota: ").lower().strip()

        edadPets = int(input("Ingrese la edad de la mascota: ").strip())
        while edadPets < 0:
            print("La edad de la mascota debe ser mayor o igual a 0. ")
            edadPets = int(input("Ingrese la edad de la mascota: ").strip())

        mascota = {
                    "nombre":namePets,
                    "tipo":tipoPets,
                    "edad":edadPets
                   }
        
        pets_Register.append(mascota)
        print("Mascota ingresada correctamente. ")
        return "Mascota ingresada correctamente. "
    except ValueError:
        print("La respuesta debe ser en numeros. ")
    except:
        print("Error. ")

def buscar_mascota(pets_Register):
    try:
        namePets = input("Ingrese el nombre de la mascota que buscas: ").lower().strip()
        for mascota in pets_Register:
            if mascota["nombre"] == namePets:
                print(f"La raza de la mascota es: {mascota["tipo"]}, y su edad es de {mascota["edad"]} años. ")
            else:
                print("La mascota que buscas no se encuentra registrada. ")
        return
    except:
        print("Error. ")

def eliminar_mascota(pets_Register):
    try:
        namePets = input("Ingresa el nombre de la mascota que deseas eliminar de los registros: ").lower().strip()
        for mascota in pets_Register:
            if mascota["nombre"] == namePets:
                pets_Register.remove(mascota)
                print("Registro de la mascota eliminado. ")
            else:
                print("El registro de la mascota no se pudo eliminar. ")
        return
    except:
        print("Error. ")

while True:
    print(menu)
    try:
        opcion = int(input("Ingresa una opción: ").strip())
        if opcion == 1:
            ingresar_mascota(pets_Register,tipo)
        elif opcion == 2:
            buscar_mascota(pets_Register)
        elif opcion == 3:
            eliminar_mascota(pets_Register)
        elif opcion == 4:
            print("Ejecución finalizada. ")
            break
        else:
            print("Opción no válida. ")      
    except ValueError:
        print("La opción ingresada debe ser en numero y no en letras. ")