# app.py - VERSIÓN COMPLETA Y COMPROBADA
import streamlit as st

# Configuración DEBE SER LA PRIMERA LÍNEA
st.set_page_config(
    page_title="Less Than Indie",
    page_icon="👕",
    layout="wide"
)

# CSS simple
st.markdown("""
<style>
    .stApp {
        background-color: #f5f3ff;
    }
    .main .block-container {
        background-color: white;
        border-radius: 10px;
        padding: 2rem;
        margin: 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Datos
marcas = [
    {
        "nombre": "0800spice",
        "descripcion": "SPICE es una marca de moda argentina que fusiona actitud urbana y diseño contemporáneo.",
        "ubicacion": "Av de Mayo 1370, CABA",
        "enlace_compra": "https://spice.empretienda.com.ar/",
        "precio": 30000,
        "categoria": "buzos"
    },
    {
        "nombre": "Pancha community",
        "descripcion": "Pancha Community nació de la idea de dos emprendedoras.",
        "ubicacion": "Belgrano",
        "enlace_compra": "https://panchacommunity.com/",
        "precio": 80000,
        "categoria": "accesorios"
    }
]

# Aplicación
st.title("👕 Less Than Indie")
st.markdown("**Descubre marcas de ropa alternativa y sostenible**")

# Sidebar
with st.sidebar:
    st.header("🔍 Filtros")
    busqueda = st.text_input("Buscar marca:")

    # Mostrar marcas
    st.header("🏷️ Marcas Disponibles")
    for marca in marcas:
        st.write(f"**{marca['nombre']}** - ${marca['precio']}")

# Contenido principal
st.header("📦 Catálogo de Marcas")
for marca in marcas:
    with st.container():
        st.subheader(marca['nombre'])
        st.write(marca['descripcion'])
        st.write(f"**Precio:** ${marca['precio']:,}")
        st.write(f"**Categoría:** {marca['categoria']}")

        if st.button(f"🛒 Comprar {marca['nombre']}", key=marca['nombre']):
            st.markdown(f"🔗 [{marca['nombre']}]({marca['enlace_compra']})")

        st.divider()

st.success("✨ Aplicación cargada correctamente")