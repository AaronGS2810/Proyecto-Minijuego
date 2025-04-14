import streamlit as st
import random

# Estilo visual claro
st.markdown("""
    <style>
        body, .stApp, html, [class*="css"]  {
            background-color: #ffffff;
            color: black;
        }
        .stButton>button {
            width: 100%;
            height: 50px;
            font-size: 20px;
            font-weight: bold;
            border-radius: 12px;
            border: none;
            transition: 0.3s;
            background-color: #e0e0e0;
            color: black;
        }
        .stButton>button:hover {
            transform: scale(1.05);
            background-color: #d0d0d0;
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
            border: 2px solid #aaa;
            background-color: #f5f5f5;
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

# Título
st.title('WORDLE!')
st.write('Wordle es un juego de palabras en el que el objetivo es adivinar una palabra secreta en un número limitado de intentos.')
st.divider()

# Palabras por longitud
if "palabras_por_longitud" not in st.session_state:
    st.session_state.palabras_por_longitud = {
        4: ["casa", "amor", "niño", "vida", "pera", "mano", "mesa", "tuna", "ropa"],
        5: ["perro", "mujer", "tarde", "niños", "madre", "padre", "radio", "plato", "calle"],
        6: ["camino", "amigos", "nevera", "mañana", "comida", "escena", "pueblo", "ciudad", "dinero"],
        7: ["montaña", "persona", "domingo", "familia", "momento", "ventana", "botella", "trabajo", "silencio"],
        8: ["cuaderno", "escalera", "bombilla", "computar", "chorizos", "panadero", "mensajes", "problema", "telefono"],
        9: ["universos", "mensajero", "mariposas", "aguacates", "escritora", "activista", "televisor", "diligente", "habitante"],
        10: ["bicicletas", "panoramica", "cumpleaños", "revolucion", "fotografia", "organizado", "enfermeria", "muletillas", "relaciones"]
    }

# Selección de longitud y dificultad
num = st.selectbox("Introduce el número de letras para jugar", list(st.session_state.palabras_por_longitud.keys()))
dificultad = st.radio("Elige tu dificultad", ("Facil", "Intermedio", "Dificil"))

# Determinar intentos
if dificultad == "Facil":
    intentos = 6
elif dificultad == "Intermedio":
    intentos = 5
else:
    intentos = 4

# Inicializar sesión
if "intentos_previos" not in st.session_state:
    st.session_state.intentos_previos = []

# Botón empezar
if st.button("Empezar"):
    st.session_state.random_word = random.choice(st.session_state.palabras_por_longitud[num]).upper()
    st.session_state.random_list = list(st.session_state.random_word)
    st.session_state.intentos = intentos
    st.session_state.fin_juego = False
    st.session_state.intentos_previos = []

    # 👇 Scroll automático al input
    st.markdown("""
        <script>
            window.location.href = '#entrada';
        </script>
    """, unsafe_allow_html=True)

# Mostrar campo de juego si la palabra ya fue generada
if "random_word" in st.session_state and not st.session_state.get("fin_juego", False):

    # 📍 Punto al que hacemos scroll
    st.markdown("<div id='entrada'></div>", unsafe_allow_html=True)

    user_word = st.text_input("Introduce una palabra", max_chars=num).upper()

    if len(user_word) == num:
        user_list = list(user_word)
        st.session_state.intentos -= 1

        resultado = []
        for i in range(num):
            letra = user_list[i]
            if letra == st.session_state.random_list[i]:
                resultado.append((letra, "#6aaa64"))  # Verde
            elif letra in st.session_state.random_list:
                resultado.append((letra, "#c9b458"))  # Amarillo
            else:
                resultado.append((letra, "#787c7e"))  # Gris

        st.session_state.intentos_previos.append(resultado)

        # Mostrar intentos
        for lista in st.session_state.intentos_previos:
            with st.container():
                col = st.columns(num)
                for i, (letra, color) in enumerate(lista):
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

        # Verificar victoria
        if user_list == st.session_state.random_list:
            st.success("🎉 ¡MUY BIEN! Has ganado máquina.")
            st.balloons()
            st.session_state.fin_juego = True

        # Verificar derrota
        if st.session_state.intentos == 0 and user_list != st.session_state.random_list:
            st.error(f"Hoy no es tu día 😅 La palabra era: {st.session_state.random_word}")
            st.session_state.fin_juego = True

# Mostrar botón de reinicio si el juego terminó
if st.session_state.get("fin_juego", False):
    st.markdown("---")
    st.subheader("¿Quieres volver a jugar?")
    if st.button("🔁 Reiniciar juego"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        try:
            from streamlit.runtime.scriptrunner import rerun
            rerun()
        except:
            st.experimental_rerun()
