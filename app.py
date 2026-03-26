import streamlit as st
from logica import Calculadora

st.set_page_config(page_title="Calculadora", layout="centered")

# Inicializar estados
if "calc" not in st.session_state:
    st.session_state.calc = Calculadora()
if "numero1" not in st.session_state:
    st.session_state.numero1 = None
if "operacion" not in st.session_state:
    st.session_state.operacion = None
if "display" not in st.session_state:
    st.session_state.display = ""
if "mensajes" not in st.session_state:
    st.session_state.mensajes = []
if "escribiendo" not in st.session_state:
    st.session_state.escribiendo = False


def presionar_tecla(tecla: str):
    calc = st.session_state.calc

    match tecla:
        case "C":
            st.session_state.numero1 = None
            st.session_state.operacion = None
            st.session_state.display = ""
            st.session_state.mensajes = []
            st.session_state.escribiendo = False

        case "+" | "-" | "x" | "/":
            st.session_state.numero1 = float(st.session_state.display)
            st.session_state.operacion = tecla
            st.session_state.display = ""
            st.session_state.mensajes.append(tecla)
            st.session_state.escribiendo = False

        case "=":
            if st.session_state.numero1 is not None and st.session_state.display:
                n1 = st.session_state.numero1
                n2 = float(st.session_state.display)
                op = st.session_state.operacion

                match op:
                    case "+":
                        resultado = calc.sumar(n1, n2)
                    case "-":
                        resultado = calc.restar(n1, n2)
                    case "x":
                        resultado = calc.multiplicar(n1, n2)
                    case "/":
                        resultado = calc.dividir(n1, n2)

                st.session_state.mensajes.append(f"{n1} {op} {n2} = {resultado}")
                st.session_state.display = ""
                st.session_state.numero1 = None
                st.session_state.operacion = None
                st.session_state.escribiendo = False

        case _:
            st.session_state.display += tecla
            if st.session_state.escribiendo:
                st.session_state.mensajes[-1] = st.session_state.display
            else:
                st.session_state.mensajes.append(st.session_state.display)
                st.session_state.escribiendo = True

    st.rerun()


# Pantalla
st.subheader("Pantalla de Salida:")
pantalla = st.empty()

if st.session_state.mensajes:
    contenido = "\n".join(f"→ {msg}" for msg in st.session_state.mensajes)
    pantalla.text_area("", value=contenido, height=200, disabled=True)
else:
    pantalla.info("Presiona un botón para escribir aquí...")

# Teclado
filas = [
    ["7", "8", "9", "x"],
    ["4", "5", "6", "-"],
    ["1", "2", "3", "+"],
    ["0", ".", "C", "="],
]

for fila in filas:
    cols = st.columns(len(fila))
    for col, tecla in zip(cols, fila):
        with col:
            if st.button(tecla, use_container_width=True):
                presionar_tecla(tecla)
