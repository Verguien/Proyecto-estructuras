import turtle as tt
import time

# Definición de dimensiones
ancho = 800
alto = 600

# Crear la ventana de Turtle
ventana = tt.Screen()
ventana.title("Pong 4-P")
ventana.bgcolor("black")
ventana.setup(width=ancho, height=alto)
ventana.tracer(0)

# Variables globales
jugadores = 2  # Por defecto, 2 jugadores

# Raquetas y pelota se definen como en tu código actual, las guardaremos en funciones para poder configurarlas dinámicamente.
def crear_raquetas():
    global raqueta_1, raqueta_2, raqueta_3, raqueta_4
    
    # Raqueta 1 (izquierda)
    raqueta_1 = tt.Turtle()
    raqueta_1.speed(0)
    raqueta_1.shape("square")
    raqueta_1.shapesize(stretch_wid=5, stretch_len=1)
    raqueta_1.color("white")
    raqueta_1.penup()
    raqueta_1.goto(-((ancho/2) - 50), 0)

    # Raqueta 2 (derecha)
    raqueta_2 = tt.Turtle()
    raqueta_2.speed(0)
    raqueta_2.shape("square")
    raqueta_2.shapesize(stretch_wid=5, stretch_len=1)
    raqueta_2.color("white")
    raqueta_2.penup()
    raqueta_2.goto(((ancho/2) - 50), 0)

    # Raquetas 3 y 4 (solo si hay 4 jugadores)
    if jugadores == 4:
        # Raqueta 3 (arriba)
        raqueta_3 = tt.Turtle()
        raqueta_3.speed(0)
        raqueta_3.shape("square")
        raqueta_3.shapesize(stretch_wid=1, stretch_len=5)
        raqueta_3.color("white")
        raqueta_3.penup()
        raqueta_3.goto(0, ((alto/2) - 50))

        # Raqueta 4 (abajo)
        raqueta_4 = tt.Turtle()
        raqueta_4.speed(0)
        raqueta_4.shape("square")
        raqueta_4.shapesize(stretch_wid=1, stretch_len=5)
        raqueta_4.color("white")
        raqueta_4.penup()
        raqueta_4.goto(0, -((alto/2) - 50))

def crear_pelota():
    # Pelota (parte del centro)
    pelota = tt.Turtle()
    pelota.speed(0)
    pelota.shape("square")
    pelota.color("white")
    pelota.penup()
    pelota.goto(0, 0)
    pelota_dx = 2
    pelota_dy = 2
    return pelota, pelota_dx, pelota_dy

def mostrar_menu():
    global jugadores

    # Función que dibuja el menú
    menu = tt.Turtle()
    menu.speed(0)
    menu.color("white")
    menu.penup()
    menu.hideturtle()
    menu.goto(0, 100)
    menu.write("Bienvenido a Pong", align="center", font=("Comic Sans MS", 24, "bold"))
    
    menu.goto(0, 50)
    menu.write("Selecciona el numero de jugadores:", align="center", font=("Comic Sans MS", 18))

    menu.goto(0, 0)
    menu.write("1) 2 Jugadores", align="center", font=("Comic Sans MS", 18))

    menu.goto(0, -50)
    menu.write("2) 4 Jugadores", align="center", font=("Comic Sans MS", 18))

    # Función para elegir el número de jugadores
    def seleccion_2():
        global jugadores
        jugadores = 2
        menu.clear()
        iniciar_juego()

    def seleccion_4():
        global jugadores
        jugadores = 4
        menu.clear()
        iniciar_juego()

    ventana.onkeypress(seleccion_2, "1")
    ventana.onkeypress(seleccion_4, "2")
    ventana.listen()

def iniciar_juego():
    # Crear raquetas y pelota según el número de jugadores
    crear_raquetas()
    pelota, pelota_dx, pelota_dy = crear_pelota()

    # Crear marcador principal para jugadores 1 y 2 en el centro de la pantalla
    marcador = tt.Turtle()
    marcador.speed(0)
    marcador.color("white")
    marcador.penup()
    marcador.hideturtle()
    marcador.goto(0, (alto/2) - 30)
    marcador.write("Jugador 1: 0      Jugador 2: 0", align="center", font=("Comic Sans MS", 18, "bold"))

    # Puntajes
    puntaje_j1 = 0
    puntaje_j2 = 0
    puntaje_j3 = 0  # Para el jugador 3
    puntaje_j4 = 0  # Para el jugador 4

    # Funciones de movimiento para las raquetas
    def raqueta_1_arriba():
        y = raqueta_1.ycor()
        if y < ((alto/2) - 50):
            y += 20
            raqueta_1.sety(y)

    def raqueta_2_arriba():
        y = raqueta_2.ycor()
        if y < ((alto/2) - 50):
            y += 20
            raqueta_2.sety(y)

    def raqueta_1_abajo():
        y = raqueta_1.ycor()
        if y > -((alto/2) - 50):
            y -= 20
            raqueta_1.sety(y)

    def raqueta_2_abajo():
        y = raqueta_2.ycor()
        if y > -((alto/2) - 50):
            y -= 20
            raqueta_2.sety(y)

    # Movimiento de las raquetas 3 y 4
    def raqueta_3_izquierda():
        x = raqueta_3.xcor()
        if x > -((ancho/2) - 50):
            x -= 20
            raqueta_3.setx(x)

    def raqueta_3_derecha():
        x = raqueta_3.xcor()
        if x < ((ancho/2) - 50):
            x += 20
            raqueta_3.setx(x)

    def raqueta_4_izquierda():
        x = raqueta_4.xcor()
        if x > -((ancho/2) - 50):
            x -= 20
            raqueta_4.setx(x)

    def raqueta_4_derecha():
        x = raqueta_4.xcor()
        if x < ((ancho/2) - 50):
            x += 20
            raqueta_4.setx(x)

    # Asignaciones de teclado
    ventana.listen()
    ventana.onkeypress(raqueta_1_arriba, "w")
    ventana.onkeypress(raqueta_1_abajo, "s")
    ventana.onkey(raqueta_2_arriba, "Up")
    ventana.onkeypress(raqueta_2_abajo, "Down")

    # Movimiento de las raquetas 3 y 4 con las teclas específicas
    if jugadores == 4:
        ventana.onkeypress(raqueta_3_izquierda, "v")
        ventana.onkeypress(raqueta_3_derecha, "k")
        ventana.onkeypress(raqueta_4_izquierda, "4")
        ventana.onkeypress(raqueta_4_derecha, "5")

    # Bucle principal del juego
    while True:
        # Mover la pelota
        pelota.setx(pelota.xcor() + pelota_dx)
        pelota.sety(pelota.ycor() + pelota_dy)

        # Verificar los límites de la pantalla
        if pelota.ycor() > (alto / 2) - 10:
            pelota_dy *= -1

        if pelota.ycor() < -(alto / 2) + 10:
            pelota_dy *= -1

        # Colisión con las raquetas (jugadores 1 y 2)
        if (pelota.xcor() > raqueta_2.xcor() - 10 and pelota.xcor() < raqueta_2.xcor() + 10 and
            pelota.ycor() < raqueta_2.ycor() + 50 and pelota.ycor() > raqueta_2.ycor() - 50):
            pelota_dx *= -1

        if (pelota.xcor() < raqueta_1.xcor() + 10 and pelota.xcor() > raqueta_1.xcor() - 10 and
            pelota.ycor() < raqueta_1.ycor() + 50 and pelota.ycor() > raqueta_1.ycor() - 50):
            pelota_dx *= -1

        # Colisión con las raquetas 3 y 4 (si hay 4 jugadores)
        if jugadores == 4:
            if (pelota.xcor() > raqueta_4.xcor() - 50 and pelota.xcor() < raqueta_4.xcor() + 50 and
                pelota.ycor() < raqueta_4.ycor() + 10 and pelota.ycor() > raqueta_4.ycor() - 10):
                pelota_dy *= -1

            if (pelota.xcor() > raqueta_3.xcor() - 50 and pelota.xcor() < raqueta_3.xcor() + 50 and
                pelota.ycor() < raqueta_3.ycor() + 10 and pelota.ycor() > raqueta_3.ycor() - 10):
                pelota_dy *= -1

        # Verificar si la pelota pasa de lado (puntuación)
        if pelota.xcor() > (ancho / 2) - 10:
            pelota_dx *= -1
            # Gol para el jugador 1
            puntaje_j1 += 1
            marcador.clear()
            marcador.write("Jugador 1: {}      Jugador 2: {}".format(puntaje_j1, puntaje_j2), align="center", font=("Comic Sans MS", 18, "bold"))

        if pelota.xcor() < -(ancho / 2) + 10:
            pelota_dx *= -1
            # Gol para el jugador 2
            puntaje_j2 += 1
            marcador.clear()
            marcador.write("Jugador 1: {}      Jugador 2: {}".format(puntaje_j1, puntaje_j2), align="center", font=("Comic Sans MS", 18, "bold"))

        # Actualización de la pantalla de turtle
        ventana.update()
        time.sleep(0.01)

# Mostrar el menú inicial
mostrar_menu()
ventana.mainloop()
