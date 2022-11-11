import random
from colorama import init,Fore,Style

def generaCables():
    ''' Genera de forma aleatoria los cables. '''
    listaCables = []
    for i in range (4):
        listaCables.append(random.randint(1,4))
    return listaCables


def imprimirCables(cables):
    ''' Imprime las opciones en consola con sus colores. '''
    for i in range(len(cables)):
        if cables[i] == 1:
            init(autoreset=True)
            print(Fore.RED+"■"*50)
        elif cables[i] == 2:
            init(autoreset=True)
            print(Fore.GREEN+"■"*50)
        elif cables[i] == 3:
            init(autoreset=True)
            print(Fore.CYAN+"■"*50)
        elif cables[i] == 4:
            init(autoreset=True)
            print(Fore.MAGENTA+"■"*50)
         

def solCables(cables,numBomba):
    ''' Recorre la lista y genera la solución. '''
    cablesRojos = cables.count(1)
    cablesAzules = cables.count(3)

    print()
    if cablesRojos >= 2 and numBomba%2 == 1:
        solucion = cables.index(1)
        solucion +=1
        return solucion
    elif cables[3] == 2 and cablesRojos == 0:
        solucion = 1
        return solucion
    elif cablesAzules == 1:
        solucion = 4
        return solucion
    else:
        solucion = 2
        return solucion

def matrizAleatoria(n,m):
    '''Crea una matriz 3x2 vacia'''
    matriz = []
    pos=0
    for i in range(n):
        lista = []
        for j in range(m):
            lista.append(palabraMatriz[pos])
            pos +=1
        matriz.append(lista)    

    return matriz

def printMatriz(matriz):
    '''Imprime la matriz'''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j], end='\t')   
        print()     

def buscaPosicion():
    '''Busca la posicion en donde esta la clave para la contraseña'''
    claveDicc= {
        'GRABE':[0,0],
        'GRAVE':[0,1],
        'BELLO':[1,0],
        'VELLO':[1,1],
        'HAY':[2,0],
        'AHÍ':[2,1]
        }
    
    claveList=['GRABE', 'GRAVE', 'BELLO', 'VELLO', 'HAY', 'AHÍ']
    
    azar = random.choice(claveList)
    a = claveDicc.get(azar)
    return azar,a

def posicionPalabraClave(pos,matriz):
    '''Ecuentra la palabra clave de la contraseña'''
    if pos == [0,0]:
        pos = matriz[0][0]
    elif pos ==[0,1]:
        pos =matriz[0][1]
    elif pos ==[1,0]:
        pos =matriz[1][0]
    elif pos ==[1,1]:
        pos =matriz[1][1]
    elif pos ==[2,0]:
        pos =matriz[2][0]
    elif pos ==[2,1]:
        pos =matriz[2][1]    
    
    return pos

def palabraRespuesta(clave):
    '''Devuelve la contraseña segun la palabra clave'''
    if clave == 'hola':
        clave = 'blanco'
    elif clave == 'ola':
        clave = 'baya'
    elif clave == 'asta':
        clave = 'valla'
    elif clave == 'hasta':
        clave = 'vaya'
    elif clave == 'honda':
        clave = 'onda'
    elif clave == 'onda':
        clave = 'hola'
    elif clave == 'vaya':
        clave = 'ola'
    elif clave == 'valla':
        clave = 'asta'
    elif clave == 'baya':
        clave = 'hasta'
    elif clave == 'blanco':
        clave = 'honda'
    elif clave == 'no sé':
        clave = 'izquierda'
    elif clave == 'derecha':
        clave = 'cual'
    elif clave == 'si':
        clave = 'es'
    elif clave == 'no':
        clave = 'seguro'
    elif clave == 'cual':
        clave = 'derecha'
    elif clave == 'izq':
        clave = 'no se'
    elif clave == 'seguro':
        clave = 'no'
    elif clave == 'es':
        clave = 'si'
    
    return clave

def generarSimbolos():
    '''Genera una lista eligiendo al azar los símbolos'''
    listaSimbolos = ['☺', '╦', 'æ', '÷', '☻', '¬', '§', 'ð', '±', '¾', '«', '½', '¥', '©', 'Â', '×', '■', '~', 'µ', 'Þ', 'Ø']
    azarSimbolos = []
    for i in range (3):
        azarSimbolos.append(random.choice(listaSimbolos))
    return azarSimbolos

def imprimirSimbolos(listaSimbolos,inicio=0):
    '''Imprime la lista de los símbolos al azar con recursividad'''
    if inicio<len(listaSimbolos):
        print(listaSimbolos[inicio], end=' ')
        imprimirSimbolos(listaSimbolos, inicio+1)
    
def comparacionSimbolos(listaSimbolos,respuesta):
    '''Evalúa si lo que ingreso el usuario es correcto'''
    intentos = 0
    while listaSimbolos != respuesta:
        respuesta.clear() #Si no lo aprendimos: respuesta = []
        print('Error - Intente nuevamente: ')
        intentos +=1
        for i in range(3):
            res = input('Ingrese los simbolos 1 a la vez, con los códigos que le indique su compañer@: ')
            respuesta.append(res)
    return intentos

def puntaje(fallos):
    '''Determina el puntaje dependendiendo de la cantidad de fallos'''
    rango = ''
    if fallos == 0:
        rango = 'MAESTRO DESACTIVADOR DE BOMBAS'
    elif fallos in range(1,4):
        rango = 'PLANTINO'
    elif fallos in range(4,10):
        rango = 'ORO'
    elif fallos in range(10,15):
        rango = 'PLATA'
    elif fallos >= 15:
        rango = 'BRONCE'
    return rango        
    
def grabarPuntuacion(fallos,rango):
    '''Carga nombre y puntaje del jugador en un archivo'''
    arch = open('Registros.txt', 'at')
    nombre = input('Ingrese su nombre: ')
    arch.write(nombre+',')
    arch.write('Rango: %s' %rango)
    arch.write('- Fallos: %s' %fallos + '\n')
    
    arch.close()

#Programa Principal
    
# Juego de CABLES    
print('██████╗░██╗░░░██╗██████╗░░█████╗░███╗░░░███╗██████╗░██╗')
print('██╔══██╗╚██╗░██╔╝██╔══██╗██╔══██╗████╗░████║██╔══██╗██║')
print('██████╔╝░╚████╔╝░██████╦╝██║░░██║██╔████╔██║██████╦╝██║')
print('██╔═══╝░░░╚██╔╝░░██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗╚═╝')
print('██║░░░░░░░░██║░░░██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝██╗')
print('╚═╝░░░░░░░░╚═╝░░░╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚═╝')
print()
while True:
    try:
        empezar = input('Presione la tecla "c" para empezar: ')
        while empezar != 'c':
            print('¿No quiere comenzar?')
            empezar = input('Presione la tecla "c" para empezar: ')
        else:
            print()
            numeroBomba = random.randint(100000,999999)
            print('Nº Serial:',numeroBomba)
            a = generaCables()
            imprimir = imprimirCables(a)
            respuestaCorrecta = solCables(a,numeroBomba)

            contador = 1
            while True:
                try:
                    respuesta = int(input('Cortar el cable número: '))
                    while respuesta != respuestaCorrecta:
                        respuesta = int(input('Cortar el cable número: '))
                        contador +=1
                except ValueError:
                    print('Dato inválido.')
                    print('Intente nuevamente: ')
                    contador +=1
                else:
                    break
            print('\a')

            # Juego de TABLA
            palabraMatriz = ['hola', 'ola', 'asta', 'hasta', 'honda', 'onda', 'baya', 'valla', 'vaya', 'blanco', 'no sé', 'izq', 'derecha', 'cual', 'si', 'no', 'es', 'seguro']
            random.shuffle(palabraMatriz)
            buscador = buscaPosicion()

            print(buscador[0].center(13, " ")) #Como me devolvio una Tupla
            ma = matrizAleatoria(3,2)
            printMatriz(ma)
            posicion = posicionPalabraClave(buscador[1],ma)
            print()
            contraseña = palabraRespuesta(posicion)
            respuesta = input('Ingrese su palabra clave: ')
            contador +=1
            while respuesta != contraseña:
                print('Error - intente de nuevo')
                respuesta = input('Ingrese su palabra clave: ')
                contador +=1
            print('\a')

            # Juego de los SIMBOLOS
            simbolos = generarSimbolos()
            imprimirSimbolos(simbolos)
            print()
            cant = 0
            listaRes = []
            contador +=1
            for i in range(3):
                res = input('Ingrese los simbolos 1 a la vez, con los codigos que le indique su experto: ')
                listaRes.append(res)
            resCorrecta = comparacionSimbolos(simbolos,listaRes)
            contador += resCorrecta
            print('\a')

            fallos = contador - 3
            print('Desactivaste la bomba, felicidades!')
            print()
            rank = puntaje(fallos)
            score = grabarPuntuacion(fallos,rank)
            print()
            print('Tus estadisticas:')
            print('Tu rango es: ', rank)
            print('Nº FALLOS:', fallos)
            print()
            print(Style.BRIGHT + '█▀▀ █▀█ ▄▀█ █▀▀ █ ▄▀█ █▀   █▀█ █▀█ █▀█   ░░█ █░█ █▀▀ ▄▀█ █▀█ █')
            print(Style.BRIGHT + '█▄█ █▀▄ █▀█ █▄▄ █ █▀█ ▄█   █▀▀ █▄█ █▀▄   █▄█ █▄█ █▄█ █▀█ █▀▄ ▄')
            print()
            print(Style.BRIGHT +'© Juego hecho por Juan Marco Giordano. ©')
    except ValueError:
        print('Dato inválido.')
        print('Intente nuevamente: ')
                       
    else:
        break
