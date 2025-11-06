# app.py - VERSIÓN COMPLETA CON TODAS LAS CARACTERÍSTICAS
import streamlit as st

# Configuración DEBE SER LA PRIMERA LÍNEA
st.set_page_config(
    page_title="Less Than Indie",
    page_icon="👕",
    layout="wide"
)

# CSS mejorado
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
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    h1, h2, h3 {
        color: #5b4b8a;
    }
    .stButton button {
        background-color: #7e69ab;
        color: white;
        border: none;
        border-radius: 5px;
        padding: 0.5rem 1rem;
    }
    .stButton button:hover {
        background-color: #6d5bbd;
    }
</style>
""", unsafe_allow_html=True)


# Datos completos de las marcas
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
        },
        {
            "nombre": "Urban Threads",
            "descripcion": "Marca emergente que combina sostenibilidad con diseño urbano. Todas las prendas están confeccionadas con materiales reciclados y procesos éticos de producción.",
            "ubicacion": "Palermo, CABA",
            "enlace_compra": "https://urbanthreads.example.com",
            "precio": 25000,
            "categoria": "remeras"
        },
        {
            "nombre": "EcoWear AR",
            "descripcion": "Primera marca argentina de moda circular. Specializados en prendas biodegradables y procesos de producción con cero desperdicios.",
            "ubicacion": "San Telmo, CABA",
            "enlace_compra": "https://ecowear.example.com",
            "precio": 45000,
            "categoria": "buzos"
        }
    ]
    return marcas


# Función principal
def main():
    st.title("👕 Less Than Indie")
    st.markdown("**Descubre marcas de ropa alternativa y sostenible**")
    st.markdown("---")

    # Cargar datos
    marcas = cargar_datos()

    # SIDEBAR CON TODOS LOS FILTROS ORIGINALES
    with st.sidebar:
        st.header("🔍 Filtros de Búsqueda")

        # Filtro por nombre
        busqueda = st.text_input("Buscar por nombre:")

        # Filtro por categoría
        categorias = ["Todas"] + sorted(list(set(marca['categoria'] for marca in marcas)))
        categoria_seleccionada = st.selectbox("Categoría:", categorias)

        # Filtro por precio
        st.write("**Rango de precios:**")
        precios = [marca['precio'] for marca in marcas]
        precio_min, precio_max = st.slider(
            "Selecciona el rango:",
            min_value=min(precios),
            max_value=max(precios),
            value=(min(precios), max(precios)),
            key="precio_slider"
        )

        # Ordenamiento
        st.write("**Ordenar resultados:**")
        orden = st.radio(
            "Criterio de orden:",
            ["Sin orden", "Menor a mayor", "Mayor a menor", "A-Z", "Z-A"],
            key="orden_radio"
        )

        # Estadísticas en sidebar
        st.markdown("---")
        st.write("**📊 Estadísticas:**")
        st.write(f"• Total de marcas: {len(marcas)}")
        st.write(f"• Categorías: {len(categorias) - 1}")
        st.write(f"• Precio promedio: ${sum(precios) // len(precios):,}")

    # APLICAR FILTROS COMPLETOS
    marcas_filtradas = []
    for marca in marcas:
        # Filtro por búsqueda de nombre
        if busqueda and busqueda.lower() not in marca['nombre'].lower():
            continue

        # Filtro por categoría
        if categoria_seleccionada != "Todas" and marca['categoria'] != categoria_seleccionada:
            continue

        # Filtro por precio
        if not (precio_min <= marca['precio'] <= precio_max):
            continue

        marcas_filtradas.append(marca)

    # APLICAR ORDENAMIENTO COMPLETO
    if orden == "Menor a mayor":
        marcas_filtradas.sort(key=lambda x: x['precio'])
    elif orden == "Mayor a menor":
        marcas_filtradas.sort(key=lambda x: x['precio'], reverse=True)
    elif orden == "A-Z":
        marcas_filtradas.sort(key=lambda x: x['nombre'])
    elif orden == "Z-A":
        marcas_filtradas.sort(key=lambda x: x['nombre'], reverse=True)

    # MOSTRAR RESULTADOS
    st.subheader(f"📦 Marcas encontradas: {len(marcas_filtradas)}")

    # Mensaje si no hay resultados
    if not marcas_filtradas:
        st.warning("🚫 No se encontraron marcas con los filtros seleccionados.")
        st.info("💡 Prueba ajustando los filtros para ver más resultados.")
        return

    # MOSTRAR CADA MARCA CON TODOS LOS DETALLES
    for i, marca in enumerate(marcas_filtradas):
        # Crear columnas para mejor layout
        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown(f"### 🏷️ {marca['nombre']}")
            st.write(f"**📝 Descripción:** {marca['descripcion']}")
            st.write(f"**📍 Ubicación:** {marca['ubicacion']}")

            # Info en columnas
            col_info1, col_info2 = st.columns(2)
            with col_info1:
                st.write(f"**📂 Categoría:** {marca['categoria'].capitalize()}")
            with col_info2:
                st.write(f"**💰 Precio:** ${marca['precio']:,}")

        with col2:
            # Botón de compra mejorado
            if st.button(f"🛒 Comprar", key=f"comprar_{i}", use_container_width=True):
                st.session_state[f'enlace_{i}'] = True

            # Mostrar enlace si se clickeó el botón
            if st.session_state.get(f'enlace_{i}', False):
                st.markdown(f"🔗 **[Ir a la tienda →]({marca['enlace_compra']})**")
                st.markdown(f"*{marca['enlace_compra']}*")

        st.markdown("---")

    # PIE DE PÁGINA CON ESTADÍSTICAS
    st.markdown("---")
    col_stats1, col_stats2, col_stats3 = st.columns(3)

    with col_stats1:
        st.metric("Marcas mostradas", len(marcas_filtradas))

    with col_stats2:
        if marcas_filtradas:
            avg_price = sum(m['precio'] for m in marcas_filtradas) // len(marcas_filtradas)
            st.metric("Precio promedio", f"${avg_price:,}")

    with col_stats3:
        categorias_filtradas = len(set(m['categoria'] for m in marcas_filtradas))
        st.metric("Categorías", categorias_filtradas)

    st.success("✨ Búsqueda completada correctamente")


# Inicializar session_state para los botones
if 'initialized' not in st.session_state:
    for i in range(20):  # Suficiente para todas las marcas
        st.session_state[f'enlace_{i}'] = False
    st.session_state.initialized = True

if __name__ == "__main__":
    main()