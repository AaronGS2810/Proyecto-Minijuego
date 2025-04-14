import streamlit as st
import random
import base64

#poner fondo

def obtener_base64_local(imagen):
    with open(imagen, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

fondo_base64 = obtener_base64_local("fondo_app.png")
#Estilo de la pagina
st.markdown(
    f"""
    <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{fondo_base64}");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
            color: black;
        }}

        html, body, [class*="css"] {{
            background-color: transparent;
            color: black;
        }}

        .stButton>button {{
            width: 100%;
            height: 50px;
            font-size: 20px;
            font-weight: bold;
            border-radius: 12px;
            border: none;
            transition: 0.3s;
            background-color: #fff9c4;
            color: black;
        }}
        .stButton>button:hover {{
            transform: scale(1.05);
            background-color: #d0d0d0;
        }}

        .play-button button {{
            background-color: #4CAF50 !important;
            color: white;
        }}
        .reset-button button {{
            background-color: #f44336 !important;
            color: white;
        }}

        .choice-box {{
            text-align: center;
            padding: 15px;
            font-size: 22px;
            font-weight: bold;
            border-radius: 10px;
            border: 2px solid #aaa;
            background-color: rgba(255,255,255,0.8);
            color: black;
        }}
    </style>
    """,
    unsafe_allow_html=True
)



# TITULO
st.image("wordleeeee.png")
st.title('WORDLE!')
st.write('Wordle es un juego de palabras en el que el objetivo es adivinar una palabra secreta de cinco letras en un máximo de seis intentos.')
st.divider()

#lista de palabras
if "palabras_por_longitud" not in st.session_state: # El session_state es para guardar cosas
    st.session_state.palabras_por_longitud = {
    4: ["casa", "amor", "niño", "vida", "pera", "mano", "mesa", "tuna", "ropa"],
    5: ["perro", "mujer", "tarde", "niños", "madre", "padre", "radio", "plato", "calle"],
    6: ["camino", "amigos", "nevera", "mañana", "comida", "escena", "pueblo", "ciudad", "dinero"],
    7: ["montaña", "persona", "domingo", "familia", "momento", "ventana", "botella", "trabajo", "silencio"],
    8: ["cuaderno", "escalera", "bombilla", "computar", "chorizos", "panadero", "mensajes", "problema", "telefono"],
    9: ["universos", "mensajero", "mariposas", "aguacates", "escritora", "activista", "televisor", "diligente", "habitante"],
    10: ["bicicletas", "panoramica", "cumpleaños", "revolucion", "fotografia", "organizado", "enfermeria", "muletillas", "relaciones"]
}
    
if "expresion_ganadora" not in st.session_state:
    st.session_state.expresion_ganadora = ["Echa la loteria que estas en racha", "Estas a un paso de un Nobel de Literatura", "INCREIBLE!!! Eres la persona más inteligente de esta página",
    "¡Eres el Wordle Whisperer!",
    "MUY BIEN!!!! Has ganado maquina",
    "Diccionario humano detectado. Reiniciando el sistema.",
    "Ganaste. Otra vez. ¿Estás bien? ¿Es esto tu superpoder?",
    "Te vamos a prohibir jugar. Deja algo para los demás.",
    "La RAE quiere contratarte como oráculo.",
    "Si fueras más bueno, serías ilegal en varios países.",
    "Wordle lloró. No puede seguir así.",
    "Ni tus calcetines combinan tan bien como esas letras.",
    "Tienes más letras en orden que tu vida. Y eso es mucho decir.",
    "¿Ya avisaste a tus enemigos que hoy te sientes invencible?",
    "Con esa victoria, puedes reclamar una tostadora imaginaria.",
    "Ganaste al Wordle. Pero aún no puedes doblar bien las sábanas.",
    "La palabra de hoy era fácil… pero tú la hiciste arte.",
    "Si el Wordle fuera una batalla, tú ya estarías coronado en Valhalla."
]
    
if "expresion_perdedora" not in st.session_state:
    st.session_state.expresion_perdedora = [
    "Perdiste. Pero al menos no fue en público. Ah, espera…",
    "Tus letras estaban tan lejos de la palabra que NASA las rastreó como objetos voladores.",
    "La palabra no era 'ERROR', pero lo intentaste con el corazón.",
    "Wordle te ganó. De nuevo. ¿Te sientes atacado personalmente o solo derrotado espiritualmente?",
    "Tus intentos fueron como consejos de tu ex: bien intencionados, pero totalmente inútiles.",
    "Jugaste con ganas… y con cero resultados.",
    "¿Intentaste escribir 'ayuda'? Porque lo pareces necesitar.",
    "Esa palabra no era para ti. Ni para nadie sin un doctorado en telepatía.",
    "Te quedaste más cerca del llanto que de la palabra correcta.",
    "Tus letras bailaron alrededor de la respuesta, pero nunca se comprometieron. Como tú en tus relaciones.",
    "Wordle hoy: 1. Tú: 0. Tu dignidad: desaparecida.",
    "Si tu estrategia era no ganar, felicitaciones, fue impecable.",
    "Mira el lado bueno: al menos no perdiste en ajedrez contra una tostadora.",
    "Tus intentos fueron como mi fe en ti: se desvanecieron rápidamente.",
    "Ese resultado fue tan triste que el diccionario pidió una orden de alejamiento."
]

# st.selectbox(label="hola", options=(4,5,6,7,8,9,10))
num = st.selectbox(label="Introduce el numero de letras para jugar", options= (x for x in st.session_state.palabras_por_longitud.keys()))

# DIFICULTAD

F = "Facil"
I = "Intermedio"
D = "Dificil"

dificultad = st.radio("Elige tu dificultad", (F,I,D))

st.divider()

# if num in st.session_state.palabras_por_longitud:
#     st.write(f"El numero es {num} y la palabra es ")

# INTENTOS

if dificultad == F:
    intentos = 6
elif dificultad == I:
    intentos = 5
else:
    intentos = 4

if "intentos_previos" not in st.session_state:
    st.session_state.intentos_previos = []


#Boton de empezar
if st.button("Empezar"):
    st.session_state.random_word = random.choice(st.session_state.palabras_por_longitud[num]).upper()
    st.session_state.random_win = random.choice(st.session_state.expresion_ganadora)
    st.session_state.random_lose = random.choice(st.session_state.expresion_perdedora)
    random_list =[]
    for letra in st.session_state.random_word:
        random_list.append(letra)
    st.session_state.random_list = random_list  # lista de letras
    st.session_state.fin_juego = False


#Estando ya la palabra guardada en el session state
if "random_word" in st.session_state:
    #st.write(f" La palabra aleatoria es: {st.session_state.random_word}")

    # Entrada del usuario
    user_word = st.text_input("Introduzca la palabra",key="", value="",max_chars=num).upper()
    if len(user_word) == num:
        user_list = list(user_word)

        if "intentos" not in st.session_state:
            st.session_state.intentos= intentos
        
        st.session_state.intentos -= 1
        st.subheader(f"Tienes {st.session_state.intentos} intentos")
        
        #st.write(f"palabra puesta {user_list}")
        #st.write(f"palabra correcta {st.session_state.random_list}")

        #--------------------------------------------
        #--------------------------------------------

        resultado = []  #Donde se guardara la lista dde la palabra ingresada

        for i in range(len(user_list)):
            letra = user_list[i]
            if letra == st.session_state.random_list[i]:
                resultado.append((letra,"#6aaa64"))  # Verde
            elif letra in st.session_state.random_list and letra != st.session_state.random_list[i]:
                resultado.append((letra,"#c9b458"))  # Amarillo
            else:
                resultado.append((letra,"#787c7e"))  # Gris

        st.session_state.intentos_previos.append(resultado)
        #for i in range(num):
        for lista in st.session_state.intentos_previos:
            with st.container():
                col = st.columns(num)
                for i, (letra,color) in enumerate(lista):
                    col[i].markdown(
                        f"""
                        <div style='
                            width: 50px;
                            height: 50px;
                            background-color: {color};
                            color: white;
                            font-size: 18px;
                            display: flex;
                            align-items: center;
                            justify-content: center;
                            border-radius: 5px;
                            margin: auto;
                        '>{letra}</div>
                        """,
                        unsafe_allow_html=True
                    )
                st.write("")

        #Cuadno gana
        if user_list == st.session_state.random_list:
            st.success(f"{st.session_state.random_win}")
            st.balloons()
            st.session_state.intentos_previos = []
            st.session_state.fin_juego = True

        #Cuando pierde         
        if st.session_state.intentos == 0 and user_list != st.session_state.random_list:
            st.error(f"{st.session_state.random_lose}")
            st.write(f"La palabra era {st.session_state.random_word}")
            st.session_state.fin_juego = True
        #--------------------------------------------------
        #-------------------------------------------
# else:
#     st.info("Presiona 'Empezar' para generar una palabra aleatoria.")

    #Para reiniciar
if st.session_state.get("fin_juego", False):
    st.markdown("---")
    st.subheader("¿Quieres echarte otra partida?")
    if st.button("🔁 Reiniciar juego"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        try:
            st.experimental_rerun()
        except:
            st.write("VUELVE A PULSAR REINICIO QUE NO LE DISTE BIEN")

