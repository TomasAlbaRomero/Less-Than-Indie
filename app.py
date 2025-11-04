# app.py - Versión con fondo violeta oscuro
import streamlit as st

# Configuración de la página con diseño personalizado
st.set_page_config(
    page_title="Less Than Indie",
    page_icon="👕",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personalizado con fondo violeta oscuro
st.markdown("""
<style>
    /* Fondo general VIOLETA OSCURO */
    .stApp {
        background: linear-gradient(135deg, #2d1b69 0%, #1a1033 100%) !important;
    }

    /* Fondo del contenido principal - blanco con sombra */
    .main .block-container {
        background: rgba(255, 255, 255, 0.95);
        border-radius: 15px;
        padding: 2rem;
        margin-top: 2rem;
        margin-bottom: 2rem;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        border: 1px solid #e0e0e0;
    }

    /* Fondo del sidebar VIOLETA OSCURO */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #3d2a7a 0%, #2a1a52 100%) !important;
    }

    /* TODOS los textos del sidebar en BLANCO */
    section[data-testid="stSidebar"] * {
        color: #ffffff !important;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3,
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] div,
    section[data-testid="stSidebar"] span,
    section[data-testid="stSidebar"] label {
        color: #ffffff !important;
        font-weight: 500;
    }

    /* Inputs del sidebar con texto blanco y fondo violeta claro */
    section[data-testid="stSidebar"] .stTextInput input {
        color: #ffffff !important;
        background: rgba(255, 255, 255, 0.15) !important;
        border: 2px solid rgba(255, 255, 255, 0.4) !important;
        border-radius: 8px !important;
    }

    section[data-testid="stSidebar"] .stTextInput input::placeholder {
        color: rgba(255, 255, 255, 0.7) !important;
    }

    /* Selectbox del sidebar */
    section[data-testid="stSidebar"] .stSelectbox select {
        color: #ffffff !important;
        background: rgba(255, 255, 255, 0.15) !important;
        border: 2px solid rgba(255, 255, 255, 0.4) !important;
        border-radius: 8px !important;
    }

    /* Number inputs del sidebar */
    section[data-testid="stSidebar"] .stNumberInput input {
        color: #ffffff !important;
        background: rgba(255, 255, 255, 0.15) !important;
        border: 2px solid rgba(255, 255, 255, 0.4) !important;
        border-radius: 8px !important;
    }

    /* Labels de los inputs */
    section[data-testid="stSidebar"] .stTextInput label,
    section[data-testid="stSidebar"] .stSelectbox label,
    section[data-testid="stSidebar"] .stNumberInput label {
        color: #ffffff !important;
        font-weight: 600 !important;
    }

    /* Botones del sidebar - violeta más claro */
    section[data-testid="stSidebar"] .stButton button {
        background: linear-gradient(45deg, #6d5bbd, #5a4aa3) !important;
        color: white !important;
        border: none !important;
        border-radius: 25px !important;
        padding: 0.5rem 2rem !important;
        font-weight: bold !important;
    }

    section[data-testid="stSidebar"] .stButton button:hover {
        background: linear-gradient(45deg, #5a4aa3, #4a3a8a) !important;
        transform: scale(1.05) !important;
    }

    /* Alertas/info del sidebar */
    section[data-testid="stSidebar"] .stAlert {
        background: rgba(255, 255, 255, 0.15) !important;
        border: 1px solid rgba(255, 255, 255, 0.3) !important;
        color: #ffffff !important;
    }

    /* Opciones del dropdown en blanco */
    section[data-testid="stSidebar"] option {
        color: #000000 !important;
        background: white !important;
    }

    /* Títulos y textos del contenido principal */
    .main h1, .main h2, .main h3 {
        color: #2d1b69 !important;
        font-family: 'Arial', sans-serif;
        font-weight: 600;
    }

    .main p, .main div, .main span, .main label {
        color: #333333 !important;
    }

    .main h1 {
        border-bottom: 3px solid #6d5bbd;
        padding-bottom: 10px;
        color: #2d1b69 !important;
    }

    /* Tarjetas de marcas con fondo blanco */
    .stContainer {
        background: #ffffff;
        border-radius: 10px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 5px solid #6d5bbd;
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        transition: transform 0.3s ease;
        border: 1px solid #e8e8e8;
    }

    .stContainer:hover {
        transform: translateY(-3px);
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    }

    /* Botones del contenido principal - violeta */
    .stButton button {
        background: linear-gradient(45deg, #6d5bbd, #5a4aa3);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: bold;
        transition: all 0.3s ease;
    }

    .stButton button:hover {
        transform: scale(1.05);
        box-shadow: 0 5px 15px rgba(109, 91, 189, 0.4);
        background: linear-gradient(45deg, #5a4aa3, #4a3a8a);
    }

    /* Inputs y selects del contenido principal */
    .stTextInput input, .stSelectbox select {
        border-radius: 10px;
        border: 2px solid #d0d0d0;
        background: white;
        color: #333333;
    }

    .stTextInput input:focus, .stSelectbox select:focus {
        border-color: #6d5bbd;
        box-shadow: 0 0 0 2px rgba(109, 91, 189, 0.2);
    }

    /* Mejorar contraste en números de precio */
    .stNumberInput input {
        border-radius: 10px;
        background: white;
        color: #333333;
        border: 2px solid #d0d0d0;
    }

    /* Mejorar contraste en los mensajes */
    .stAlert {
        background: rgba(255, 255, 255, 0.95);
        border: 1px solid #e0e0e0;
    }

    /* Links más visibles - violeta */
    a {
        color: #6d5bbd !important;
        font-weight: 500;
    }

    a:hover {
        color: #5a4aa3 !important;
    }

    /* Mejorar el expander */
    .streamlit-expanderHeader {
        background: #f8f9fa;
        border: 1px solid #e0e0e0;
        border-radius: 8px;
        color: #333333;
        font-weight: 600;
    }

    /* Separadores más visibles */
    hr {
        border-color: #6d5bbd !important;
        opacity: 0.3;
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
    # Header de la aplicación con mejor diseño
    col1, col2 = st.columns([3, 1])

    with col1:
        st.title("👕 Less Than Indie")
        st.markdown("### 🎯 Descubre marcas de ropa alternativa y sostenible")
        st.markdown("**Encuentra tu estilo único con marcas independientes argentinas**")

    with col2:
        st.markdown("")
        st.markdown("")
        st.markdown("🛍️ **Tu tienda de moda alternativa**")

    st.markdown("---")

    # Cargar datos
    marcas = cargar_datos()

    # Sidebar con filtros - fondo violeta oscuro
    with st.sidebar:
        st.markdown("### 🔍 Filtros de Búsqueda")
        st.markdown("---")

        # Filtro por nombre
        busqueda = st.text_input(
            "**Buscar por nombre:**",
            value="",
            key="busqueda_input_unique_123",
            placeholder="Ej: 0800spice, Pancha..."
        )

        # Filtro por categoría
        todas_categorias = list(set(marca['categoria'] for marca in marcas))
        todas_categorias.sort()
        opciones_categoria = ["Todas"] + todas_categorias
        categoria = st.selectbox(
            "**Categoría:**",
            opciones_categoria,
            key="categoria_select_unique_123"
        )

        # Filtro por precio
        st.markdown("**💰 Rango de precios:**")
        todos_precios = [marca['precio'] for marca in marcas]
        col_precio1, col_precio2 = st.columns(2)
        with col_precio1:
            precio_min = st.number_input(
                "Mínimo:",
                min_value=0,
                value=min(todos_precios),
                step=1000,
                key="precio_min_unique_123"
            )
        with col_precio2:
            precio_max = st.number_input(
                "Máximo:",
                min_value=0,
                value=max(todos_precios),
                step=1000,
                key="precio_max_unique_123"
            )

        # Ordenamiento
        orden = st.selectbox(
            "**📊 Ordenar por precio:**",
            ["Sin orden", "Menor a mayor", "Mayor a menor"],
            key="orden_select_unique_123"
        )

        # Info de búsqueda
        if busqueda.strip():
            st.info(f"**Buscando:** '{busqueda}'")

    # Aplicar filtros
    marcas_filtradas = []

    for marca in marcas:
        if busqueda.strip() != "":
            if busqueda.lower() not in marca['nombre'].lower():
                continue

        if categoria != "Todas":
            if marca['categoria'] != categoria:
                continue

        if marca['precio'] < precio_min or marca['precio'] > precio_max:
            continue

        marcas_filtradas.append(marca)

    # Ordenar resultados
    if orden == "Menor a mayor":
        marcas_filtradas.sort(key=lambda x: x['precio'])
    elif orden == "Mayor a menor":
        marcas_filtradas.sort(key=lambda x: x['precio'], reverse=True)

    # Mostrar resultados con diseño mejorado
    st.subheader(f"📦 Marcas Encontradas: {len(marcas_filtradas)}")

    if len(marcas_filtradas) == 0:
        st.warning("🚫 No se encontraron marcas con los filtros seleccionados.")
        st.info("💡 **Sugerencias:** Prueba con '0800spice', 'Pancha community', o 'KAZARIAN'")
        return

    # Mostrar cada marca encontrada con diseño de tarjeta
    for i, marca in enumerate(marcas_filtradas):
        # Usar container para cada marca con estilo personalizado
        with st.container():
            # Aplicar estilo CSS personalizado al container
            st.markdown(
                f"""
                <div style='
                    background: #ffffff; 
                    border-radius: 10px; 
                    padding: 1.5rem; 
                    margin: 1rem 0; 
                    border-left: 5px solid #6d5bbd; 
                    box-shadow: 0 4px 12px rgba(0,0,0,0.15);
                    transition: transform 0.3s ease;
                    border: 1px solid #e8e8e8;
                '>
                """,
                unsafe_allow_html=True
            )

            st.markdown(f"### 🏷️ {marca['nombre']}")

            col_info, col_accion = st.columns([3, 1])

            with col_info:
                st.markdown(f"**📝 Descripción:** {marca['descripcion']}")
                st.markdown(f"**📍 Ubicación:** {marca['ubicacion']}")
                st.markdown(f"**🎯 Categoría:** {marca['categoria'].capitalize()}")
                st.markdown(f"**💵 Precio:** ${marca['precio']: ,}")

            with col_accion:
                st.markdown("")  # Espacio
                st.markdown("")  # Espacio
                if st.button(f"🛒 Comprar", key=f"comprar_{i}"):
                    st.markdown(f"🔗 **[Ir a la tienda →]({marca['enlace_compra']})**")

            # Cerrar el div personalizado
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("---")

    # Tabla resumen en expander
    with st.expander("📊 Ver resumen completo de marcas"):
        st.write("**Lista detallada de marcas encontradas:**")
        for i, marca in enumerate(marcas_filtradas, 1):
            st.write(f"{i}. **{marca['nombre']}** - 💵 ${marca['precio']: ,} - 🏷️ {marca['categoria'].capitalize()}")


if __name__ == "__main__":
    main()