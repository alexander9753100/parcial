import json


# Cargar los usuarios existentes desde un archivo JSON o crear una lista vacía
try:
    with open('usuarios.json') as f:
        usuarios = json.load(f)
except FileNotFoundError:
    usuarios = []
print("___________________________________________________________")
def main_menu():
    print("Bienvenido al menú principal")
    print("1. Iniciar sesión")
    print("2. Crear usuario")
    print("0. Salir")

    selection = input("Ingrese el número de la opción que desea: ")
    print("___________________________________________________________")
    
    
    if selection == "1":
        login()
    elif selection == "2":
        crear_usuario()
    elif selection == "0":
        print("Hasta luego.")
        exit()
    else:
        print("Opción no válida. Por favor, ingrese un número del 0 al 2.")
        main_menu()


def login():
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    
    # Buscar al usuario en la lista de usuarios
    for usuario in usuarios:
        if usuario['username'] == username and usuario['password'] == password:
            print("Bienvenido,", username)
            shopping_menu()
            break
    else:
        print("Nombre de usuario, contraseña o edad incorrectos. Intente nuevamente.")
        login()
    print("-------------------------------------------------------------------------------------------------")


def crear_usuario():
    username = input("Ingrese un nombre de usuario: ")
    password = input("Ingrese una contraseña: ")

    # Agregar el usuario a la lista de usuarios y guardar en archivo
    usuarios.append({'username': username, 'password': password})
    with open('usuarios.json', 'w') as f:
        json.dump(usuarios, f)

    print("Usuario creado exitosamente.")
    main_menu()
print(".................................................................................................")

def shopping_menu():
    print("Menú de compras")
    print("1. Nintendo")
    print("2. Consolas Retro")
    print("3. Menú de juegos de PC")
    print("4. Menú de Xbox")
    print("5. Menú de Juegos de Mesa")
    print("0. Cerrar sesión")
    selection = input("Ingrese el número de la opción que desea: ")
    print(".................................................................................................")
    if selection == "1":
        nintendo_menu()
    elif selection == "2":
        retro_menu()
    elif selection == "3":
          pc_menu() 
    elif selection == "4":
        xbox_menu()
    elif selection == "5":
        mesa_menu() 
    elif selection == "0":
        print("Cerrando sesión...")
        main_menu()
    else:
        print("Opción no válida. Por favor, ingrese un número del 0 al 5.")
        shopping_menu()
    print(".................................................................................................")

def nintendo_menu():
    print("Menú de Nintendo")
    print("1. Nintendo Switch")
    print("2. Nintendo Switch Lite")
    print("3. Nintendo 3DS")
    print("0. Volver al menú principal")

    selection = input("Ingrese el número de la opción que desea: ")
    print("-------------------------------------------------------------------------------------------------")
    if selection == "1":
        print("Has seleccionado Nintendo Switch.")
        precio = 299.99
    elif selection == "2":
        print("Has seleccionado Nintendo Switch Lite.")
        precio = 199
    elif selection == "3":
        print("Has seleccionado Nintendo 3DS.")
        precio = 149.99
    elif selection == "0":
        shopping_menu()
        return
    else:
        print("Opción no válida. Por favor, ingrese un número del 0 al 3.")
        nintendo_menu()
    print("-------------------------------------------------------------------------------------------------")

    print("El precio de su selección es:", precio)
    comprar(precio)


def retro_menu():
    print("Menú de Consolas Retro")
    print("1. PlayStation 2")
    print("2. Nintendo 64")
    print("3. SEGA Genesis")
    print("0. Volver al menú principal")

    selection = input("Ingrese el número de la opción que desea: ")
    print("-------------------------------------------------------------------------------------------------")
    if selection == "1":
        print("Has seleccionado PlayStation 2.")
        precio = 129.99
    elif selection == "2":
        print("Has seleccionado Nintendo 64.")
        precio = 99.99
    elif selection == "3":
        print("Has seleccionado SEGA Genesis.")
        precio = 89.99
    elif selection == "0":
        shopping_menu()
        return
    else:
        print("Opción no válida. Por favor, ingrese un número del 0 al 3.")
        retro_menu()

    comprar(precio)
    print("-------------------------------------------------------------------------------------------------")

def pc_menu():
    print("Menú de PC Gaming")
    print("1. PC Gamer Armado")
    print("2. Tarjeta de Video GTX 1080")
    print("3. Monitor Curvo")
    print("0. Volver al menú principal")

    selection = input("Ingrese el número de la opción que desea: ")
    print("-------------------------------------------------------------------------------------------------")
    if selection == "1":
        print("Has seleccionado PC Gamer Armado.")
        precio = 999.99
    elif selection == "2":
        print("Has seleccionado Tarjeta de Video GTX 1080.")
        precio = 399.99
    elif selection == "3":
        print("Has seleccionado Monitor Curvo.")
        precio = 299.99
    elif selection == "0":
        shopping_menu()
        return
    else:
        print("Opción no válida. Por favor, ingrese un número del 0 al 3.")
        pc_menu()

    print("El precio de su selección es:", precio)
    comprar(precio)
    print("-------------------------------------------------------------------------------------------------")

def xbox_menu():
    print("Menú de Xbox")
    print("1. Xbox Series X")
    print("2. Xbox Series S")
    print("3. Xbox One")
    print("0. Volver al menú principal")
    print("-------------------------------------------------------------------------------------------------")
    selection = input("Ingrese el número de la opción que desea: ")

    if selection == "1":
        print("Has seleccionado Xbox Series X.")
        precio = 499.99
    elif selection == "2":
        print("Has seleccionado Xbox Series S.")
        precio = 299.99
    elif selection == "3":
        print("Has seleccionado Xbox One.")
        precio = 249.99
    elif selection == "0":
        shopping_menu()
        return
    else:
        print("Opción no válida. Por favor, ingrese un número del 0 al 3.")
        xbox_menu()
    print("-------------------------------------------------------------------------------------------------")
    print("El precio de su selección es:", precio)
    comprar(precio)

def mesa_menu():
    print("Menú de Juegos de Mesa")
    print("1. Monopoly")
    print("2. Catan")
    print("3. Risk")
    print("4. UNO")
    print("0. Volver al menú principal")

    selection = input("Ingrese el número de la opción que desea: ")
    print("-------------------------------------------------------------------------------------------------")
    if selection == "1":
        print("Has seleccionado Monopoly.")
        precio = 29.99
    elif selection == "2":
        print("Has seleccionado Catan.")
        precio = 34.99
    elif selection == "3":
        print("Has seleccionado Risk.")
        precio = 39.99
    elif selection == "4":
        print("Has seleccionado UNO.")
        precio = 5.00
    elif selection == "0":
        shopping_menu()
        return
    else:
        print("Opción no válida. Por favor, ingrese un número del 0 al 4.")
        mesa_menu()
    print("-------------------------------------------------------------------------------------------------")
    print("El precio de su selección es:", precio)
    comprar(precio)



def comprar(precio):
    print(f"El precio del artículo es de ${precio}.")
    confirmacion = input("¿Desea realizar la compra? (s/n): ")
    
    while confirmacion == "s":
        print("¿Desea comprar nuevamente?")
        if shopping_menu():
            if confirmacion.lower() == "s":
                print("Compra realizada con éxito. Gracias por comprar con nosotros.")
                main_menu()
            elif confirmacion.lower() == "n":
                print("Compra cancelada. Volviendo al menú principal...")
                main_menu()
            else:
                print("Opción no válida. Por favor, ingrese 's' o 'n'.")
                comprar(precio)
        else:
            print("De acuerdo, hasta la proxima")
    

    print("-------------------------------------------------------------------------------------------------")

# Iniciar la aplicación
main_menu()



#Este programa es un pequeño simulador de compras en línea que permite al usuario crear una cuenta, iniciar sesión y navegar por diferentes categorías de productos. El programa tiene las siguientes variables
#usuarios: Una lista que contiene un diccionario para cada usuario creado. Cada diccionario tiene tres claves: username, passwordy age.
#selection: Una variable que almacena la opción seleccionada por el usuario en cada menú.
#username, password, age: Variables que almacenan el nombre de usuario, la contraseña y la edad ingresados ​​por el usuario al iniciar sesión o crear una cuenta.
#precio: Una variable que almacena el precio del producto seleccionado por el usuario.
#f: Una variable que representa el archivo de usuarios que se abre para leer o escribir la lista de usuarios.
