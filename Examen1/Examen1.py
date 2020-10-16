#Ejercicio 1: Suma de los 100 primeros numeros naturales
def Suma_1():
    suma = (100+1)*100/2
    print(round(suma))
    print ("")

#Ejercicio 2:  Suma de los n primeros numeros naturales
def Suma_2():
    n = int(input("Ingresa un numero natural: "))
    suma = (n+1)*n/2
    print(round(suma))
    print ("")

#Ejercicio 3:  Suma de los n primeros numeros naturales con verificacion
def Suma_3():
    while True:
        try:
            n = int(input("Ingresa un numero natural: "))
            if n < 0:
                n = int("1.0")
        except ValueError:
            print("Ingresa un numero correcto.\n")
        else:
            suma = (n+1)*n/2
            print(round(suma))
            print ("")
            break
            

def menu():
	print ("Selecciona una opción")
	print ("\t1 - Suma de los primeros 100 numeros naturales.")
	print ("\t2 - Suma de los primeros n numeros naturales (sin verificacion)")
	print ("\t3 - Suma de los primeros n numeros naturales (con verificacion)")
	print ("\t0 - Salir")
 
 
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("inserta un numero valor >> ")
 
	if opcionMenu=="1":
		print ("")
		Suma_1()
	elif opcionMenu=="2":
		print ("")
		Suma_2()
	elif opcionMenu=="3":
		print ("")
		Suma_3()
	elif opcionMenu=="0":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
        


