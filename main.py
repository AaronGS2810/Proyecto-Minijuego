import random
import time

# DATOS
palabras_por_longitud = {
    4: ["casa", "amor", "niño", "vida", "pera", "mano", "mesa", "tuna", "ropa"],
    5: ["perro", "mujer", "tarde", "niños", "madre", "padre", "radio", "plato", "calle"],
    6: ["camino", "amigos", "nevera", "mañana", "comida", "escena", "pueblo", "ciudad", "dinero"],
    7: ["montaña", "persona", "domingo", "familia", "momento", "ventana", "botella", "trabajo", "silencio"],
    8: ["cuaderno", "escalera", "bombilla", "computar", "chorizos", "panadero", "mensajes", "problema", "telefono"],
    9: ["universos", "mensajero", "mariposas", "aguacates", "escritora", "activista", "televisor", "diligente", "habitante"],
    10: ["bicicletas", "panoramica", "cumpleaños", "revolucion", "fotografia", "organizado", "enfermeria", "muletillas", "relaciones"]
}
print("Wordle es un juego de palabras en el que el objetivo es adivinar una palabra secreta de cinco letras en un máximo de seis intentos. ")

time.sleep(2)
print("COMENCEMOS!!!!")
time.sleep(1)
print("Las categorías de letras son las siguientes: \n 4 letras \n 5 letras \n 6 letras \n 7 letras \n 8 letras \n 9 letras \n 10 letras")
time.sleep(1)
# INTERACCION CON USUARIO
while True:
    try:
        num = int(input("Introduce un numero de letras: "))
        if num in palabras_por_longitud:
            random_word = random.choice(palabras_por_longitud[num]).upper()
            print(random_word)
            break
        else:
         print("Vuelve a seleccionar el numero")
        
    except ValueError as e:
        print(f"Has tenido un error {e}")

time.sleep(1)

while True:
    try:
        dificultad = int(input("Introduce la dificultad: \n 1. Facil \n 2. Intermedio \n 3. Dificil \n "))

        if dificultad == 1:
            intentos = 6
            print("Has seleccionado nivel FACIL")
            break
        elif dificultad == 2:
            intentos = 5
            print("Has seleccionado nivel INTERMEDIO")
            break
        elif dificultad ==3:
            intentos = 4
            print("Has seleccionado nivel DIFICIL")
            break
        else:
            print(f"Introduce el numero bien")
    except ValueError as e:
        print(f"El error es: \n {e}")


random_list =[]
for letra in random_word:
    random_list.append(letra)

print(random_list)

list_result= []
time.sleep(2)
print("NORMAS IMPORTANTES: \n - Letras en mayuscula son las que pertenecen a la palabra secreta y estan en la posicion correcta \n - Letras en minusculas son las que pertenecen a la palabra secreta pero no estan en la posicion correcta")
time.sleep(1)
# COMIENZA EL JUEGO

while intentos > 0:
    print(f"Te quedan {intentos} intentos")

    #Crear lista con x

    list_empty =[]
    for letra in random_list:
        list_empty.append('_')

    #Pedir palabra al usuario
    
    try:
        while True:
            user_word = str(input("Introduce tu palabra: ")).strip().upper()
            if len(user_word) != len(random_word):
                print(f"Introduce una palabra con la misma cantidad de caracteres que la palabra a encontrar. \n La palabra debe tener {num} caracteres")
            else:
                break
    except TypeError as e:
        print(f"El error es:\n {e}")

    user_list=[]
    for letra in user_word:
        user_list.append(letra)
    
    # Logica del juego

    for i in range(len(random_list)):
        if user_list[i] == random_list[i]:  #letra en posicion correcta
            list_empty[i] = user_list[i].upper()
        elif user_list[i] in random_list:   #letra en la palabra
            list_empty[i] = user_list[i].lower()
        else:
            list_empty[i] = '_'

    list_result.append(list_empty)
    
    #Mostrar todas las combinaciones

    for lista in list_result:
        print(lista)

    if user_list == random_list:
        print("FELICIDADES CRACK!")
        break
    intentos -= 1
    

if intentos == 0:
    print("Mira que hay que ser tronco pero no adivinar esta palabra ya es el colmo...\n La proxima vez prueba a la petanca y aun asi no creo que valgas para eso")

