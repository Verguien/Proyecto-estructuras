import turtle as tt
import random
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
colores_raquetas = ["white", "white", "white", "white"]  # Colores de las raquetas


# Función para crear raquetas
def crear_raquetas():
    global raqueta_1, raqueta_2, raqueta_3, raqueta_4

    # Raqueta 1 (izquierda)
    raqueta_1 = tt.Turtle()
    raqueta_1.speed(0)
    raqueta_1.shape("square")
    raqueta_1.shapesize(stretch_wid=5, stretch_len=1)
    raqueta_1.color(colores_raquetas[0])
    raqueta_1.penup()
    raqueta_1.goto(-((ancho / 2) - 50), 0)

    # Raqueta 2 (derecha)
    raqueta_2 = tt.Turtle()
    raqueta_2.speed(0)
    raqueta_2.shape("square")
    raqueta_2.shapesize(stretch_wid=5, stretch_len=1)
    raqueta_2.color(colores_raquetas[1])
    raqueta_2.penup()
    raqueta_2.goto(((ancho / 2) - 50), 0)

    # Raquetas 3 y 4 (solo si hay 4 jugadores)
    if jugadores == 4:
        # Raqueta 3 (arriba)
        raqueta_3 = tt.Turtle()
        raqueta_3.speed(0)
        raqueta_3.shape("square")
        raqueta_3.shapesize(stretch_wid=1, stretch_len=5)
        raqueta_3.color(colores_raquetas[2])
        raqueta_3.penup()
        raqueta_3.goto(0, ((alto / 2) - 50))

        # Raqueta 4 (abajo)
        raqueta_4 = tt.Turtle()
        raqueta_4.speed(0)
        raqueta_4.shape("square")
        raqueta_4.shapesize(stretch_wid=1, stretch_len=5)
        raqueta_4.color(colores_raquetas[3])
        raqueta_4.penup()
        raqueta_4.goto(0, -((alto / 2) - 50))


# Función para crear la pelota
def crear_pelota():
    pelota = tt.Turtle()
    pelota.speed(0)
    pelota.shape("square")
    pelota.color("white")
    pelota.penup()
    pelota.goto(0, 0)
    pelota_dx = random.choice([-2, 2])
    pelota_dy = random.choice([-2, 2])
    return pelota, pelota_dx, pelota_dy


# Función para mostrar el menú de selección de jugadores
def mostrar_menu():
    global jugadores
    menu = tt.Turtle()
    menu.speed(0)
    menu.color("white")
    menu.penup()
    menu.hideturtle()
    menu.goto(0, 100)
    menu.write("Bienvenido a Pong", align="center", font=("Comic Sans MS", 24, "bold"))

    menu.goto(0, 50)
    menu.write("Selecciona el número de jugadores:", align="center", font=("Comic Sans MS", 18))
    menu.goto(0, 0)
    menu.write("1) 2 Jugadores (Presiona 1)", align="center", font=("Comic Sans MS", 18))
    menu.goto(0, -50)
    menu.write("2) 4 Jugadores (Presiona 2)", align="center", font=("Comic Sans MS", 18))

    def seleccion_2():
        global jugadores
        jugadores = 2
        menu.clear()
        mostrar_colores()

    def seleccion_4():
        global jugadores
        jugadores = 4
        menu.clear()
        mostrar_colores()

    ventana.onkeypress(seleccion_2, "1")
    ventana.onkeypress(seleccion_4, "2")
    ventana.listen()


# Función para mostrar las instrucciones de las teclas
def mostrar_instrucciones():
    instrucciones = tt.Turtle()
    instrucciones.speed(0)
    instrucciones.color("white")
    instrucciones.penup()
    instrucciones.hideturtle()
    instrucciones.goto(0, 100)
    instrucciones.write("Controles del Juego", align="center", font=("Comic Sans MS", 24, "bold"))

    instrucciones.goto(0, 50)
    instrucciones.write("Jugador 1 (Izquierda): W (Arriba), S (Abajo)", align="center", font=("Comic Sans MS", 16))

    instrucciones.goto(0, 20)
    instrucciones.write("Jugador 2 (Derecha): Flecha Arriba, Flecha Abajo", align="center", font=("Comic Sans MS", 16))

    if jugadores == 4:
        instrucciones.goto(0, -10)
        instrucciones.write("Jugador 3 (Arriba): V (Izquierda), K (Derecha)", align="center", font=("Comic Sans MS", 16))

        instrucciones.goto(0, -40)
        instrucciones.write("Jugador 4 (Abajo): 4 (Izquierda), 5 (Derecha)", align="center", font=("Comic Sans MS", 16))

    instrucciones.goto(0, -80)
    instrucciones.write("Presiona ESPACIO para comenzar...", align="center", font=("Comic Sans MS", 16))

    # Esperar una tecla para iniciar el juego
    def iniciar():
        instrucciones.clear()
        iniciar_juego()

    ventana.listen()
    ventana.onkeypress(iniciar, "space")


# Función para mostrar el menú de selección de colores
def mostrar_colores():
    color_menu = tt.Turtle()
    color_menu.speed(0)
    color_menu.color("white")
    color_menu.penup()
    color_menu.hideturtle()
    color_menu.goto(0, 100)
    color_menu.write("Elige los colores de las raquetas", align="center", font=("Comic Sans MS", 24, "bold"))

    def elegir_color_raqueta_1():
        global colores_raquetas
        colores_raquetas[0] = "red"
        color_menu.clear()
        mostrar_instrucciones()

    def elegir_color_raqueta_2():
        global colores_raquetas
        colores_raquetas[1] = "blue"
        color_menu.clear()
        mostrar_instrucciones()

    def elegir_color_raqueta_3():
        global colores_raquetas
        colores_raquetas[2] = "green"
        color_menu.clear()
        mostrar_instrucciones()

    def elegir_color_raqueta_4():
        global colores_raquetas
        colores_raquetas[3] = "yellow"
        color_menu.clear()
        mostrar_instrucciones()

    # Se pueden agregar más colores si se desea
    color_menu.goto(0, 50)
    color_menu.write("1) Rojo para Jugador 1", align="center", font=("Comic Sans MS", 16))
    color_menu.goto(0, 20)
    color_menu.write("2) Azul para Jugador 2", align="center", font=("Comic Sans MS", 16))
    if jugadores == 4:
        color_menu.goto(0, -10)
        color_menu.write("3) Verde para Jugador 3", align="center", font=("Comic Sans MS", 16))
        color_menu.goto(0, -40)
        color_menu.write("4) Amarillo para Jugador 4", align="center", font=("Comic Sans MS", 16))

    ventana.listen()
    ventana.onkeypress(elegir_color_raqueta_1, "1")
    ventana.onkeypress(elegir_color_raqueta_2, "2")
    if jugadores == 4:
        ventana.onkeypress(elegir_color_raqueta_3, "3")
        ventana.onkeypress(elegir_color_raqueta_4, "4")

    # Esperar que el jugador elija los colores
    color_menu.goto(0, -80)
    color_menu.write("Presiona la tecla para elegir el color de las raquetas...", align="center", font=("Comic Sans MS", 16))


# Función para iniciar el juego
def iniciar_juego():
    crear_raquetas()
    pelota, pelota_dx, pelota_dy = crear_pelota()

    marcador = tt.Turtle()
    marcador.speed(0)
    marcador.color("white")
    marcador.penup()
    marcador.hideturtle()
    marcador.goto(0, (alto / 2) - 30)
    marcador.write("Jugador 1: 0      Jugador 2: 0", align="center", font=("Comic Sans MS", 18, "bold"))

    puntaje_j1 = 0
    puntaje_j2 = 0
    puntaje_j3 = 0
    puntaje_j4 = 0

    # Funciones de movimiento
    def raqueta_1_arriba():
        y = raqueta_1.ycor()
        if y < ((alto / 2) - 50):
            raqueta_1.sety(y + 20)

    def raqueta_1_abajo():
        y = raqueta_1.ycor()
        if y > -((alto / 2) - 50):
            raqueta_1.sety(y - 20)

    def raqueta_2_arriba():
        y = raqueta_2.ycor()
        if y < ((alto / 2) - 50):
            raqueta_2.sety(y + 20)

    def raqueta_2_abajo():
        y = raqueta_2.ycor()
        if y > -((alto / 2) - 50):
            raqueta_2.sety(y - 20)

    def raqueta_3_izquierda():
        x = raqueta_3.xcor()
        if x > -((ancho / 2) - 50):
            raqueta_3.setx(x - 20)

    def raqueta_3_derecha():
        x = raqueta_3.xcor()
        if x < ((ancho / 2) - 50):
            raqueta_3.setx(x + 20)

    def raqueta_4_izquierda():
        x = raqueta_4.xcor()
        if x > -((ancho / 2) - 50):
            raqueta_4.setx(x - 20)

    def raqueta_4_derecha():
        x = raqueta_4.xcor()
        if x < ((ancho / 2) - 50):
            raqueta_4.setx(x + 20)

    ventana.listen()
    ventana.onkeypress(raqueta_1_arriba, "w")
    ventana.onkeypress(raqueta_1_abajo, "s")
    ventana.onkeypress(raqueta_2_arriba, "Up")
    ventana.onkeypress(raqueta_2_abajo, "Down")
    if jugadores == 4:
        ventana.onkeypress(raqueta_3_izquierda, "v")
        ventana.onkeypress(raqueta_3_derecha, "k")
        ventana.onkeypress(raqueta_4_izquierda, "4")
        ventana.onkeypress(raqueta_4_derecha, "5")

    while True:
        pelota.setx(pelota.xcor() + pelota_dx)
        pelota.sety(pelota.ycor() + pelota_dy)

        if pelota.ycor() > (alto / 2) - 10 or pelota.ycor() < -(alto / 2) + 10:
            pelota_dy *= -1

        if (pelota.xcor() > raqueta_2.xcor() - 10 and pelota.xcor() < raqueta_2.xcor() + 10 and
                pelota.ycor() < raqueta_2.ycor() + 50 and pelota.ycor() > raqueta_2.ycor() - 50):
            pelota_dx *= -1

        if (pelota.xcor() < raqueta_1.xcor() + 10 and pelota.xcor() > raqueta_1.xcor() - 10 and
                pelota.ycor() < raqueta_1.ycor() + 50 and pelota.ycor() > raqueta_1.ycor() - 50):
            pelota_dx *= -1

        if jugadores == 4:
            if (pelota.xcor() > raqueta_4.xcor() - 50 and pelota.xcor() < raqueta_4.xcor() + 50 and
                    pelota.ycor() < raqueta_4.ycor() + 10 and pelota.ycor() > raqueta_4.ycor() - 10):
                pelota_dy *= -1

            if (pelota.xcor() > raqueta_3.xcor() - 50 and pelota.xcor() < raqueta_3.xcor() + 50 and
                    pelota.ycor() < raqueta_3.ycor() + 10 and pelota.ycor() > raqueta_3.ycor() - 10):
                pelota_dy *= -1

        if pelota.xcor() > (ancho / 2) - 10:
            pelota.goto(0, 0)
            pelota_dx = random.choice([-2, 2])
            pelota_dy = random.choice([-2, 2])
            puntaje_j1 += 1
            marcador.clear()
            marcador.write("Jugador 1: {}      Jugador 2: {}".format(puntaje_j1, puntaje_j2), align="center", font=("Comic Sans MS", 18, "bold"))

        if pelota.xcor() < -(ancho / 2) + 10:
            pelota.goto(0, 0)
            pelota_dx = random.choice([-2, 2])
            pelota_dy = random.choice([-2, 2])
            puntaje_j2 += 1
            marcador.clear()
            marcador.write("Jugador 1: {}      Jugador 2: {}".format(puntaje_j1, puntaje_j2), align="center", font=("Comic Sans MS", 18, "bold"))

        ventana.update()
        time.sleep(0.005)


# Mostrar el menú inicial
mostrar_menu()
ventana.mainloop()
