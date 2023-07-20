import turtle
import random
import math

#Se registran las imagenes a utilizar en el programa
turtle.register_shape("img/chihuahuaaguila.gif")
turtle.register_shape("img/perro.gif")
turtle.register_shape("img/persona.gif")
aguila = turtle.Turtle()
personaje = turtle.Turtle()
personaje.shape("img/persona.gif")
personaje.penup()
personaje.hideturtle()
personaje.setpos(-400,-175)
aguila.shape("img/chihuahuaaguila.gif")
aguila.hideturtle()
perro = turtle.Turtle()
perro.hideturtle()


#Dibuja una linea para marcar el suelo del juego
def linea_mundo():
    turtle.speed(800)
    turtle.penup()
    turtle.goto(-600, -270)
    turtle.pendown()
    turtle.goto(600, -270)


#Dibuja los arboles en las posiciones dadas en el archivo main.py
def dibujar_arbol(posarbol1, posarbol2, posarbol3):
    altura = random.randint(200, 450)
    altura2 = random.randint(200, 450)
    altura3 = random.randint(200, 450)

    personaje.showturtle()
    turtle.speed(800)
    turtle.hideturtle()

    # Posicion arbol 1

    turtle.penup()
    turtle.goto(posarbol1)
    turtle.left(90)
    turtle.pensize(6)
    turtle.pencolor("#643800")
    turtle.pendown()
    turtle.forward(altura)
    turtle.pensize(4)
    turtle.pencolor("black")
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.right(150)
    for _ in range(3):
        turtle.forward(altura/3)
        turtle.right(120)

    turtle.end_fill()
    turtle.penup()
    turtle.right(30)
    turtle.forward(altura/3.5)
    turtle.right(180)
    turtle.pendown()
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.right(150)
    for _ in range(3):
        turtle.forward(altura/3)
        turtle.right(120)
    turtle.end_fill()
    turtle.penup()
    turtle.right(30)
    turtle.forward(altura/3.5)
    turtle.right(180)
    turtle.pendown()
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.right(150)
    for _ in range(3):
        turtle.forward(altura/3)
        turtle.right(120)
    turtle.end_fill()
    turtle.right(30)
    turtle.left(90)

    # Posicion arbol 2

    turtle.penup()
    turtle.goto(posarbol2)
    turtle.pendown()
    turtle.left(90)
    turtle.pensize(6)
    turtle.pencolor("#643800")
    turtle.pendown()
    turtle.forward(altura2)
    turtle.pensize(4)
    turtle.pencolor("black")
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.right(150)
    for _ in range(3):
        turtle.forward(altura2/3)
        turtle.right(120)

    turtle.end_fill()
    turtle.penup()
    turtle.right(30)
    turtle.forward(altura2/3.5)
    turtle.right(180)
    turtle.pendown()
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.right(150)
    for _ in range(3):
        turtle.forward(altura2/3)
        turtle.right(120)
    turtle.end_fill()
    turtle.penup()
    turtle.right(30)
    turtle.forward(altura2/3.5)
    turtle.right(180)
    turtle.pendown()
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.right(150)
    for _ in range(3):
        turtle.forward(altura2/3)
        turtle.right(120)
    turtle.end_fill()
    turtle.right(30)
    turtle.left(90)

    # Posicion arbol 3

    turtle.penup()
    turtle.goto(posarbol3)
    turtle.left(90)
    turtle.pensize(6)
    turtle.pencolor("#643800")
    turtle.pendown()
    turtle.forward(altura3)
    turtle.pensize(4)
    turtle.pencolor("black")
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.right(150)
    for _ in range(3):
        turtle.forward(altura3/3)
        turtle.right(120)

    turtle.end_fill()
    turtle.penup()
    turtle.right(30)
    turtle.forward(altura3/3.5)
    turtle.right(180)
    turtle.pendown()
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.right(150)
    for _ in range(3):
        turtle.forward(altura3/3)
        turtle.right(120)
    turtle.end_fill()
    turtle.penup()
    turtle.right(30)
    turtle.forward(altura3/3.5)
    turtle.right(180)
    turtle.pendown()
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.right(150)
    for _ in range(3):
        turtle.forward(altura3/3)
        turtle.right(120)
    turtle.end_fill()
    turtle.right(30)
    turtle.left(90)

    #Retorna las alturas de los arboles, las cuales seran ocupadas en la funcion lanzamiento flecha
    return altura, altura2, altura3


#Ingreso de valores
def ingreso_valores():
     velocidad_inicial = int(input("Ingrese la velocidad de la flecha: "))
     angulo_inicial = int(input("Ingrese el angulo de la flecha: "))
     
     return velocidad_inicial,angulo_inicial

#Transformacion de grados a radianes
def radianes(v_inicial):
            resultado = v_inicial * math.pi / 180
            return resultado


def lanzamiento_flecha(alturas, posarbol1, posarbol2, posarbol3, screen):
    i = 1
    #Se definen los intentos se manera aleatoria
    intentos = random.randint(3, 5)

    print(f"Rescata a hector!!!\nTienes {intentos} intentos.")

    #Mientras i sea menor a la cantidad de intentos se ejecutara el movimiento de la flecha
    while i <= intentos:
        # xaguila = 0 indica que el aguila va a estar entre el primer y segundo arbol; 1 indica que el aguila va a estar entre el segundo y tercer arbol
        # yaguila = indica a que altura va a estar el aguila
        xaguila = random.randint(0, 1)
        yaguila = random.randint(-200, 200)

        aguila.speed(1)
        aguila.penup()
       
        #Si xaguila == 0 el aguila estara entre el primer y segundo arbol
        if xaguila == 0:
            aguila.goto(200, yaguila)
        #Si xaguila == 0 el aguila estara entre el segundo y tercer
        elif xaguila == 1:
            aguila.goto(400, yaguila)

        aguila.showturtle()

        posicion_aguila = aguila.pos()

        #Creacion de "caja" de aguila (Desde donde se va a detectar el aguila)
        #Estos son 4 puntos imaginarios los cuales van a determinar en que rango de posiciones se va a detectar el aguila
        px1aguila = posicion_aguila[0] - 60
        px2aguila = posicion_aguila[0] + 60
        py1aguila = posicion_aguila[1] - 60
        py2aguila = posicion_aguila[1] + 60

        print(f"Intento numero {i}: ")

        valores = ingreso_valores()

        
        #Se calcula la velocidad del eje x e y con la formula dada en el pdf del proyecto
        velocidad_x = valores[0] * math.cos(radianes(valores[1]))
        velocidad_y = valores[0] * math.sin(radianes(valores[1]))

        # Creación de la flecha
        flecha = turtle.Turtle()
        flecha.hideturtle()
        flecha.speed(1)
        flecha.shape("arrow")
        flecha.color("white")
        flecha.pen(2)
        flecha.penup()
        flecha.goto(-350, -130)
        flecha.pendown()
        flecha.showturtle()
        linea_base = [0, -250]

        da = 0.3
        posicion = flecha.position()
        #Mientras la flecha este dentro de la pantalla se ejecutara el programa
        #Tanto el ancho como el alto del juego se dividio en 2 ya que esta libreria funciona como un plano carteciano. Es decir que al ancho ser 700, habra -350 posiciones a la izquierda y 350 posiciones a la derecha
        while screen.window_width() / 2 > posicion[0] > -screen.window_width() / 2 and posicion[1] - 10 < screen.window_height() / 2 and posicion[1] > linea_base[1]:

            #Calculo de la nueva posicion x e y de la flecha
            nueva_x = posicion[0] + velocidad_x * da
            nueva_y = posicion[1] + velocidad_y * da - 0.5 * 9.81 * da ** 2

            velocidad_y -= 9.81 * da
            posicion = [nueva_x, nueva_y]


            #Creacion de caja de registro de los 3 arboles en la posicion x
            #Servira para determinar cuando la flecha esta tocando un arbol
            rangoa1_1 = posarbol1[0] - 20
            rangoa1_2 = posarbol1[0] + 20
            rangoa2_1 = posarbol2[0] - 20
            rangoa2_2 = posarbol2[0] + 20
            rangoa3_1 = posarbol3[0] - 20
            rangoa3_2 = posarbol3[0] + 20

            # Si la posibilidad es 1 entonces la flecha va a saguir el trayecto
            # Si la posibilidad es 0 entonces la flecha se quedara pegada en el arbol

            #Posibilidad de que la flecha traspase el arbol 1
            posibilidad = random.randint(0, 1)
            #Posibilidad de que la flecha traspase el arbol 2
            posibilidad2 = random.randint(0, 1)
            #Posibilidad de que la flecha traspase el arbol 3
            posibilidad3 = random.randint(0, 1)


            #Los siguientes condicionales evaluan las posiciones y determinan si la flecha seguira su camino
            if posicion[0] >= rangoa1_1 and posicion[0] <= rangoa1_2:
                if posicion[1] >= -271 + alturas[0]:
                    flecha.goto(nueva_x, nueva_y)
                elif posicion[1] < -271 + alturas[0] and posibilidad == 1:
                    flecha.goto(nueva_x, nueva_y)
                else:
                    break
            #Verifica si la flecha chocara con el aguila
            elif posicion[0] >= px1aguila and posicion[0] <= px2aguila:
                if posicion[1] > py1aguila and posicion[1] <= py2aguila:
                    #Cuando la flecha impacte con el aguila se creara una imagen del perro y una del aguila de forma independiente

                    posperro = aguila.pos()
                    flecha.hideturtle()
                    turtle.register_shape("img/aguila.gif")
                    perro.speed(1)
                    aguila.speed(1)
                    perro.penup()
                    perro.shape("img/perro.gif")
                    aguila.shape("img/aguila.gif")
                    perro.goto(posperro[0], posperro[1])
                    perro.showturtle()
                    perro.goto(posperro[0], -242)
                    aguila.goto(-100, 500)
                    perro.goto(-350, -242)

                    i = intentos
                    break
            #Verifica si la flecha chocara con el segundo arbol
            elif posicion[0] > rangoa2_1 and posicion[0] <= rangoa2_2:
                if posicion[1] >= -271 + alturas[1]:
                    flecha.goto(nueva_x, nueva_y)
                elif posicion[1] < -271 + alturas[1] and posibilidad2 == 1:
                    flecha.goto(nueva_x, nueva_y)
                else:
                    break
            #Verifica si la flecha chocara con el tercer arbol
            elif posicion[0] > rangoa3_1 and posicion[0] <= rangoa3_2:
                if posicion[1] >= -271 + alturas[2]:
                    flecha.goto(nueva_x, nueva_y)
                elif posicion[1] < -271 + alturas[2] and posibilidad3 == 1:
                    flecha.goto(nueva_x, nueva_y)
                else:
                    break
            else:
                flecha.goto(nueva_x, nueva_y)
        
        #Se limpia el trazo de la flecha e inicia un nuevo intento
        flecha.clear()
        i += 1


    #Si el perro llega con su dueño(o a la posicion x = -350) se mostrara en pantalla: "Has rescatado a Héctor!!!"
    
    if perro.xcor() == -350:
        aguila.shape("classic")
        aguila.hideturtle()
        aguila.goto(0,250)
        aguila.color("white")
        aguila.write("Salvaste a Héctor!!!", align="center", font=("Arial",40, "bold"))
    
    #Si no se mostrara en pantalla: "Fuiste bueno Héctor"
    else:
        aguila.goto(-100,500)
        aguila.shape("classic")
        aguila.hideturtle()
        aguila.goto(0,250)
        aguila.color("white")
        aguila.write("Fuiste bueno Héctor", align="center", font=("Arial",40, "bold"))
    
    print("Juego Terminado.")