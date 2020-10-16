from random import randint

#Alumno: Jorge Ivan Perez Perez
#Numero de cuenta: 314211349
#Materia: Probabilidad 1

#Galleta de la fortuna
def galleta():
    fortuna = ['¡Algun tipo de alienigena se te aparecera proximamente!',' Puedo confiar en ti para guardar un secreto.','Ya era hora de que saliera de la galleta.','Disfruta mientras puedas.','¡Ayuda! Estoy siendo prisionero de una pasteleria china']
    print(fortuna[randint(0,4)])
    print("\n")

#Lanzamiento de moneda
def moneda():
    cara = 0
    cruz = 0

    contador = 1

    print("Lanzando moneda 100 veces...\n")

    while contador <= 100:
        aux = randint(0,1)

        if aux == 0:
            cara += 1
        else:
            cruz += 1

        contador += 1

    print(f"Ha salido {cara} veces cara")
    print(f"Ha salido {cruz} veces cruz\n")

def guess():
    
    intentos = 1
    numero = randint(1,100)
    castigos = ['Decir, al revés, los números del 30 al 1, pero sin mencionar los múltiplos de 3','Mandale un mensaje a tu crush','Llama a tu pareja y hazle una confesión falsa','Haz 50 lagartijas','Comete un chile habanero']

    print("Adivina que numero estoy pensando!!")
    print("Tienes 5 intentos, si no lo logras tendras un castigo\n")
   
    while intentos <= 5:

        x = int(input("Ingresa un numero: \n"))
        print("\n")

        if x > numero:
            print("El numero que escogiste es mayor a mi numero..")
            print("Intentalo de nuevo!!\n")
            print(f"Te quedan {5-intentos} intentos\n ")
        elif x < numero:
            print("El numero que escogiste es menor a mi numero..")
            print("Intentalo de nuevo!!\n")
            print(f"Te quedan {5-intentos} intentos\n ")
        else:
            print("Felicidades haz adivinado el numero!!\n")
            break
        
        intentos += 1

    if intentos > 5:
        print("No adivinaste el numero :(")
        print(f"El numero era {numero}\n")
        print(f"Tu castigo es... {castigos[randint(0,4)]}")
        print("\n")



def menu():
	print ("Selecciona una opción")
	print ("\t1 - Galleta de la fortuna.")
	print ("\t2 - Lanzamineto 100 veces de una moneda")
	print ("\t3 - Guess my number")
	print ("\t0 - Salir")
 
 
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu=="1":
		print ("")
		galleta()
	elif opcionMenu=="2":
		print ("")
		moneda()
	elif opcionMenu=="3":
		print ("")
		guess()
	elif opcionMenu=="0":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
    
