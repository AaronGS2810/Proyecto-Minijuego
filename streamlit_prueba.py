import streamlit as st
import random
st.markdown(
    """
    <style>
        body {
            background-color: #121212;
            color: white;
        }
        .stApp {
            background-color: #121212;
            color: white;
        }
        html, body, [class*="css"]  {
            background-color: #121212;
            color: white;
        }

        .stButton>button {
            width: 100%;
            height: 50px;
            font-size: 20px;
            font-weight: bold;
            border-radius: 12px;
            border: none;
            transition: 0.3s;
            background-color: #1f1f1f;
            color: white;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            background-color: #333333;
        }

        .play-button button {
            background-color: #4CAF50 !important;
            color: white;
        }
        .reset-button button {
            background-color: #f44336 !important;
            color: white;
        }

        .choice-box {
            text-align: center;
            padding: 15px;
            font-size: 22px;
            font-weight: bold;
            border-radius: 10px;
            border: 2px solid #444;
            background-color: #1e1e1e;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)


# TITULO

st.title('WORDLE!')
st.write('Wordle es un juego de palabras en el que el objetivo es adivinar una palabra secreta de cinco letras en un máximo de seis intentos.')
st.divider()

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
# st.selectbox(label="hola", options=(4,5,6,7,8,9,10))
num = st.selectbox(label="Introduce el numero de letras para jugar", options= (x for x in st.session_state.palabras_por_longitud.keys()))
st.write(f"El numero es {num}")
# DIFICULTAD

F = "Facil"
I = "Intermedio"
D = "Dificil"

dificultad = st.radio("Elige tu dificultad", (F,I,D))

st.divider()

if num in st.session_state.palabras_por_longitud:
    st.write(f"El numero es {num} y la palabra es ")

# INTENTOS

if dificultad == F:
        intentos = 6
if dificultad == I:
        intentos = 5
if dificultad == D:
        intentos = 4

st.write(f"Tienes {intentos} intentos para pasarte el juego")

# BOTON EMPEZAR
# if st.button("Empezar"):
#     if "random_word" not in st.session_state:
#         st.session_state.random_word = random.choice(st.session_state.palabras_por_longitud[num]).upper()


# user_word = st.text_input("Introduzca la palabra", value="").upper()
# user_list=[]
# for letra in user_word:
#     user_list.append(letra)

# if "user_list" not in st.session_state:
#     st.session_state.user_list = user_list


    
# if "random_list" not in st.session_state:
#     st.session_state.random_list = random_list

# st.write(f"La palabra es {st.session_state.random_list}")

if "intentos_previos" not in st.session_state:
    st.session_state.intentos_previos = []

if st.button("Empezar"):
    st.session_state.random_word = random.choice(st.session_state.palabras_por_longitud[num]).upper()
    random_list =[]
    for letra in st.session_state.random_word:
        random_list.append(letra)
    st.session_state.random_list = random_list  # lista de letras

# Mostrar palabra aleatoria (si ya fue generada)
if "random_word" in st.session_state:
    st.write(f"✅ La palabra aleatoria es: {st.session_state.random_word}")

    # Entrada del usuario
    user_word = st.text_input("Introduzca la palabra",key="valor_entrada", value="",max_chars=num).upper()
    if len(user_word) == num:
        user_list = list(user_word)

        


        st.write(f"🔤 Letras ingresadas: {user_list}")
        st.write(f"🧠 Letras de la palabra correcta: {st.session_state.random_list}")

        #--------------------------------------------
        #--------------------------------------------

        resultado = []
        for i in range(len(user_list)):
            letra = user_list[i]
            if letra == st.session_state.random_list[i]:
                resultado.append((letra,"#6aaa64"))  # Verde
            elif letra in st.session_state.random_list:
                resultado.append((letra,"#c9b458"))  # Amarillo
            else:
                resultado.append((letra,"#787c7e"))  # Gris

        st.session_state.intentos_previos.append(resultado)
        st.write(f"{st.session_state.intentos_previos}")

        #for i in range(num):
        for lista in st.session_state.intentos_previos:
            col = st.columns(num)
            for i, (letra,color) in enumerate(lista):
                col[i].markdown(
                f"""
                <div style='
                    width: 75px;
                    height: 75px;
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
            if user_list == st.session_state.random_list:
                 st.write(f"Ganasteeee")
            intentos -=1
            if intentos == 0:
                 st.write(f"Perdiste")
        #--------------------------------------------------
        #-------------------------------------------
    st.session_state.valor_entrada = ""

else:
    st.info("Presiona 'Empezar' para generar una palabra aleatoria.")

# resultado = []
# for i in range(len(user_list)):
#     letra = user_list[i]
#     if letra == st.session_state.random_list[i]:
#         resultado.append((letra,"#6aaa64"))  # Verde
#     elif letra in st.session_state.random_list:
#         resultado.append((letra,"#c9b458"))  # Amarillo
#     else:
#         resultado.append((letra,"#787c7e"))  # Gris

# st.session_state.intentos_previos.append(resultado)
# st.write(f"{st.session_state.intentos_previos}")

# #for i in range(num):
# for lista in st.session_state.intentos_previos:
#     col = st.columns(num)
#     for i, (letra,color) in enumerate(lista):
#         col[i].markdown(
#         f"""
#         <div style='
#             width: 50px;
#             height: 50px;
#             background-color: {color};
#             color: white;
#             font-size: 24px;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             border-radius: 5px;
#             margin: auto;
#         '>{letra}</div>
#         """,
#         unsafe_allow_html=True
#     )
    


