# Iteration 5: Streamlit Interactive Components

import streamlit as st
st.markdown(
    """
    <style>
        body { background-color: #f5f5f5; }
        .stButton>button {
            width: 100%;
            height: 50px;
            font-size: 20px;
            font-weight: bold;
            border-radius: 12px;
            border: none;
            transition: 0.3s;
        }
        .stButton>button:hover {
            transform: scale(1.05);
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
            border: 2px solid #ddd;
            background-color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title('WELCOME TO MY WEB!')
st.write('Let`s go!!!.')
st.divider()
# 5.2.1 A text input for user comments.





import streamlit as st

st.subheader("📝 Deja tu comentario")

# Inicializar la lista si no existe
if "comentarios" not in st.session_state:
    st.session_state.comentarios = []

# Inputs del usuario
nombre = st.text_input("Dime tu nombre crack")
comentario = st.text_area("Escribe tu comentario")

# Botón para guardar
if st.button("Enviar comentario"):
    if nombre and comentario:
        st.session_state.comentarios.append((nombre, comentario))
        st.success("Comentario enviado ✅")
    else:
        st.warning("Por favor, completa ambos campos mi arma")


# Button

# Show user input from sidebar in main page
st.divider()

st.subheader("Elige tu lenguaje de programación favorito")
opcion = st.radio("Selecciona una opcion:", ["Python", "Javascript", "C++"], key="radio_col2")

if opcion == 'Python':
    st.success(f"Elegiste {opcion} , y menos mal sino el SEPE te expulsa del curso (Naaah no lo te preocupes)")
elif opcion == 'Javascript':
    st.success(f"Elegiste {opcion} asi que no sabes que haces con tu vida")
else:
    st.success(f"Elegiste {opcion} y asi te va")

st.divider()

# Slider
st.subheader("Slider")
user_age = st.slider("Select your age:", min_value=0, max_value=100, value=25)
st.write(f"You selected: {user_age} years old")
if user_age > 50:
    st.write(f"Vas por menos del 50% del juego de tu vida pasado asi que aprovecha al maximo lo que te queda")
    
st.divider()


st.subheader("¿Quieres saber un secreto?")

mostrar_mensaje = st.checkbox("Mostrar secreto")

if mostrar_mensaje:
    st.write("Eres el mejor analista de datos que existe actualmente en esta pagina (y el unico)")



# Mostrar comentarios guardados
st.divider()
st.subheader("Comentarios")

if st.session_state.comentarios:
    for n, c in reversed(st.session_state.comentarios):  # Muestra el más reciente arriba
        st.markdown(f"**{n}** dijo:")
        st.write(f"> {c}")
        st.markdown("---")
else:
    st.write("No hay comentarios todavia.")