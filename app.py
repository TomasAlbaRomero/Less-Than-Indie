# app.py - Versión con fondo violeta claro mejorado
import streamlit as st

# Configuración básica de la página
st.set_page_config(
    page_title="Less Than Indie",
    page_icon="👕",
    layout="wide"
)

# CSS con fondo violeta claro mejorado
st.markdown("""
<style>
    /* Fondo general VIOLETA CLARO */
    .stApp {
        background-color: #f5f3ff;
    }

    /* Sidebar violeta medio */
    section[data-testid="stSidebar"] {
        background-color: #7e69ab !important;
    }

    /* Texto del sidebar en blanco */
    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    /* Inputs del sidebar */
    section[data-testid="stSidebar"] .stTextInput input,
    section[data-testid="stSidebar"] .stSelectbox select,
    section[data-testid="stSidebar"] .stNumberInput input {
        background-color: rgba(255, 255, 255, 0.2);
        color: #ffffff !important;
        border: 1px solid rgba(255, 255, 255, 0.4);
    }

    /* Contenido principal con fondo blanco para máximo contraste */
    .main .block-container {
        background-color: white;
        border-radius: 15px;
        padding: 2.5rem;
        margin: 2rem;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        border: 1px solid #e5deff;
    }

    /* Títulos en color violeta para buen contraste */
    h1, h2, h3 {
        color: #5b4b8a !important;
        font-weight: 700 !important;
    }

    /* Texto normal en gris oscuro para mejor legibilidad */
    p, div, span, .stMarkdown, .stText {
        color: #333333 !important;
        font-weight: 400 !important;
        line-height: 1.6;
    }

    /* Texto específico de Streamlit */
    .stMarkdown p, .stMarkdown div, .stMarkdown span {
        color: #333333 !important;
    }

    /* Botones violeta atractivo */
    .stButton button {
        background-color: #7e69ab;
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        transition: background-color 0.3s ease;
    }

    .stButton button:hover {
        background-color: #6d5bbd;
    }

    /* Mejorar los labels de los filtros en el sidebar */
    section[data-testid="stSidebar"] label {
        font-weight: 600 !important;
        color: #ffffff !important;
        font-size: 1rem !important;
    }

    /* Placeholder de los inputs en blanco */
    section[data-testid="stSidebar"] .stTextInput input::placeholder {
        color: rgba(255, 255, 255, 0.8) !important;
    }

    /* Mejorar contraste del texto en warnings y mensajes */
    .stAlert {
        color: #000000 !important;
    }

    /* Texto del slider en sidebar */
    section[data-testid="stSidebar"] .stSlider label {
        color: #ffffff !important;
        font-weight: 500 !important;
    }

    /* Texto de los radio buttons en sidebar */
    section[data-testid="stSidebar"] .stRadio label {
        color: #ffffff !important;
        font-weight: 500 !important;
    }

    /* Separadores más sutiles */
    hr {
        border-color: #e5deff !important;
        margin: 1.5rem 0;
    }

    /* Mejorar el header principal */
    .stTitle {
        color: #5b4b8a !important;
    }

    /* Subtítulo */
    .stMarkdown h1, .stMarkdown h2, .stMarkdown h3 {
        color: #5b4b8a !important;
    }
</style>
""", unsafe_allow_html=True)


# Datos de las marcas
def cargar_datos():
    marcas = [
        {
            "nombre": "0800spice",
            "descripcion": "SPICE es una marca de moda argentina que fusiona actitud urbana y diseño contemporáneo. Con piezas versátiles, estilos audaces y envíos a todo el país, invita a expresar tu individualidad con cada prenda.",
            "ubicacion": "Av de Mayo 1370, piso 4 oficina 52, Monserrat, CABA",
            "enlace_compra": "https://spice.empretienda.com.ar/",
            "precio": 30000,
            "categoria": "buzos"
        },
        {
            "nombre": "Pancha community",
            "descripcion": "Pancha Community nació de la idea de dos emprendedoras que no encontraban la marca que querían consumir, así que decidieron crearla. Con diseño propio y atención personalizada, ofrecen accesorios y complementos de moda en Argentina con envío a todo el país, y una estética cercana, fresca y accesible.",
            "ubicacion": "Belgrano | Pick up point",
            "enlace_compra": "https://panchacommunity.com/",
            "precio": 80000,
            "categoria": "accesorios"
        },
        {
            "nombre": "KAZARIAN | rockstar wear",
            "descripcion": "KAZARIAN es una marca argentina de moda rock-chic que reinterpreta el espíritu urbano con actitud. Con colecciones de baby tees, tank tops, pantalones y accesorios, invita a vestirse con personalidad y estilo rebelde. Desde su showroom en Villa Crespo (CABA) hasta su tienda online, KAZARIAN conecta con quien busca ser el centro de su propia pasarela.",
            "ubicacion": "Acevedo 1085, Villa Crespo, Buenos Aires, Argentina 1414",
            "enlace_compra": "https://kazarian.com.ar/",
            "precio": 40000,
            "categoria": "remeras"
        }
    ]
    return marcas


def main():
    # Header simple
    st.title("👕 Less Than Indie")
    st.markdown("**Descubre marcas de ropa alternativa y sostenible**")
    st.markdown("---")

    # Cargar datos
    marcas = cargar_datos()

    # Sidebar simple
    with st.sidebar:
        st.header("🔍 Filtros")

        # Filtro por nombre
        busqueda = st.text_input("Buscar por nombre:", key="busqueda")

        # Filtro por categoría
        categorias = ["Todas"] + list(set(marca['categoria'] for marca in marcas))
        categoria = st.selectbox("Categoría:", categorias, key="categoria")

        # Filtro por precio
        st.write("Rango de precios:")
        precios = [marca['precio'] for marca in marcas]
        precio_min, precio_max = st.slider(
            "Precio:",
            min_value=min(precios),
            max_value=max(precios),
            value=(min(precios), max(precios)),
            key="precio"
        )

        # Ordenamiento
        orden = st.radio("Ordenar por precio:", ["Sin orden", "Menor a mayor", "Mayor a menor"], key="orden")

    # Aplicar filtros
    marcas_filtradas = []
    for marca in marcas:
        if busqueda and busqueda.lower() not in marca['nombre'].lower():
            continue
        if categoria != "Todas" and marca['categoria'] != categoria:
            continue
        if not (precio_min <= marca['precio'] <= precio_max):
            continue
        marcas_filtradas.append(marca)

    # Ordenar
    if orden == "Menor a mayor":
        marcas_filtradas.sort(key=lambda x: x['precio'])
    elif orden == "Mayor a menor":
        marcas_filtradas.sort(key=lambda x: x['precio'], reverse=True)

    # Mostrar resultados
    st.subheader(f"Marcas encontradas: {len(marcas_filtradas)}")

    if not marcas_filtradas:
        st.warning("No se encontraron marcas con los filtros seleccionados.")
        return

    # Mostrar marcas
    for marca in marcas_filtradas:
        st.markdown(f"### {marca['nombre']}")
        st.write(f"**Descripción:** {marca['descripcion']}")
        st.write(f"**Ubicación:** {marca['ubicacion']}")
        st.write(f"**Categoría:** {marca['categoria'].capitalize()}")
        st.write(f"**Precio:** ${marca['precio']:,}")

        if st.button(f"Comprar en {marca['nombre']}", key=marca['nombre']):
            st.markdown(f"[Ir a la tienda]({marca['enlace_compra']})")

        st.markdown("---")


if __name__ == "__main__":
    main()