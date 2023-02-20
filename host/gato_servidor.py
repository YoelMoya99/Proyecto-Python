#!/usr/bin/python3

'''
*** INICIO DEL ENCABEZADO ***

    Yoel Moya Carmona
    carné: B75262

    Luis Diego Nuñes
    carné: B75473

*** ESTRUCTURA GENERAL DEL CODIGO ***

    Se utilizó tkinter, la cual es una biblioteca de python que genera
    interfaces gráficas. Cabe mencionar que algunas secciónes del uso de
    esta biblioteca no son compatibles con el formato de flake8, por lo
    que se utilizo '# noqa' en los lugares donde no era posible modificar
    la sintaxis.
    Se utilizó la biblioteca sockets para crear una estructura tipo
    servidor-cliente, la cual pretende interactuar con el codigo del juego
    para comunicar información entre las dos maquinas virtuales a traves de
    la misma sub red.
    Se utilizó la biblioteca threading para mantener la comunicación entre
    ambas maquinas virtuales mientras se continua ejecutando el resto del
    codigo.

    FUNCIONES:

    La función servidor determina el 'servidor' al cual se va a conectar la
    maquina virtual. Es nesesario ejecutar este codigo primero para que el
    'cliente' pueda solicitar la conexión.

    La función enviar_data, es utilizada luego de la habilitacion del
    servidor para transmitir información hacia la maquina virtual
    cliente.

    La funcion recibir_sms es utilizada para capturar los mensajes enviados
    desde la otra maquina virtual. En este caso, para capturar los mensajes
    enviados por el cliente.

    Las funciones next_turnXX, donde ambas 'X' representan el valor
    posicional que tienen en una matriz y el numero del boton al cual se
    encuentran relacionadas.

    La función check_winner, pretender revisar con cada turno que pasa
    cada una de las condiciones de gane.

    La funcion empty_spaces, busca llevar cuenta de la cantidad de espacios
    no marcados, para poder proveer información sobre un posible empate a
    la funcion check_winner.

    Y por ultimo, la funcion new_game, devuelve a las caracteristicas
    iniciales a cada uno de los botones, lo que genera una nueva partida.

    EL CODIGO PRINCIPAL:

    Luego de levantar el servidor y esperar la conexion del cliente, se
    inicia la interfas grafica, donde se determinan todas las partes de
    ella, y su funcionamiento.
'''

from tkinter import *  # noqa
import socket
import threading


# Función que levanta el servidor:
def servidor():
    # Direccion IP estática del Host:
    host = '10.0.2.16'
    # Puerto utilizado para la comunicacion:
    port = 65432

    # Creando el socket que utilizará el servidor:
    serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Uniendo la dirección IP con el puerto y esperando la
    # coneccion con el servidor:
    serv.bind((host, port))
    serv.listen(1)

    # Se determina la variable global para que se pueda utilizar
    # en otras secciones del codigo para la transmicion de datos:
    global conn
    # Se acepta la coneccion con el cliente:
    conn, address = serv.accept()


# Funcion para envio de datos:
def enviar_data(datos):

    # Se establece la variable global data, para poder utilizar de ella
    # en otras secciones de codigo:
    global data

    # Se establece el comando que envia la información al cliente:
    data = datos
    conn.send(data.encode())


# Funcion para recibir datos
def recibir_sms():

    # Se define la variable global:
    global sms

    # Se utliza un manejo de ecepciones para no devolver mensajes vacios:
    while 1:
        try:
            sms = conn.recv(1024).decode()
            if sms != '':
                return sms
        except BaseException:
            pass


'''
PRIMERA FILA DE BOTONES DE LA REJILLA
'''


# Funcion de cambio de turno del boton de la posicion 00. Las funciones para
# cada boton poseen la misma logica, por lo que se explicara a detalle
# solo una:
def next_turn00():

    # Para accesar al jugador en turno, se determina una variable global:
    global player

    # Si el texto del boton es vacio, y todavia nadie ha ganado. Si alguien
    # ganó o el boton ya fue presionado anteriormente, este queda bloqueado:
    if buttons00['text'] == '' and check_winner() is False:

        # Se determina el texto del boton como el nombre del jugador en turno
        if player == players[0]:
            buttons00['text'] = player

            # Si nadie ha ganado con el cambio anterior, se cambia de jugador:
            if check_winner() is False:
                player = players[1]
                label.config(text=('turno de '+players[1]))

            # Si alguien ganó, se declara:
            elif check_winner() is True:
                label.config(text=(players[0]+' ganó'))

            # Si nadie ganó:
            elif check_winner() == 'Empate':
                label.config(text='Empate')

        # Misma logica para el otro jugador
        else:
            buttons00['text'] = player

            if check_winner() is False:
                player = players[0]
                label.config(text=('turno de '+players[0]))

            elif check_winner() is True:
                label.config(text=(players[1]+' ganó'))

            elif check_winner() == 'Empate':
                label.config(text='Empate')

        # Función que envia datos a la otra maquina para activar el boton 00:
        boton = '00'
        enviar_data(boton)


def next_turn01():

    global player

    if buttons01['text'] == '' and check_winner() is False:
        if player == players[0]:
            buttons01['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=('turno de '+players[1]))
            elif check_winner() is True:
                label.config(text=(players[0]+' ganó'))
            elif check_winner() == 'Empate':
                label.config(text='Empate')
        else:
            buttons01['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=('turno de '+players[0]))
            elif check_winner() is True:
                label.config(text=(players[1]+' ganó'))
            elif check_winner() == 'Empate':
                label.config(text='Empate')
        boton = '01'
        enviar_data(boton)


def next_turn02():

    global player

    if buttons02['text'] == '' and check_winner() is False:
        if player == players[0]:
            buttons02['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=('turno de '+players[1]))
            elif check_winner() is True:
                label.config(text=(players[0]+' ganó'))
            elif check_winner() == 'Empate':
                label.config(text='Empate')
        else:
            buttons02['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=('turno de '+players[0]))
            elif check_winner() is True:
                label.config(text=(players[1]+' ganó'))
            elif check_winner() == 'Empate':
                label.config(text='Empate')
        boton = '02'
        enviar_data(boton)


'''
SEGUNDA FILA DE BOTONES DE LA REJILLA
'''


def next_turn10():

    global player

    if buttons10['text'] == '' and check_winner() is False:
        if player == players[0]:
            buttons10['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=('turno de '+players[1]))
            elif check_winner() is True:
                label.config(text=(players[0]+' ganó'))
            elif check_winner() == 'Empate':
                label.config(text='Empate')
        else:
            buttons10['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=('turno de '+players[0]))
            elif check_winner() is True:
                label.config(text=(players[1]+' ganó'))
            elif check_winner() == 'Empate':
                label.config(text='Empate')
        boton = '10'
        enviar_data(boton)


def next_turn11():

    global player

    if buttons11['text'] == '' and check_winner() is False:
        if player == players[0]:
            buttons11['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=('turno de '+players[1]))
            elif check_winner() is True:
                label.config(text=(players[0]+' ganó'))
            elif check_winner() == 'Empate':
                label.config(text='Empate')
        else:
            buttons11['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=('turno de '+players[0]))
            elif check_winner() is True:
                label.config(text=(players[1]+' ganó'))
            elif check_winner() == 'Empate':
                label.config(text='Empate')
        boton = '11'
        enviar_data(boton)


def next_turn12():

    global player

    if buttons12['text'] == '' and check_winner() is False:
        if player == players[0]:
            buttons12['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=('turno de '+players[1]))
            elif check_winner() is True:
                label.config(text=(players[0]+' ganó'))
            elif check_winner() == 'Empate':
                label.config(text='Empate')
        else:
            buttons12['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=('turno de '+players[0]))
            elif check_winner() is True:
                label.config(text=(players[1]+' ganó'))
            elif check_winner() == 'Empate':
                label.config(text='Empate')
        boton = '12'
        enviar_data(boton)


'''
TERCERA FILA DE BOTONES DE LA REJILLA
'''


def next_turn20():

    global player

    if buttons20['text'] == '' and check_winner() is False:
        if player == players[0]:
            buttons20['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=('turno de '+players[1]))
            elif check_winner() is True:
                label.config(text=(players[0]+' ganó'))
            elif check_winner() == 'Empate':
                label.config(text='Empate')
        else:
            buttons20['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=('turno de '+players[0]))
            elif check_winner() is True:
                label.config(text=(players[1]+' ganó'))
            elif check_winner() == 'Empate':
                label.config(text='Empate')
        boton = '20'
        enviar_data(boton)


def next_turn21():

    global player

    if buttons21['text'] == '' and check_winner() is False:
        if player == players[0]:
            buttons21['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=('turno de '+players[1]))
            elif check_winner() is True:
                label.config(text=(players[0]+' ganó'))
            elif check_winner() == 'Empate':
                label.config(text='Empate')
        else:
            buttons21['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=('turno de '+players[0]))
            elif check_winner() is True:
                label.config(text=(players[1]+' ganó'))
            elif check_winner() == 'Empate':
                label.config(text='Empate')
        boton = '21'
        enviar_data(boton)


def next_turn22():

    global player

    if buttons22['text'] == '' and check_winner() is False:
        if player == players[0]:
            buttons22['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=('turno de '+players[1]))
            elif check_winner() is True:
                label.config(text=(players[0]+' ganó'))
            elif check_winner() == 'Empate':
                label.config(text='Empate')
        else:
            buttons22['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=('turno de '+players[0]))
            elif check_winner() is True:
                label.config(text=(players[1]+' ganó'))
            elif check_winner() == 'Empate':
                label.config(text='Empate')
        boton = '22'
        enviar_data(boton)


def comunicacion_remota():

    # Activacion remota de botones:
    if recibir_sms() == '00':
        buttons00.invoke()

    if recibir_sms() == '01':
        buttons01.invoke()

    if recibir_sms() == '02':
        buttons02.invoke()

    if recibir_sms() == '10':
        buttons10.invoke()

    if recibir_sms() == '11':
        buttons11.invoke()

    if recibir_sms() == '12':
        buttons12.invoke()

    if recibir_sms() == '20':
        buttons20.invoke()

    if recibir_sms() == '21':
        buttons21.invoke()

    if recibir_sms() == '22':
        buttons22.invoke()


def check_winner():

    # Se revisan todas las posibles opciones de gane por fila

    # Primera Fila:
    if buttons00['text'] == buttons01['text'] == buttons02['text'] != '':

        buttons00.config(bg='green')
        buttons01.config(bg='green')
        buttons02.config(bg='green')
        return True

    # Segunda Fila:
    elif buttons10['text'] == buttons11['text'] == buttons12['text'] != '':

        buttons10.config(bg='green')
        buttons11.config(bg='green')
        buttons12.config(bg='green')
        return True

    # Tercera Fila:
    elif buttons20['text'] == buttons21['text'] == buttons22['text'] != '':

        buttons20.config(bg='green')
        buttons21.config(bg='green')
        buttons22.config(bg='green')
        return True

    # Se revisan todas las posibles opciones de gane por colunma:

    # Primera Columna
    elif buttons00['text'] == buttons10['text'] == buttons20['text'] != '':

        buttons00.config(bg='green')
        buttons10.config(bg='green')
        buttons20.config(bg='green')
        return True

    # Segunda Columna
    elif buttons01['text'] == buttons11['text'] == buttons21['text'] != '':

        buttons01.config(bg='green')
        buttons11.config(bg='green')
        buttons21.config(bg='green')
        return True

    # Tercera Columna
    elif buttons02['text'] == buttons12['text'] == buttons22['text'] != '':

        buttons02.config(bg='green')
        buttons12.config(bg='green')
        buttons22.config(bg='green')
        return True

    # Revisando la Diagonal \

    elif buttons00['text'] == buttons11['text'] == buttons22['text'] != '':

        buttons00.config(bg='green')
        buttons11.config(bg='green')
        buttons22.config(bg='green')
        return True

    # Revisando la Diagonal /

    elif buttons02['text'] == buttons11['text'] == buttons20['text'] != '':
        buttons02.config(bg='green')
        buttons11.config(bg='green')
        buttons20.config(bg='green')
        return True

    # En dado caso que nadie gane y se acaben las casillas:
    elif empty_spaces() is False:

        buttons00.config(bg='yellow')
        buttons01.config(bg='blue')
        buttons02.config(bg='yellow')

        buttons10.config(bg='blue')
        buttons11.config(bg='yellow')
        buttons12.config(bg='blue')

        buttons20.config(bg='yellow')
        buttons21.config(bg='blue')
        buttons22.config(bg='yellow')

        return 'Empate'

    else:
        return False


# Contador de espacios vacios para determinar empate:
def empty_spaces():

    spaces = 9

    if buttons00['text'] != '':
        spaces -= 1
    if buttons01['text'] != '':
        spaces -= 1
    if buttons02['text'] != '':
        spaces -= 1

    if buttons10['text'] != '':
        spaces -= 1
    if buttons11['text'] != '':
        spaces -= 1
    if buttons12['text'] != '':
        spaces -= 1

    if buttons20['text'] != '':
        spaces -= 1
    if buttons21['text'] != '':
        spaces -= 1
    if buttons22['text'] != '':
        spaces -= 1

    if spaces == 0:
        return False
    else:
        return True


# Generador de nuevo juego:
def new_game():

    global player

    # Generador del siguiente jugador:
    player = players[0]

    # Establecimiento de las condiciones iniciales del titulo y los botones:
    label.config(text='turno de '+player)

    buttons00.config(text='', bg='#F0F0F0')
    buttons01.config(text='', bg='#F0F0F0')
    buttons02.config(text='', bg='#F0F0F0')

    buttons10.config(text='', bg='#F0F0F0')
    buttons11.config(text='', bg='#F0F0F0')
    buttons12.config(text='', bg='#F0F0F0')

    buttons20.config(text='', bg='#F0F0F0')
    buttons21.config(text='', bg='#F0F0F0')
    buttons22.config(text='', bg='#F0F0F0')

    datos = 'reset'
    enviar_data(datos)


if __name__ == '__main__':

    servidor()

    # Activación de la recepcion de mensajes:
    recibir_thread = threading.Thread(target=recibir_sms)
    recibir_thread.start()
    comunic_thread = threading.Thread(target=comunicacion_remota)
    comunic_thread.start()

    window = Tk()  # noqa
    window.title('Gato 3x3')
    players = ['x', 'o']

    player = players[0]

    # Generador del indicador de turno:
    label = Label(text= 'turno de '+player, font=('consolas', 40))  # noqa
    label.pack(side='top')

    reset_button = Button(text='reiniciar', font=('consolas', 20),  # noqa
                          command=new_game
                          )

    reset_button.pack(side='top')

    frame = Frame(window)  # noqa
    frame.pack()

    buttons00 = Button(frame, text='', font=('consolas', 40), width=5,  # noqa
                       height=2, command=next_turn00
                       )

    buttons01 = Button(frame, text='', font=('consolas', 40), width=5,  # noqa
                       height=2, command=next_turn01
                       )

    buttons02 = Button(frame, text='', font=('consolas', 40), width=5,  # noqa
                       height=2, command=next_turn02
                       )

    buttons10 = Button(frame, text='', font=('consolas', 40), width=5,  # noqa
                       height=2, command=next_turn10
                       )

    buttons11 = Button(frame, text='', font=('consolas', 40), width=5,  # noqa
                       height=2, command=next_turn11
                       )

    buttons12 = Button(frame, text='', font=('consolas', 40), width=5,  # noqa
                       height=2, command=next_turn12
                       )

    buttons20 = Button(frame, text='', font=('consolas', 40), width=5,  # noqa
                       height=2, command=next_turn20
                       )

    buttons21 = Button(frame, text='', font=('consolas', 40), width=5,  # noqa
                       height=2, command=next_turn21
                       )

    buttons22 = Button(frame, text='', font=('consolas', 40), width=5,  # noqa
                       height=2, command=next_turn22
                       )

    # Organizacion de los botones por fila y columna en la interfaz grafica:
    buttons00.grid(row=0, column=0)
    buttons01.grid(row=0, column=1)
    buttons02.grid(row=0, column=2)

    buttons10.grid(row=1, column=0)
    buttons11.grid(row=1, column=1)
    buttons12.grid(row=1, column=2)

    buttons20.grid(row=2, column=0)
    buttons21.grid(row=2, column=1)
    buttons22.grid(row=2, column=2)

    # 'Loop' que se mantiene actualizando la interfaz.
    window.mainloop()
