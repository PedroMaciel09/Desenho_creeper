#prova 

import turtle
turtle.speed(11)
turtle.shape("turtle")
turtle.pensize(3)

def cabeca_creeper(pos_x,pos_y,cor,zoom:int=1):
    turtle.penup()
    turtle.goto(pos_x,pos_y)
    turtle.pendown() 

    turtle.fillcolor(cor) 
    turtle.begin_fill()

    for c in range(4):
        turtle.fd(zoom*15)
        turtle.left(90)
    turtle.end_fill()

def olho_esq(pos_x,pos_y,cor,zoom:int=1):
    turtle.penup()
    turtle.goto(pos_x,pos_y)
    turtle.pendown() 

    turtle.fillcolor(cor)
    turtle.begin_fill()

    for o in range(4):
        turtle.fd(zoom*3.5)
        turtle.left(90)

    turtle.end_fill()

def olho_dir(pos_x,pos_y,cor,zoom:int=1):
    turtle.penup()
    turtle.goto(pos_x,pos_y)
    turtle.pendown() 

    turtle.fillcolor(cor)
    turtle.begin_fill()

    for o in range(4):
        turtle.fd(zoom*3.5)
        turtle.left(90)

    turtle.end_fill()

def boca(pos_x,pos_y,cor,zoom:int=1):
    turtle.penup()
    turtle.goto(pos_x,pos_y)
    turtle.pendown() 

    turtle.fillcolor(cor)
    turtle.begin_fill()

    turtle.left(90)
    turtle.fd(zoom*3)
    turtle.right(90)
    turtle.fd(zoom*5.6)
    turtle.right(90)
    turtle.fd(zoom*3)
    turtle.right(90)
    turtle.fd(zoom*1.5)
    turtle.right(90)
    turtle.fd(zoom*1.3)
    turtle.left(90)
    turtle.fd(zoom*2.5)
    turtle.left(90)
    turtle.fd(zoom*1.3)
    turtle.right(90)
    turtle.fd(zoom*1.7)

    turtle.end_fill()

def cartola_creeper(pos_x,pos_y,cor,zoom:int=1):
    turtle.penup()
    turtle.goto(pos_x,pos_y)
    turtle.pendown() 

    turtle.fillcolor(cor)
    turtle.begin_fill()

    turtle.right(90)
    turtle.fd(zoom*2)
    turtle.right(90)
    turtle.fd(zoom*10.5)
    turtle.right(90)
    turtle.fd(zoom*2)
    turtle.goto(-50,130)
    
    #parte de cima da cartola

    turtle.penup()
    turtle.goto(-32,150)
    turtle.pendown()

    turtle.right(180)
    turtle.fd(zoom*5.5)
    turtle.right(90)
    turtle.fd(zoom*6.7)
    turtle.right(90)
    turtle.fd(zoom*5.5)
    turtle.goto(-30,150)

    turtle.end_fill()


def listra_branca_cartola(pos_x,pos_y,cor,zoom:int=1):
    turtle.penup()
    turtle.goto(pos_x,pos_y)
    turtle.pendown() 

    turtle.fillcolor(cor)
    turtle.begin_fill()

    turtle.left(90)
    turtle.fd(zoom*7)
    turtle.right(90)
    turtle.fd(zoom*1)
    turtle.right(90)
    turtle.fd(zoom*6.8)
    turtle.right(90)
    turtle.fd(zoom*1)

    turtle.end_fill()

#aqui, chamaremos as funções criadas definindo seus respectivos argumentos, zoom e positions.
input("Pressione ENTER para iniciar...")
cabeca_creeper(-75,-20,"green",zoom=10)
olho_esq(-45,60,"black",zoom=10)
olho_dir(10,60,"black",zoom=10)
boca(-27,15,"black",zoom=10)
cartola_creeper(-50,130,"black",zoom=10)
listra_branca_cartola(-35,175,"white",zoom=10)

#final

turtle.hideturtle()

turtle.done()
