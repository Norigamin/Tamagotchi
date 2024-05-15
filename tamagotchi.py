from tkinter import *
from AnimatedLabel import *
from ImageLabel import *
import random

def app():
    #Configuracion Ventana
    ventana = Tk()
    ventana.title("Tamagotchi ¡MOLANG!")
    ventana.iconbitmap("tamagotchi_icon.ico")
    ventana.geometry("500x700")
    # ventana.resizable(0,0)
    #Estado y Puntuacion
    score_comida = 40
    score_juego = 40
    score_descanso = 40
    state = "\nFeliz"
    #Etiqueta Titulo
    titulo = Label(ventana, text="Tamagotchi\n¡MOLANG!",fg="red",font=("bold",30),pady=10)
    titulo.place(x=150,y=0)
    #Imagen De Fondo
    imagen_tamagotchi = ImageLabel(ventana, "tamagotchi_bg.png")
    imagen_tamagotchi.place(x=0,y=100)
    #Etiqueta De Estado
    state_label = Label(ventana, text=f"Estado De Animo: {state}", background="#E3E026",font=("normal",15))
    state_label.place(x=170,y=150)
    #GIF'S

    inicio1 = AnimatedLabel(ventana, "images/inicio1.gif")
    inicio2 = AnimatedLabel(ventana, "images/inicio2.gif")
    inicio3 = AnimatedLabel(ventana, "images/inicio3.gif")

    comiendo1 = AnimatedLabel(ventana, "images/comiendo1.gif")
    comiendo2 = AnimatedLabel(ventana, "images/comiendo2.gif")
    comiendo3 = AnimatedLabel(ventana, "images/comiendo3.gif")

    descansando1 = AnimatedLabel(ventana, "images/descansando1.gif")
    descansando2 = AnimatedLabel(ventana, "images/descansando2.gif")
    descansando3 = AnimatedLabel(ventana, "images/descansando3.gif")

    jugando1 = AnimatedLabel(ventana, "images/jugando1.gif")
    jugando2 = AnimatedLabel(ventana, "images/jugando2.gif")
    jugando3 = AnimatedLabel(ventana, "images/jugando3.gif")

    def show_gif(gif_to_show):
        comiendo1.place_forget()
        comiendo2.place_forget()
        comiendo3.place_forget()
        descansando1.place_forget()
        descansando2.place_forget()
        descansando3.place_forget()
        jugando1.place_forget()
        jugando2.place_forget()
        jugando3.place_forget()
        gif_to_show.place(x=155,y=265)
            
    #IMAGEN DE INICIO ALEATORIA
    show_gif(random.choice([inicio1,inicio2,inicio3]))
    #Etiquetas De Puntuacion
    score_label_comer = Label(ventana, text=f"Comida: {score_comida}",font=("bold",20),pady=10,background="#E3E026")
    score_label_comer.place(x=15,y=625)
    score_label_descansar = Label(ventana, text=f"Descanso: {score_descanso}",font=("bold",20),pady=10,background="#E3E026")
    score_label_descansar.place(x=170,y=625)
    score_label_jugar = Label(ventana, text=f"Juego: {score_juego}",font=("bold",20),pady=10,background="#E3E026")
    score_label_jugar.place(x=360,y=625)

    #FUNCIONES - LÓGICA
    def create_button(text, command):
        button = Button(button_frame, text=text, background="black", foreground="white", command=command)
        button.pack(side=LEFT, padx=5)

    def update_score(comida, juego, descanso):
        nonlocal score_comida, score_juego, score_descanso

        score_comida += comida
        score_juego += juego
        score_descanso += descanso

        score_label_comer.config(text=f"Comida: {score_comida}")
        score_label_descansar.config(text=f"Descanso: {score_descanso}")
        score_label_jugar.config(text=f"Juego: {score_juego}")

    def update_state(type):
        nonlocal state
        #PARA CAMBIAR DE COLOR DE LA PUNTUACION ES CON score.label(background="blue")
        if type == 1:
            show_gif(random.choice([comiendo1, comiendo2, comiendo3]))
            if score_comida <= 30 and score_comida > 0:
                state = "\nHambriento"
                #imagen gif
                state_label.config(background="salmon")
                score_label_comer.config(background="red")
            elif score_comida > 30 and score_comida < 60:
                state = "\nSatisfecho"
                #imagen gif
                state_label.config(background="lime")
                score_label_comer.config(background="lime")
            elif score_comida >= 60 and score_comida < 80:
                state = "\nLleno"
                #imagen gif
                state_label.config(background="red")
                score_label_comer.config(background="red")
            else:
                state = "\nMuerto"
                #imagen gif
                state_label.config(background="gray")
                score_label_comer.config(background="gray")

        elif type == 2:
            show_gif(random.choice([jugando1, jugando2, jugando3]))
            if score_juego <= 30 and score_comida > 0:
                state = "\nAburrido"
                #imagen gif
                state_label.config(background="#E3C1F6")
                score_label_jugar.config(background="red")
            elif score_juego > 30 and score_juego < 60:
                state = "\nTranquilo"
                #imagen gif
                state_label.config(background="lime")
                score_label_jugar.config(background="lime")
            elif score_juego >= 60 and score_juego < 80:
                state = "\nHiperactivo"
                #imagen gif
                state_label.config(background="gold")
                score_label_jugar.config(background="red")
            else:
                state = "\nMuerto"
                #imagen gif
                state_label.config(background="gray")
                score_label_jugar.config(background="gray")

        elif type == 3:
            show_gif(random.choice([descansando1, descansando2, descansando3]))
            if score_descanso <= 30 and score_descanso > 0:
                state = "\nCansado"
                #imagen gif
                state_label.config(background="#7A4EB2")
                score_label_descansar.config(background="red")
            elif score_descanso > 30 and score_descanso < 60:
                state = "\nDescansado"
                #imagen gif
                state_label.config(background="lime")
                score_label_descansar.config(background="lime")
            elif score_descanso >= 60 and score_descanso < 80:
                state = "\nMuy Peresozo"
                #imagen gif
                state_label.config(background="aqua")
                score_label_descansar.config(background="red")
            else:
                state = "\nMuerto"
                #imagen gif
                state_label.config(background="gray")
                score_label_descansar.config(background="gray")

        state_label.config(text=f"Estado De Animo: {state}")

    def comer_action():
        update_score(10,-5,-5)
        update_state(1)
        print("Alimentando a la mascota")

    def jugar_action():
        update_score(-5,10,-5)
        update_state(2)
        print("Jugando con la mascota")

    def descansar_action():
        update_score(-5,-5,10)
        update_state(3)
        print("Haciendo descansar a la mascota")

    button_frame = Frame(ventana, background="black")
    button_frame.pack()

    create_button("Comer", comer_action)
    create_button("Jugar", jugar_action)
    create_button("Descansar", descansar_action)

    ventana.mainloop()

if __name__ == "__main__":
    app()