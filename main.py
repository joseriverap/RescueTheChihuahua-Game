#Proyecto de José Tomás Rivera Pérez
#Version de Python utilizada: 3.11.3
#Librerias utilizadas: turtle, random, math


#Importacion de librerias
import turtle
import funciones

#Propiedades de la ventana
screen = turtle.Screen()
screen.setup(1200, 700)
turtle.title("Operación Rescue the Chihuahua")
screen.bgpic('img/fondo.png')

#Posicion en eje x de arboles
posarbol1 = [100, -271]
posarbol2 = [300, -271]
posarbol3 = [500, -271]



funciones.linea_mundo()
#Guarda las alturas de los arboles
alturas = funciones.dibujar_arbol(posarbol1, posarbol2, posarbol3)
funciones.lanzamiento_flecha(alturas, posarbol1, posarbol2, posarbol3, screen)


turtle.done()
