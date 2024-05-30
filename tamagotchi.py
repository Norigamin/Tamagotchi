from tkinter import *
from AnimatedLabel import *
from ImageLabel import *
import random
import pygame

def app():
    # Configuración de la ventana
    global ventana
    ventana = Tk()
    ventana.title("Tamagotchi ¡MOLANG!")
    ventana.iconbitmap("tamagotchi_icon.ico")
    ventana.geometry("500x730")
    # ventana.resizable(0,0)

    # Variables
    score_comida = 40
    score_juego = 40
    score_descanso = 40
    state = "\nFeliz"
    edad = 0
    contador_interacciones = 0
    enfermo = False

    # Imagen de fondo
    imagen_tamagotchi = ImageLabel(ventana,"tamagotchi_bg.png")
    imagen_tamagotchi.place(x=0,y=100)

    #Imagenes Botones
    comer_button_image = PhotoImage(file="images/button_images/comer_button.png")
    jugar_button_image = PhotoImage(file="images/button_images/jugar_button.png")
    descansar_button_image = PhotoImage(file="images/button_images/descansar_button.png")
    reiniciar_button_image = PhotoImage(file="images/button_images/reiniciar_button.png")
    # Etiquetas
    titulo = Label(ventana, text="Tamagotchi\n¡MOLANG!", fg="red", font=("bold", 30))
    titulo.place(x=150, y=0)

    state_label = Label(ventana, text=f"Estado De Animo: {state}", background="#E3E026", font=("normal", 15))
    state_label.place(x=170, y=150)

    edad_label = Label(ventana, text=f"Edad: {edad}", font=("bold", 20), pady=10, background="#E3E026")
    edad_label.place(x=380, y=60)

    score_label_comer = Label(ventana, text=f"Comida: {score_comida}", font=("bold", 20), pady=10, background="#E3E026")
    score_label_comer.place(x=15, y=625)

    score_label_descansar = Label(ventana, text=f"Descanso: {score_descanso}", font=("bold", 20), pady=10, background="#E3E026")
    score_label_descansar.place(x=320, y=625)

    score_label_jugar = Label(ventana, text=f"Juego: {score_juego}", font=("bold", 20), pady=10, background="#E3E026")
    score_label_jugar.place(x=180, y=625)

    action_label_comer = Label(ventana, text="Alimentando a la mascota", background="#E3E026", font=("normal", 15))
    action_label_jugar = Label(ventana, text="Jugando con la mascota", background="#E3E026", font=("normal", 15))
    action_label_descansar = Label(ventana, text="Haciendo descansar a la mascota", background="#E3E026", font=("normal", 15))

    inicio_label1 = Label(ventana, text="¡Molang! esta relax...", background="#E3E026", font=("normal", 15))
    inicio_label2 = Label(ventana, text="Ójala ser ¡Molang!...", background="#E3E026", font=("normal", 15))
    inicio_label3 = Label(ventana, text="Pollito Mejor Amigo...", background="#E3E026", font=("normal", 15))

    bonus_label = Label(ventana, text="", font=("normal", 12), background="#E3E026")

    # GIFs
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

    enfermedad1 = AnimatedLabel(ventana, "images/enfermedad1.gif")
    enfermedad2 = AnimatedLabel(ventana, "images/enfermedad2.gif")

    muerte = AnimatedLabel(ventana, "images/muerte.gif")
    curado = AnimatedLabel(ventana, "images/curado.gif")
    enojado = AnimatedLabel(ventana, "images/enojado.gif")

    hambriento = AnimatedLabel(ventana, "images/hambriento.gif")
    cansado = AnimatedLabel(ventana, "images/cansado.gif")
    aburrido = AnimatedLabel(ventana, "images/aburrido.gif")

    # Funciones Botones
    def comer_action():
        play_music(["audio/SFX/comer.wav"],1)
        inicio1.place_forget()
        inicio2.place_forget()
        inicio3.place_forget()
        update_score(10, -6, -6)
        update_state()
        apply_bonus()

        if state == "Muerto":
            show_gif(muerte)
            stop_music()
            play_music(["audio/SFX/muerte.wav"],1)
        elif state == "¿Es Encerio?":
            show_gif(enojado)
            stop_music()
            play_music(["audio/SFX/no.wav"],1)
            update_score(-30, 0, 6)
            if score_comida <= 0:
                state == "Muerto"
                play_music(["audio/SFX/muerte.wav"],1)
        elif state == "Hambriento":
            show_gif(hambriento)
        elif state == "Cansado":
            show_gif(cansado)
        elif state == "Aburrido":
            show_gif(aburrido)
        else:
            show_gif(random.choice([comiendo1, comiendo2, comiendo3]))
    
        show_textlabel(action_label_comer, 140, 690)
        check_age()

    def jugar_action():
        play_music(["audio/SFX/jugar.wav"],1)
        inicio1.place_forget()
        inicio2.place_forget()
        inicio3.place_forget()
        update_score(-6, 10, -6)
        update_state()
        apply_bonus()

        if state == "Muerto":
            show_gif(muerte)
            stop_music()
            play_music(["audio/SFX/muerte.wav"],1)
        elif state == "Hambriento":
            show_gif(hambriento)
        elif state == "Cansado":
            show_gif(cansado)
        elif state == "Aburrido":
            show_gif(aburrido)
        else:
            show_gif(random.choice([jugando1, jugando2, jugando3]))

        show_textlabel(action_label_jugar, 150, 690)
        check_age()

    def descansar_action():
        play_music(["audio/SFX/descansar.wav"],1)
        inicio1.place_forget()
        inicio2.place_forget()
        inicio3.place_forget()
        update_score(-6, -6, 10)
        update_state()
        apply_bonus()

        if state == "Muerto":
            show_gif(muerte)
            stop_music()
            play_music(["audio/SFX/muerte.wav"],1)
        elif state == "¿Es Encerio?":
            show_gif(enojado)
            stop_music()
            play_music(["audio/SFX/no.wav"],1)
            update_score(6, 0, -30)
            if score_descanso <= 0:
                state == "Muerto"
                play_music(["audio/SFX/muerte.wav"],1)
        elif state == "Hambriento":
            show_gif(hambriento)
        elif state == "Cansado":
            show_gif(cansado)
        elif state == "Aburrido":
            show_gif(aburrido)
        else:
            show_gif(random.choice([descansando1, descansando2, descansando3]))

        show_textlabel(action_label_descansar, 110, 690)
        check_age()

    # Botones

    comer_button = Button(ventana, image=comer_button_image, command=comer_action)
    comer_button.place(x=140,y=470)

    jugar_button = Button(ventana, image=jugar_button_image, command=jugar_action)
    jugar_button.place(x=200,y=530)

    descansar_button = Button(ventana, image=descansar_button_image, command=descansar_action)
    descansar_button.place(x=270,y=470)

    reset_button = Button(ventana, image=reiniciar_button_image, command=reset)

    # Funciones
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
        enfermedad1.place_forget()
        enfermedad2.place_forget()
        muerte.place_forget()
        curado.place_forget()
        hambriento.place_forget()
        cansado.place_forget()
        aburrido.place_forget()
        enojado.place_forget()
        gif_to_show.place(x=155, y=265)

    def show_textlabel(textlabel, x, y):
        action_label_comer.place_forget()
        action_label_jugar.place_forget()
        action_label_descansar.place_forget()
        inicio_label1.place_forget()
        inicio_label2.place_forget()
        inicio_label3.place_forget()
        textlabel.place(x=x, y=y)

    def update_score(comida, juego, descanso):
        nonlocal score_comida, score_juego, score_descanso

        score_comida = max(0, min(score_comida + comida, 80))
        score_juego = max(0, min(score_juego + juego, 80))
        score_descanso = max(0, min(score_descanso + descanso, 80))

        score_label_comer.config(text=f"Comida: {score_comida}")
        score_label_jugar.config(text=f"Juego: {score_juego}")
        score_label_descansar.config(text=f"Descanso: {score_descanso}")

        update_state()
        
        if state == "Muerto":
            show_gif(muerte)
            stop_music()
            reset_button.place(x=0,y=0)

    def apply_bonus():
        nonlocal score_comida, score_juego, score_descanso
    
        if score_comida >= 34 and score_juego >= 34 and score_descanso >= 34:
            bonus = random.choice([(5, 5, 5), (5, 0, 0), (0, 5, 0), (0, 0, 5), (5, 5, 0), (0, 5, 5), (5, 0, 5)])
    
            score_comida = max(0, min(score_comida + bonus[0], 80))
            score_juego = max(0, min(score_juego + bonus[1], 80))
            score_descanso = max(0, min(score_descanso + bonus[2], 80))
    
            score_label_comer.config(text=f"Comida: {score_comida}")
            score_label_jugar.config(text=f"Juego: {score_juego}")
            score_label_descansar.config(text=f"Descanso: {score_descanso}")
    
            bonus_label.config(text=f"Bonus: {bonus}\nPuntos Por\nBuen Amigo")
            bonus_label.place(x=20, y=70)
            play_music(["audio/SFX/bonus.wav"],0.3)
        else:
            bonus_label.place_forget()

    def update_state():
        nonlocal state
        if score_comida <= 0 or score_descanso <= 0:
            state = "Muerto"
            state_label.config(background="gray")

            comer_button.config(state=DISABLED)
            jugar_button.config(state=DISABLED)
            descansar_button.config(state=DISABLED)
        elif score_juego <= 0:
            state = "¿Es Encerio?"
            state_label.config(background="gray")
            jugar_button.config(state=DISABLED)
        elif score_comida < 30:
            state = "Hambriento"
            state_label.config(background="salmon")
        elif score_juego < 30:
            state = "Aburrido"
            state_label.config(background="salmon")
        elif score_descanso < 30:
            state = "Cansado"
            state_label.config(background="salmon")
        elif (30 < score_comida < 60) or (30 < score_descanso < 60) or (30 < score_juego < 60):
            state = "Satisfecho"
            state_label.config(background="lime")
        else:
            state = "Muy Feliz"
            state_label.config(background="gold")

        state_label.config(text=f"Estado De Animo: \n{state}")

    def check_age():
        nonlocal edad, contador_interacciones, enfermo

        contador_interacciones += 1

        if enfermo:
            check_survive()
        elif contador_interacciones >= 3:
            edad += 1
            edad_label.config(text=f"Edad: {edad}")
            contador_interacciones = 0
            if edad >= 5:
                check_sick()

    def check_sick():
        nonlocal state, enfermo
        probabilidad_enfermo = random.randint(1, 3)
        if probabilidad_enfermo == 2:
            enfermo = True
            state = "Enfermo"
            state_label.config(text=f"Estado De Animo: \n{state}", background="purple")
            show_gif(random.choice([enfermedad1, enfermedad2]))
            play_music(["audio/SFX/enfermedad.wav"],1)

    def check_survive():
        nonlocal state, enfermo, contador_interacciones

        if contador_interacciones >= 3:
            probabilidad_survive = random.randint(1, 3)
            if probabilidad_survive == 2:
                state = "Muerto"
                state_label.config(text=f"Estado De Animo: \n{state}", background="gray")
                show_gif(muerte)
                stop_music()
                play_music(["audio/SFX/muerte.wav"],1)
                reset_button.place(x=0,y=0)
                
                comer_button.config(state=DISABLED)
                jugar_button.config(state=DISABLED)
                descansar_button.config(state=DISABLED)
            else:
                state = "Curado"
                state_label.config(text=f"Estado De Animo: \n{state}", background="pink")
                show_gif(curado)
                play_music(["audio/SFX/curado.wav"],1)
            enfermo = False
            contador_interacciones = 0

    #Configuración Música y Efectos De Sonido
    pygame.mixer.init()

    def play_music(sounds,volume):
        if not sounds:
            return    
        
        sound = pygame.mixer.Sound(sounds[0])
        sound.set_volume(volume)
        sound.play()
        sound_length = sound.get_length()
        ventana.after(int(sound_length * 1000), lambda: play_music(sounds[1:],1))

    def stop_music():
        pygame.mixer.stop()

    # Imagenes y textos de inicio aleatorios
    show_gif(random.choice([inicio1, inicio2, inicio3]))
    show_textlabel(random.choice([inicio_label1, inicio_label2, inicio_label3]), 160, 690)
    #Música de fondo
    play_music(["audio/music/background_music.ogg"],0.5)

    ventana.mainloop()

def reset():
        ventana.destroy()
        app()
        
if __name__ == "__main__":
    app()