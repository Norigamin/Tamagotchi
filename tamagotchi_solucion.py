from tkinter import *
from AnimatedLabel import *
from ImageLabel import *
import random
#HACER LISTA DE IMAGENES DE INICIO  RANDOM CADA VEZ QUE SE EJECUTA EL PROGRAMA [inicio1,inicio2,inicio3...]
def app():
    #Configuracion Ventana
    ventana = Tk()
    ventana.title("Tamagotchi ¡MOLANG!")
    ventana.iconbitmap("tamagotchi_icon.ico")
    ventana.geometry("500x700")
    # ventana.resizable(0,0)
    #Estado y Puntuacion
    score = 50
    state = "\nFeliz"
    #Etiqueta Titulo
    titulo = Label(ventana, text="Tamagotchi\n¡MOLANG!",fg="red",font=("bold",30),pady=10)
    titulo.place(x=150,y=0)
    #Imagen De Fondo
    imagen_tamagotchi = ImageLabel(ventana, "tamagotchi_bg.png")
    imagen_tamagotchi.place(x=0,y=100)
    #Etiqueta Estado
    state_label = Label(ventana, text=f"Estado De Animo: {state}", background="#E3E026", foreground="black",font=("normal",15))
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

    def lista_inicio_random(gif1,gif2,gif3):
        random_list = [gif1,gif2,gif3]
        show_list = random.choice(random_list)
        show_list.place(x=155,y=265)

    lista_inicio_random(inicio1,inicio2,inicio3)

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

    #Etiqueta Puntuacion
    score_label = Label(ventana, text=f"Puntuación\n{score}",font=("bold",20),pady=10)
    score_label.place(x=180,y=615)
    
    def create_button(text, command):
        button = Button(button_frame, text=text, background="black", foreground="white", command=command)
        button.pack(side=LEFT, padx=5)

    def update_score(change):
        nonlocal score
        score += change
        score_label.config(text=f"Puntaje: {score}")
        if score <= 20:
            state = "\nCansado"
            state_label.config(background="#7A4EB2")
        elif score >= 80:
            state = "\nFeliz"
            state_label.config(background="#E3E026")
        else:
            state = "\nHambriento"
            state_label.config(background="salmon")
        state_label.config(text=f"Estado De Animo: {state}")

    def comer_action():
        update_score(10)
        show_gif(random.choice([comiendo1, comiendo2, comiendo3]))
        print("Alimentando a la mascota")

    def jugar_action():
        update_score(-10)
        show_gif(random.choice([jugando1, jugando2, jugando3]))
        print("Jugando con la mascota")

    def dormir_action():
        update_score(5)
        show_gif(random.choice([descansando1, descansando2, descansando3]))
        print("Haciendo dormir a la mascota")

    button_frame = Frame(ventana, background="black")
    button_frame.pack()

    create_button("Comer", comer_action)
    create_button("Jugar", jugar_action)
    create_button("Dormir", dormir_action)

    ventana.mainloop()

if __name__ == "__main__":
    app()