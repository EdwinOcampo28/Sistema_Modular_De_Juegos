import os
import random
import time

# ============================================================
#                  COLORES (ESTILO HACKER)
# ============================================================
RESET = "\033[0m"
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
MAGENTA = "\033[95m"
BLUE = "\033[94m"
BOLD = "\033[1m"
COLORES = [GREEN, CYAN, YELLOW, RED, MAGENTA, BLUE]

# ============================================================
#                  UTILIDADES
# ============================================================
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def pause():
    input(YELLOW + "\n▶ Presione ENTER para continuar..." + RESET)

def colorear_texto(texto):
    return "".join(random.choice(COLORES) + c + RESET for c in texto)

# ============================================================
#                  RANKING
# ============================================================
def ranking_file(juego):
    return f"ranking_{juego.replace(' ', '_')}.txt"

def cargar_ranking(juego):
    ranking = []
    archivo = ranking_file(juego)
    if os.path.exists(archivo):
        with open(archivo, "r") as f:
            for line in f:
                name, score = line.strip().split(",")
                ranking.append((name, int(score)))
    return ranking

def guardar_ranking(juego, nombre, puntaje):
    ranking = cargar_ranking(juego)
    ranking.append((nombre, puntaje))
    ranking.sort(key=lambda x: x[1], reverse=True)
    ranking = ranking[:5]  # top 5
    with open(ranking_file(juego), "w") as f:
        for name, score in ranking:
            f.write(f"{name},{score}\n")

def mostrar_ranking(juego):
    ranking = cargar_ranking(juego)
    print(GREEN + BOLD + f"\n╔════ RANKING TOP 5: {juego} ═══╗" + RESET)
    if ranking:
        for i, (name, score) in enumerate(ranking, start=1):
            print(CYAN + f"           {i}. {name} - {score} puntos" + RESET)
    else:
        print(YELLOW + "No hay registros todavía." + RESET)
    print(GREEN + "╚══════════════════════════════════════╝" + RESET)

# ============================================================
#                  NOMBRE
# ============================================================
def solicitar_nombre():
    while True:
        nombre = input(CYAN + "Ingresa tu nombre para el ranking: " + RESET).strip()
        if nombre.replace(" ", "").isalpha():
            return nombre
        else:
            print(RED + "El nombre solo debe contener letras." + RESET)

# ============================================================
#                  JUEGOS
# ============================================================
def JuegoAdivinaNumero():
    clear()
    mostrar_ranking("Adivina Número")
    print(YELLOW + BOLD + "╔══════════════════════════════════════╗" + RESET)
    print(YELLOW + BOLD + "║        Juego: Adivina el Número      ║" + RESET)
    print(YELLOW + BOLD + "╚══════════════════════════════════════╝" + RESET)

    nombre = solicitar_nombre()
    numero_secreto = random.randint(1,50)
    intentos = 10
    aciertos = 0

    while intentos > 0:
        try:
            adivina = int(input(CYAN + f"Tienes {intentos} intentos. Ingresa tu número: " + RESET))
        except:
            print(RED + "Entrada inválida." + RESET)
            continue

        if adivina == numero_secreto:
            print(GREEN + "🎉 ¡Felicidades! Adivinaste el número." + RESET)
            aciertos = intentos  # Puntaje basado en intentos restantes
            break
        elif abs(adivina - numero_secreto) <= 5:
            if adivina < numero_secreto:
                print(CYAN + "⚠️ Muy cerca, sube un poco." + RESET)
            else:
                print(CYAN + "⚠️ Muy cerca, baja un poco." + RESET)
        else:
            if adivina < numero_secreto:
                print(YELLOW + "🔺 Muy bajo." + RESET)
            else:
                print(RED + "🔻 Muy alto." + RESET)

        intentos -= 1

    if intentos == 0:
        print(RED + f"💀 Se acabaron los intentos. El número era {numero_secreto}." + RESET)

    if aciertos > 0:
        guardar_ranking("Adivina Número", nombre, aciertos)
    mostrar_ranking("Adivina Número")
    pause()

def JuegoPiedraPapelTijera():
    clear()
    print(GREEN + BOLD + "╔══════════════════════════════════════╗" + RESET)
    print(GREEN + BOLD + "║      Juego: Piedra Papel Tijera      ║" + RESET)
    print(GREEN + BOLD + "╚══════════════════════════════════════╝" + RESET)

    opciones = {"1":"piedra","2":"papel","3":"tijera"}
    jugador = input(CYAN + "Elige 1 Piedra 2 Papel  3 Tijera " + RESET)
    while jugador not in opciones:
        jugador = input(RED + "Opción inválida. Elige 1, 2 o 3: " + RESET)
    jugador = opciones[jugador]

    maquina = random.choice(list(opciones.values()))
    print(YELLOW + f"Computadora eligió: {maquina}" + RESET)
    if jugador == maquina:
        print(YELLOW + "Empate!" + RESET)
    elif (jugador == "piedra" and maquina == "tijera") or \
         (jugador == "papel" and maquina == "piedra") or \
         (jugador == "tijera" and maquina == "papel"):
        print(GREEN + "¡Ganaste!" + RESET)
    else:
        print(RED + "Perdiste." + RESET)
    pause()

def JuegoDados():
    clear()
    print(GREEN + BOLD + "╔══════════════════════════════════════╗" + RESET)
    print(GREEN + BOLD + "║        Juego: Adivina el Dado        ║" + RESET)
    print(GREEN + BOLD + "╚══════════════════════════════════════╝" + RESET)

    dado = random.randint(1,6)
    try:
        adivina = int(input(CYAN + "Adivina el número del dado (1-6): " + RESET))
    except:
        adivina = 0

    print(YELLOW + f"Número del dado: {dado}" + RESET)
    if adivina == dado:
        print(GREEN + "¡Acertaste!" + RESET)
    else:
        print(RED + "No acertaste." + RESET)
    pause()

def JuegoMemoria():
    clear()
    juego = "Memoria"
    mostrar_ranking(juego)

    print(GREEN + BOLD + "╔══════════════════════════════════════╗" + RESET)
    print(GREEN + BOLD + "║     Juego de Memoria PRO             ║" + RESET)
    print(GREEN + BOLD + "╚══════════════════════════════════════╝" + RESET)

    nombre = solicitar_nombre()

    nivel = 1
    vidas = 3
    mensajes = [
        "🔥 Vas excelente",
        "💪 Sigue así",
        "🧠 Memoria en modo PRO",
        "👑 Nivel experto",
        "⚡ Brutal!"
    ]

    while vidas > 0:
        clear()
        print(BOLD + CYAN + f"Nivel: {nivel} 🔥" + RESET)
        print(RED + f"Vidas: {'♥ ' * vidas}" + RESET)
        print(YELLOW + random.choice(mensajes) + RESET)
        print(GREEN + "-" * 40 + RESET)

        longitud = 3 + nivel  # dificultad progresiva
        secuencia = [random.randint(0, 9) for _ in range(longitud)]

        print(CYAN + "Recuerda esta secuencia:" + RESET)
        print(colorear_texto(" ".join(map(str, secuencia))))
        pause()

        clear()
        respuesta = input(CYAN + "Ingresa la secuencia separada por espacios: " + RESET)
        respuesta_lista = [int(x) for x in respuesta.split() if x.isdigit()]

        if respuesta_lista == secuencia:
            print(GREEN + "🎉 ¡Correcto!" + RESET)
            nivel += 1

            if nivel % 3 == 0:
                vidas += 1
                print(BLUE + "🎁 BONUS: ¡Ganaste una vida extra!" + RESET)

        else:
            vidas -= 1
            print(RED + "❌ Incorrecto." + RESET)
            print(YELLOW + f"La secuencia era: {secuencia}" + RESET)

        pause()

    puntaje = nivel + vidas
    print(RED + "💀 Juego terminado" + RESET)
    print(GREEN + f"Nivel alcanzado: {nivel}" + RESET)
    print(GREEN + f"Puntaje final: {puntaje}" + RESET)

    guardar_ranking(juego, nombre, puntaje)
    mostrar_ranking(juego)
    pause()



# ============================================================
#                  NUEVOS JUEGOS (DIFICULTAD PROGRESIVA)
# ============================================================
def JuegoMatematicaRapida():
    clear()
    mostrar_ranking("Matematica Rapida")
    print(GREEN + BOLD + "╔══════════════════════════════════════╗" + RESET)
    print(GREEN + BOLD + "║       Juego: Matemática Rápida       ║" + RESET)
    print(GREEN + BOLD + "╚══════════════════════════════════════╝" + RESET)

    nombre = solicitar_nombre()
    aciertos = 0
    nivel = 1
    rango = 50
    while True:
        a, b = random.randint(1, rango), random.randint(1, rango)
        try:
            r = int(input(CYAN + f"Nivel {nivel} - Resuelve: {a} + {b} = " + RESET))
        except:
            print(RED + "Entrada inválida." + RESET)
            continue
        if r == a + b:
            aciertos += 1
            nivel += 1
            rango += 10
            print(GREEN + f"¡Correcto! Llevas {aciertos} aciertos seguidos." + RESET)
        else:
            print(RED + f"Incorrecto. La respuesta correcta era {a + b}." + RESET)
            break

    guardar_ranking("Matematica Rapida", nombre, aciertos)
    mostrar_ranking("Matematica Rapida")
    pause()

def JuegoAdivinaProducto():
    clear()
    mostrar_ranking("Adivina Producto")
    print(GREEN + BOLD + "╔══════════════════════════════════════╗" + RESET)
    print(GREEN + BOLD + "║        Juego: Adivina el Producto    ║" + RESET)
    print(GREEN + BOLD + "╚══════════════════════════════════════╝" + RESET)

    nombre = solicitar_nombre()
    aciertos = 0
    nivel = 1
    rango = 12
    while True:
        a, b = random.randint(1, rango), random.randint(1, rango)
        try:
            r = int(input(CYAN + f"Nivel {nivel} - Resuelve: {a} x {b} = " + RESET))
        except:
            print(RED + "Entrada inválida." + RESET)
            continue
        if r == a * b:
            aciertos += 1
            nivel += 1
            rango += 2
            print(GREEN + f"¡Correcto! Llevas {aciertos} aciertos seguidos." + RESET)
        else:
            print(RED + f"Incorrecto. La respuesta correcta era {a * b}." + RESET)
            break

    guardar_ranking("Adivina Producto", nombre, aciertos)
    mostrar_ranking("Adivina Producto")
    pause()

def JuegoMayorMenor():
    clear()
    mostrar_ranking("Mayor o Menor")
    print(GREEN + BOLD + "╔══════════════════════════════════════╗" + RESET)
    print(GREEN + BOLD + "║        Juego: Mayor o Menor          ║" + RESET)
    print(GREEN + BOLD + "╚══════════════════════════════════════╝" + RESET)

    nombre = solicitar_nombre()
    anterior = random.randint(1,100)
    aciertos = 0
    while True:
        print(CYAN + f"Número actual: {anterior}" + RESET)
        siguiente = random.randint(1,100)
        eleccion = input(CYAN + "¿El siguiente será Mayor (M) o menor (m)? " + RESET)
        if eleccion not in ["M","m"]:
            print(RED + "Opción inválida." + RESET)
            continue
        print(YELLOW + f"Siguiente número: {siguiente}" + RESET)
        correcto = (eleccion=="M" and siguiente>anterior) or (eleccion=="m" and siguiente<anterior)
        if correcto:
            aciertos += 1
            print(GREEN + f"¡Correcto! Llevas {aciertos} aciertos seguidos." + RESET)
            anterior = siguiente
        else:
            print(RED + "Incorrecto." + RESET)
            break
    guardar_ranking("Mayor o Menor", nombre, aciertos)
    mostrar_ranking("Mayor o Menor")
    pause()

def JuegoAdivinaPalabra():
    clear()
    juego = "Adivina Palabra"
    mostrar_ranking(juego)
    
    print(GREEN + BOLD + "╔══════════════════════════════════════╗" + RESET)
    print(GREEN + BOLD + "║       Juego: Adivina la Palabra      ║" + RESET)
    print(GREEN + BOLD + "╚══════════════════════════════════════╝" + RESET)

    nombre = solicitar_nombre()
    palabras = ["python", "programa", "juego", "ranking", "palabra", "hacker", "computadora"]
    palabra_secreta = random.choice(palabras).lower()
    aciertos = 0
    intentos = 6
    letras_adivinadas = []

    # Pistas
    print(YELLOW + f"Pista: La palabra tiene {len(palabra_secreta)} letras." + RESET)
    print(YELLOW + f"Pista: La primera letra es '{palabra_secreta[0]}'." + RESET)

    while intentos > 0:
        mostrar = "".join([letra if letra in letras_adivinadas else "_" for letra in palabra_secreta])
        print(colorear_texto(f"\nPalabra: {mostrar}"))
        if "_" not in mostrar:
            print(GREEN + "🎉 ¡Felicidades! Adivinaste la palabra." + RESET)
            aciertos = intentos  # basado en intentos restantes
            break

        letra = input(YELLOW + f"Tienes {intentos} intentos. Ingresa una letra: " + RESET).lower()
        if len(letra) != 1 or not letra.isalpha():
            print(RED + "Entrada inválida. Ingresa solo una letra." + RESET)
            continue

        if letra in letras_adivinadas:
            print(RED + "Ya ingresaste esa letra." + RESET)
            continue

        letras_adivinadas.append(letra)
        if letra not in palabra_secreta:
            intentos -= 1
            print(RED + "Letra incorrecta." + RESET)
        else:
            print(GREEN + "¡Letra correcta!" + RESET)

    if "_" in "".join([l if l in letras_adivinadas else "_" for l in palabra_secreta]):
        print(RED + f"\n💀 Se acabaron los intentos. La palabra era: {palabra_secreta}" + RESET)

    guardar_ranking(juego, nombre, aciertos)
    mostrar_ranking(juego)
    pause()

# ============================================================
#                  JUEGO: SERPIENTES MATEMÁTICAS
# ============================================================
def JuegoSerpientesMatematicas():
    clear()
    mostrar_ranking("Serpientes Matemáticas")
    print(GREEN + BOLD + "╔══════════════════════════════════════╗" + RESET)
    print(GREEN + BOLD + "║      Juego: Serpientes Matemáticas   ║" + RESET)
    print(GREEN + BOLD + "╚══════════════════════════════════════╝" + RESET)

    nombre = solicitar_nombre()
    aciertos = 0
    nivel = 1
    operaciones = ["+", "-", "*", "/"]
    while True:
        max_val = 10 * nivel
        a = random.randint(1, max_val)
        b = random.randint(1, max_val)
        op = random.choice(operaciones)

        if op == "/":
            while b == 0 or a % b != 0:
                b = random.randint(1, max_val)

        pregunta = f"{a} {op} {b}"
        if op == "+":
            resultado = a + b
        elif op == "-":
            resultado = a - b
        elif op == "*":
            resultado = a * b
        elif op == "/":
            resultado = a // b

        try:
            respuesta = int(input(CYAN + f"Nivel {nivel} - Resuelve: {pregunta} = " + RESET))
        except:
            print(RED + "Entrada inválida." + RESET)
            continue

        if respuesta == resultado:
            aciertos += 1
            print(GREEN + f"¡Correcto! Llevas {aciertos} aciertos seguidos." + RESET)
            if aciertos % 3 == 0:
                nivel += 1
                print(BLUE + f"🔥 ¡Subiste al nivel {nivel}!" + RESET)
        else:
            print(RED + f"Incorrecto. La respuesta correcta era {resultado}." + RESET)
            break

    guardar_ranking("Serpientes Matemáticas", nombre, aciertos)
    mostrar_ranking("Serpientes Matemáticas")
    pause()


# ============================================================
#                  MENÚ PRINCIPAL
# ============================================================
def main():
    opcion = 0
    while opcion != 12:
        clear()
        print(GREEN + BOLD + "╔══════════════════════════════════════╗" + RESET)
        print(GREEN + BOLD + "║      SISTEMA MODULAR DE JUEGOS       ║" + RESET)
        print(GREEN + BOLD + "╚══════════════════════════════════════╝" + RESET)

        print(CYAN + "\n1. Juego: Adivina Número")
        print("2. Juego: Piedra, Papel o Tijera")
        print("3. Juego: Dados")
        print("4. Juego de Memoria")
        print("5. Juego: Matemática Rápida")
        print("6. Juego: Adivina el Producto")
        print("7. Juego: Mayor o Menor")
        print("8. Juego: Adivina la Palabra")
        print("9. Juego: Serpientes Matemáticas")  # en el menú
        print("10. ❌ SALIR" + RESET)
        print(GREEN + "========================================" + RESET)

        try:
            opcion = int(input(YELLOW + "Seleccione una opción: " + RESET))
        except:
            opcion = 0

        if opcion == 1:
            JuegoAdivinaNumero()
        elif opcion == 2:
            JuegoPiedraPapelTijera()
        elif opcion == 3:
            JuegoDados()
        elif opcion == 4:
            JuegoMemoria()
        elif opcion == 5:
            JuegoMatematicaRapida()
        elif opcion == 6:
            JuegoAdivinaProducto()
        elif opcion == 7:
            JuegoMayorMenor()
        elif opcion == 8:
            JuegoAdivinaPalabra()
        elif opcion == 9:
            JuegoSerpientesMatematicas()
        elif opcion == 10:
            print(GREEN + "Saliendo del sistema..." + RESET)
            time.sleep(2)
            break
        else:
            print(RED + "Opción inválida..." + RESET)
            pause()

if __name__ == "__main__":
    main()