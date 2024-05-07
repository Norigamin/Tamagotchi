import random
from tkinter import *

def lista_random(gif1,gif2,gif3):
    random_list = [gif1,gif2,gif3]
    show_list = random.choice(random_list)
    show_list.place(x=170,y=150)

# def lista_random(gif1, gif2, gif3):
#   random_list = [gif1, gif2, gif3]
#   mostrados = []

#   while len(mostrados) < len(random_list):
#     indice_aleatorio = random.randint(0, len(random_list) - 1)
#     if indice_aleatorio not in mostrados:
#       mostrados.append(indice_aleatorio)
#       show_list = random_list[indice_aleatorio]
#       show_list.place(x=155, y=265)

#CODIGO CON SHOW
#GIF'S

# inicio1 = AnimatedLabel(ventana, "images/inicio1.gif")
# inicio2 = AnimatedLabel(ventana, "images/inicio2.gif")
# inicio3 = AnimatedLabel(ventana, "images/inicio3.gif")

# comiendo1 = AnimatedLabel(ventana, "images/comiendo1.gif")
# comiendo2 = AnimatedLabel(ventana, "images/comiendo2.gif")
# comiendo3 = AnimatedLabel(ventana, "images/comiendo3.gif")

# descansando1 = AnimatedLabel(ventana, "images/descansando1.gif")
# descansando2 = AnimatedLabel(ventana, "images/descansando2.gif")
# descansando3 = AnimatedLabel(ventana, "images/descansando3.gif")

# jugando1 = AnimatedLabel(ventana, "images/jugando1.gif")
# jugando2 = AnimatedLabel(ventana, "images/jugando2.gif")
# jugando3 = AnimatedLabel(ventana, "images/jugando3.gif")

# def show_gif(gif_to_show):
        
#         inicio1.place_forget()
#         inicio2.place_forget()
#         inicio3.place_forget()
#         comiendo1.place_forget()
#         comiendo2.place_forget()
#         comiendo3.place_forget()
#         descansando1.place_forget()
#         descansando2.place_forget()
#         descansando3.place_forget()
#         jugando1.place_forget()
#         jugando2.place_forget()
#         jugando3.place_forget()
#         gif_to_show.place(x=155,y=265)

# def comer_action():
#         update_score(10)
#         show_gif(random.choice([comiendo1, comiendo2, comiendo3]))
#         print("Alimentando a la mascota")

#     def jugar_action():
#         update_score(-10)
#         show_gif(random.choice([jugando1, jugando2, jugando3]))
#         print("Jugando con la mascota")

#     def dormir_action():
#         update_score(5)
#         show_gif(random.choice([descansando1, descansando2, descansando3]))
#         print("Haciendo dormir a la mascota")
