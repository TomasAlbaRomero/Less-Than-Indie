# app.py - Versión optimizada para Python 3.13
import streamlit as st
from typing import List, Dict, Any

# Configuración básica de la página - DEBE SER LA PRIMERA LÍNEA
st.set_page_config(
    page_title="Less Than Indie",
    page_icon="👕",
    layout="wide"
)

# CSS con sidebar claro
st.markdown("""
<style>
    /* Fondo general violeta claro */
    .stApp {
        background-color: #f5f3ff;
    }

    /* Sidebar CLARO */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 2px solid #e5deff;
    }

    /* Texto del sidebar - OSCURO */
    [data-testid="stSidebar"] * {
        color: #333333 !important;
    }

    /* Títulos del sidebar */
    [data-testid="stSidebar"] h1, 
    [data-testid="stSidebar"] h2, 
    [data-testid="stSidebar"] h3 {
        color: #5b4b8a !important;
    }

    /* Inputs del sidebar con fondo claro */
    [data-testid="stSidebar"] .stTextInput input,
    [data-testid="stSidebar"] .stSelectbox select,
    [data-testid="stSidebar"] .stNumberInput input {
        background-color: #f8f7ff;
        color: #333333 !important;
        border: 1px solid #d4ccee;
        border-radius: 5px;
    }

    /* Labels de los inputs */
    [data-testid="stSidebar"] label {
        color: #5b4b8a !important;
        font-weight: 600;
    }

    /* Radio buttons y sliders */
    [data-testid="stSidebar"] .stRadio label,
    [data-testid="stSidebar"] .stSlider label {
        color: #333333 !important;
        font-weight: 500;
    }

    /* Slider styling */
    [data-testid="stSidebar"] .stSlider .stSliderValue {
        color: #5b4b8a !important;
        font-weight: bold;
    }

    /* Placeholder de inputs */
    [data-testid="stSidebar"] .stTextInput input::placeholder {
        color: #888888 !important;
    }

    /* Contenido principal */
    .main .block-container {
        background-color: white;
        border-radius: 10px;
        padding: 2rem;
        margin: 1rem;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }

    /* Títulos */
    h1, h2, h3 {
        color: #5b4b8a !important;
    }

    /* Texto normal */
    .stMarkdown, .stText {
        color: #333333 !important;
    }

    /* Botones */
    .stButton button {
        background-color: #7e69ab;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }

    /* Efecto hover en botones */
    .stButton button:hover {
        background-color: #6d5bbd;
    }
</style>
""", unsafe_allow_html=True)


# Datos de las marcas usando type hints mejorados
def cargar_datos() -> List[Dict[str, Any]]:
    """Carga los datos de las marcas de ropa."""
    marcas = [
        {
            "nombre": "0800spice",
            "descripcion": "SPICE es una marca de moda argentina que fusiona actitud urbana y diseño contemporáneo. Con piezas versátiles, estilos audaces y envíos a todo el país, invita a expresar tu individualidad con cada prenda.",
            "ubicacion": "Av de Mayo 1370, piso 4 oficina 52, Monserrat, CABA",
            "enlace_compra": "https://spice.empretienda.com.ar/",
            "precio": 30_000,  # Usando underscore para mejor legibilidad
            "categoria": "buzos"
        },
        {
            "nombre": "Pancha community",
            "descripcion": "Pancha Community nació de la idea de dos emprendedoras que no encontraban la marca que querían consumir, así que decidieron crearla. Con diseño propio y atención personalizada, ofrecen accesorios y complementos de moda en Argentina con envío a todo el país, y una estética cercana, fresca y accesible.",
            "ubicacion": "Belgrano | Pick up point",
            "enlace_compra": "https://panchacommunity.com/",
            "precio": 80_000,
            "categoria": "accesorios"
        },
        {
            "nombre": "KAZARIAN | rockstar wear",
            "descripcion": "KAZARIAN es una marca argentina de moda rock-chic que reinterpreta el espíritu urbano con actitud. Con colecciones de baby tees, tank tops, pantalones y accesorios, invita a vestirse con personalidad y estilo rebelde. Desde su showroom en Villa Crespo (CABA) hasta su tienda online, KAZARIAN conecta con quien busca ser el centro de su propia pasarela.",
            "ubicacion": "Acevedo 1085, Villa Crespo, Buenos Aires, Argentina 1414",
            "enlace_compra": "https://kazarian.com.ar/",
            "precio": 40_000,
            "categoria": "remeras"
        }
    ]
    return marcas


def aplicar_filtros(marcas: List[Dict[str, Any]],
                    busqueda: str,
                    categoria_seleccionada: str,
                    precio_min: int,
                    precio_max: int) -> List[Dict[str, Any]]:
    """Aplica los filtros a la lista de marcas."""
    marcas_filtradas = []

    for marca in marcas:
        # Filtro por búsqueda
        if busqueda and busqueda.lower() not in marca['nombre'].lower():
            continue

        # Filtro por categoría
        if categoria_seleccionada != "Todas" and marca['categoria'] != categoria_seleccionada:
            continue

        # Filtro por precio
        if not (precio_min <= marca['precio'] <= precio_max):
            continue

        marcas_filtradas.append(marca)

    return marcas_filtradas


def mostrar_marca(marca: Dict[str, Any], index: int) -> None:
    """Muestra la información de una marca individual."""
    st.markdown(f"### {marca['nombre']}")
    st.write(f"**Descripción:** {marca['descripcion']}")
    st.write(f"**Ubicación:** {marca['ubicacion']}")
    st.write(f"**Categoría:** {marca['categoria'].capitalize()}")
    st.write(f"**Precio:** ${marca['precio']:,}")

    # Usar columnas para el botón
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button(f"Comprar", key=f"btn_{index}"):
            st.markdown(f"[Ir a la tienda]({marca['enlace_compra']})")


def main() -> None:
    """Función principal de la aplicación."""
    # Header
    st.title("👕 Less Than Indie")
    st.markdown("**Descubre marcas de ropa alternativa y sostenible**")
    st.markdown("---")

    # Cargar datos
    marcas = cargar_datos()

    # Sidebar
    with st.sidebar:
        st.header("🔍 Filtros")

        # Filtro por nombre
        busqueda = st.text_input("Buscar por nombre:")

        # Filtro por categoría usando set comprehension
        categorias = ["Todas"] + list({marca['categoria'] for marca in marcas})
        categoria_seleccionada = st.selectbox("Categoría:", categorias)

        # Filtro por precio
        st.write("Rango de precios:")
        precios = [marca['precio'] for marca in marcas]
        precio_min, precio_max = st.slider(
            "Precio:",
            min_value=min(precios),
            max_value=max(precios),
            value=(min(precios), max(precios))
        )

        # Ordenamiento
        orden = st.radio("Ordenar por precio:", ["Sin orden", "Menor a mayor", "Mayor a menor"])

    # Aplicar filtros
    marcas_filtradas = aplicar_filtros(
        marcas, busqueda, categoria_seleccionada, precio_min, precio_max
    )

    # Ordenar usando match case (nueva característica de Python 3.10+)
    match orden:
        case "Menor a mayor":
            marcas_filtradas.sort(key=lambda x: x['precio'])
        case "Mayor a menor":
            marcas_filtradas.sort(key=lambda x: x['precio'], reverse=True)
        case _:
            pass  # Sin orden

    # Mostrar resultados
    st.subheader(f"Marcas encontradas: {len(marcas_filtradas)}")

    if not marcas_filtradas:
        st.warning("No se encontraron marcas con los filtros seleccionados.")
        return

    # Mostrar marcas usando enumerate
    for i, marca in enumerate(marcas_filtradas):
        mostrar_marca(marca, i)
        st.markdown("---")


if __name__ == "__main__":
    main()