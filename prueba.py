import streamlit as st
import random

# DATOS
palabras_por_longitud = {
    4: ["casa", "amor", "niño", "vida", "pera", "mano", "mesa", "tuna", "ropa"],
    5: ["perro", "mujer", "tarde", "niños", "madre", "padre", "radio", "plato", "calle"],
    6: ["camino", "amigos", "nevera", "mañana", "comida", "escena", "pueblo", "ciudad", "dinero"],
    7: ["montaña", "persona", "domingo", "familia", "momento", "ventana", "botella", "trabajo", "silencio"],
    8: ["cuaderno", "escalera", "bombilla", "computar", "chorizos", "panadero", "mensajes", "problema", "telefono"],
    9: ["universos", "mensajero", "mariposas", "aguacates", "escritora", "activista", "televisor", "diligente", "habitante"],
    10: ["bicicletas", "panoramica", "revolucion", "organizado", "enfermeria", "muletillas", "relaciones"]
}

st.title("🔤 Wordle MiniJuego")

# Reiniciar juego
if st.button("🔁 Reiniciar juego"):
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.experimental_rerun()

# Selección inicial
if "palabra" not in st.session_state:
    st.session_state.n_letras = st.selectbox("Selecciona la cantidad de letras:", list(palabras_por_longitud.keys()))
    st.session_state.dificultad = st.radio("Selecciona la dificultad:", ["Fácil", "Intermedio", "Difícil"])

    dificultad_map = {
        "Fácil": 6,
        "Intermedio": 5,
        "Difícil": 4
    }

    st.session_state.intentos_restantes = dificultad_map[st.session_state.dificultad]
    st.session_state.palabra = random.choice(palabras_por_longitud[st.session_state.n_letras]).upper()
    st.session_state.historial = []
    st.session_state.fin_juego = False

# Entrada del jugador
if not st.session_state.fin_juego:
    guess = st.text_input(f"Introduce una palabra de {st.session_state.n_letras} letras:", max_chars=st.session_state.n_letras).strip().upper()

    if st.button("Probar palabra"):
        if len(guess) != st.session_state.n_letras:
            st.warning(f"La palabra debe tener {st.session_state.n_letras} letras.")
        else:
            resultado = []
            palabra_objetivo = st.session_state.palabra
            for i in range(len(guess)):
                if guess[i] == palabra_objetivo[i]:
                    resultado.append(f":green[{guess[i]}]")
                elif guess[i] in palabra_objetivo:
                    resultado.append(f":orange[{guess[i]}]")
                else:
                    resultado.append(f":gray[{guess[i]}]")

            st.session_state.historial.append(" ".join(resultado))

            if guess == palabra_objetivo:
                st.success("🎉 ¡Felicidades, has adivinado la palabra!")
                st.session_state.fin_juego = True
            else:
                st.session_state.intentos_restantes -= 1
                if st.session_state.intentos_restantes == 0:
                    st.error(f"😢 Te has quedado sin intentos. La palabra era: **{st.session_state.palabra}**")
                    st.session_state.fin_juego = True

# Mostrar historial
st.subheader("Intentos anteriores:")
for intento in st.session_state.historial:
    st.markdown(intento)

# Mostrar intentos restantes
if not st.session_state.fin_juego:
    st.info(f"🔁 Intentos restantes: {st.session_state.intentos_restantes}")
else:
    st.button("🔁 Reiniciar juego")  # Mostrar también si ya terminó

