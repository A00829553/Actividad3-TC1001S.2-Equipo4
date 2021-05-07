# Nombre: Roberto Miguel Rodriguez Hermann
# Matricula: A00829553
#Reflexion: #Esta actividad me emociono mucho porque pouse en practica las habilidades que consegui durante estos 3 dias. Que a pesar de ser poco tiempo siento que aprendi 
#mucho, pues nunca imagine que podria lograr mejorar la inteligencia de los enemigos con herrmaientas tan básicas. Al fin comprendi mejor el orden en que se llevan a cabo 
#las acciones dentro del código lo que hizo que todo fuera más fácil. Dentro de mi carrera a veces es dificil imaginarte o el movimiento o comportamiento de ciertos fenomenos 
#y creo que con lo que aprendi, en especial hoy, puedo hacer programas para vizualisarlo de una mejor manera y poder explicarlos. Por otro lado ahora siento mas 
#confianza para la actividad final, pues no me sentia capaz de hacer un juego desde 0 y ahora con lo que logre con mi equipo si creo que podemos dar un buen trabajo.

# Nombre: Roberto Miguel Rodriguez Hermann
# Matricula: A00829553
# Reflexion:

# Import de las librerias necesarias
from random import choice
from turtle import *
from freegames import floor, vector

# Score inicial
state = {'score': 0}
# Instancias de Turtle para el score y para el juego
path = Turtle(visible=False)
writer = Turtle(visible=False)

# Direccion y posicion de Pacman
aim = vector(5, 0)
pacman = vector(-40, -80)

# Arreglo de las direcciones y posiciones de los fantasmas
ghosts = [
    [vector(-180, 160), vector(5, 0)],
    [vector(-180, -160), vector(0, 5)],
    [vector(100, 160), vector(0, -5)],
    [vector(100, -160), vector(-5, 0)],
]

# Arreglo del tablero
tiles = [
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]

# Dibuja un cuadrado con las coordenadas de la esquina inferior izquierda
def square(x, y):
    "Draw square using path at (x, y)."
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()


def offset(point):
    "Return offset of point in tiles."
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index
#retorna true si es un tile valido (que no sea una pared) 
def valid(point):
    "Return True if point is valid in tiles."
    index = offset(point)
#si es 0 ternoa flase -pared
    if tiles[index] == 0:
        return False

    index = offset(point + 19)
#si es 0 ternoa flase -pared
    if tiles[index] == 0:
        return False
#checa el valor de X y Y en un punto
    return point.x % 20 == 0 or point.y % 20 == 0
#dibuja el mapa
def world():
    "Draw world using path."
    bgcolor('black')
    path.color('blue')
#checa el valor en la lista del index
    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            #calcula la X Y donde se dibuja el square
            x = (index % 20) * 20 - 200 # si index es (21%20)*20-200=-180
            y = 180 - (index // 20) * 20#180-(21//20)*20=160
            square(x, y)#diuja el square en (-180,160)
# dibuja las galltas sobre el square en el centro de las tiles
            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')

def move():
    #listas de colores para fantasmas
    "Move pacman and all ghosts."
    #listas de colores para fantasmas
    colores = ['red','orange','green','white']
    "Move pacman and all ghosts."
    writer.undo()
    writer.write(state['score'])

    clear()

    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:
        tiles[index] = 2
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)
    dot(20, 'yellow')
    k=0

    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            options = [
                vector(5, 0),
                vector(-5, 0),
                vector(0, 5),
                vector(0, -5),
            ]
            if abs(point.x-pacman.x) > abs(point.y-pacman.y):
              if point.x > pacman.x:
                plan = options[1]
                  
              else:
                plan = options[0]
              if not valid(point + plan):  
                if point.y > pacman.y:
                  plan = options[3]

                else:
                  plan = options[2]

            elif abs(point.x-pacman.x) < abs(point.y-pacman.y):
              if point.y > pacman.y:
                plan = options[3]

              else:
                plan = options[2]
              if not valid(point + plan):  
                if point.x > pacman.x:
                  plan = options[1]
                else:
                  plan = options[0]
            else:
              plan=choice(options)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)
        dot(20, colores[k])
        k=k+1

    update()

    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    ontimer(move, 100)

def change(x, y):
    "Change pacman aim if valid."
    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
writer.goto(160, 160)
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
world()
move()
done()
