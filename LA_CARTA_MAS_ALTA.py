#################################################################################
###### Massachusetts Institute of Technology (MIT) - IES Gran Capitán (GC) ######
#################################################################################

         ##########################################################
         ########           JUEGO CLÁSICO                  ########
         ########         LA CARTA MÁS ALTA                ########
         ##########################################################

#Módulos que emplearemos en todo el programa:
import random
import time
#Creación de dos listas: palos y carta (para obtener una carta con su palo):

palos=['Oros','Copas','Espadas','Bastos']
carta=['Dos','Tres','Cuatro','Cinco','Seis','Siete','Sota','Caballo','Rey','As']

#Texto de Bienvenida:

print ('''          *********************************
          *     LA CARTA MAS ALTA         *
          *********************************''')
print ("¡Bienvenido! al famoso juego \"LA CARTA MÁS ALTA\"") 
print ("¿Cúal es tú nombre?")
jugador = input()
print ("Encantado,",jugador)
print ("Vamos a jugar una partida a cinco rondas. ¡Suerte!")
print("")
time.sleep(2)

#Variables para cada ronda ganadora:
jugador_ronda_ganada=0
cpu_ronda_ganada=0

#Rondas de la partida
ronda=1
while ronda<6:
    print ("RONDA Nº", ronda)
    print ("Barajando las cartas...")
    time.sleep(2)
    jugador_palo=random.randint(0,3) #variable jugador_palo con el palo de la carta
    jugador_carta=random.randint(0,9) #variable jugador_carta con el valor de la carta
    ##### carta[jugador_carta] permite obtener un elemento aleatorio de la lista carta[]
    ##### palos[jugador_palo] permite obtener un elemento aleatorio de la lista palo[]    
    print (jugador,"ha sacado la carta:",carta[jugador_carta],"de",palos[jugador_palo])

    ##### Mismo procedimiento para CPU
    cpu_palo=random.randint(0,3)
    cpu_carta=random.randint(0,9)

    ##### La carta de CPU debe ser distinta que la del jugador
    while cpu_carta==jugador_carta & cpu_palo==jugador_palo:
        cpu_carta=random.randint(0,9)
        cpu_palo=random.randint(0,3)
    print ("CPU ha sacado la carta:",carta[cpu_carta],"de",palos[cpu_palo])

    ##### Comparamos el valor de las cartas para elegir ganador de la ronda
    if jugador_carta>cpu_carta:
        jugador_ronda_ganada = jugador_ronda_ganada + 1
        print(jugador, "gana la ronda")
    if jugador_carta<cpu_carta:
        cpu_ronda_ganada = cpu_ronda_ganada + 1
        print("CPU gana la ronda")
    if jugador_carta==cpu_carta:
        print("Vaya, ha habido empate :)")

    ##### Nueva ronda a la espera de pulsar una tecla
    ronda = ronda+1
    print("pulsa una tecla para continuar...")
    input()

#Resultados finales de la partida:
print("Hemos completado las cinco rondas de esta partida")
print("Estos han sido los resultados obtenidos:")
time.sleep(1)
print("")
print ("*"*33)
print (jugador, "ha obtenido", jugador_ronda_ganada, "rondas ganadas")
print ("*"*33)
print("")
print ("*"*33)
print ("CPU ha obtenido", cpu_ronda_ganada, "rondas ganadas")
print ("*"*33)
print("")
time.sleep(2)
#Ganador de la partida
print("Y EL GANADOR DE LA PARTIDA A LA CARTA MAS ALTA HA SIDO...")
print("")
time.sleep(1)
if jugador_ronda_ganada>cpu_ronda_ganada:
    print("€"*30)
    print(" "*10,jugador)
    print("€"*30)
    print("")
    print("¡Enhorabuena!",jugador)
if jugador_ronda_ganada<cpu_ronda_ganada:
    print("€"*30)
    print("              CPU")
    print("€"*30)
    print("")
    print("Lo siento, quizá la próxima vez tengas más suerte.")
if jugador_ronda_ganada==cpu_ronda_ganada:
    print("€"*30)
    print(" "*10+"¡EMPATE!")
    print("€"*30)
    print("")
    print("Vaya, esto si que es excepcional, ¿no te parece?")
        
print("")
print("En cualquier caso, ha sido un placer jugar contigo")
print("¡Hasta la próxima partida!", jugador)



