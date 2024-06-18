import random

# Función para simular el campeonato de tenis
def simular_campeonato(jugadores):
    ronda = 1
    participantes = jugadores[:]  # Hacemos una copia de la lista de jugadores inicial
    
    while len(participantes) > 1:
        print(f"Ronda {ronda}")
        proximos_ganadores = []
        
        # Simular los partidos
        for i in range(0, len(participantes), 2):
            jugador1 = participantes[i]
            jugador2 = participantes[i + 1]
            
            # Simulamos el resultado del partido (ganador aleatorio)
            ganador = random.choice([jugador1, jugador2])
            
            # Mostramos el resultado del partido y guardamos al ganador
            print(f"{jugador1} - {jugador2}: {ganador}")
            proximos_ganadores.append(ganador)
        
        # Los ganadores de esta ronda pasan a la siguiente
        participantes = proximos_ganadores[:]
        ronda += 1
    
    # Al final solo queda un jugador, que es el campeón
    campeon = participantes[0]
    print(f"\nCampeón del torneo: {campeon}")

# Ingresar nombres de los jugadores
jugadores = []
for i in range(1, 9):
    nombre = input(f"Ingrese el nombre del jugador {i}: ")
    jugadores.append(nombre)
    
# Simular el campeonato con los nombres ingresados
simular_campeonato(jugadores)
