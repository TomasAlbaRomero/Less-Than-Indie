# app.py - Versión simplificada y funcional
import streamlit as st

# Configuración básica de la página - PRIMERA LÍNEA
st.set_page_config(
    page_title="Less Than Indie",
    page_icon="👕",
    layout="wide"
)

# CSS MÍNIMO Y SEGURO
st.markdown("""
<style>
    .stApp {
        background-color: #f5f3ff;
    }
    [data-testid="stSidebar"] {
        background-color: #ffffff;
    }
    .main .block-container {
        background-color: white;
        border-radius: 10px;
        padding: 2rem;
        margin: 1rem;
    }
    h1, h2, h3 {
        color: #5b4b8a;
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

        # Filtro por categoría
        categorias = ["Todas"] + list(set(marca['categoria'] for marca in marcas))
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
    marcas_filtradas = []
    for marca in marcas:
        if busqueda and busqueda.lower() not in marca['nombre'].lower():
            continue
        if categoria_seleccionada != "Todas" and marca['categoria'] != categoria_seleccionada:
            continue
        if not (precio_min <= marca['precio'] <= precio_max):
            continue
        marcas_filtradas.append(marca)

    # Ordenar (sin match case)
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
    for i, marca in enumerate(marcas_filtradas):
        st.markdown(f"### {marca['nombre']}")
        st.write(f"**Descripción:** {marca['descripcion']}")
        st.write(f"**Ubicación:** {marca['ubicacion']}")
        st.write(f"**Categoría:** {marca['categoria'].capitalize()}")
        st.write(f"**Precio:** ${marca['precio']:,}")

        if st.button(f"Comprar en {marca['nombre']}", key=f"btn_{i}"):
            st.markdown(f"[Ir a la tienda]({marca['enlace_compra']})")

        st.markdown("---")


if __name__ == "__main__":
    main()