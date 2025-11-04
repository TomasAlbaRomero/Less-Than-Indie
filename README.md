# Less-Than-Indie
##  Descripción general
Less Than Indie es una plataforma web que permite a los usuarios descubrir marcas de ropa alternativa de bajo y mediano perfil. 
Los usuarios podrán buscar marcas por nombre, marca , precios (de mayor a menos y viceversa) o categoría de prendas de ropa, y ver información básica de cada una.

---

## Objetivo principal
Facilitar la búsqueda y descubrimiento de marcas independientes o sostenibles que no son tan conocidas.

---

##  Tipos de usuario
- **Visitante:** Puede buscar y explorar marcas sin iniciar sesión.
- (Opcional en el futuro) **Usuario registrado:** Puede guardar marcas favoritas.

---

##  Funcionalidades principales
1.**Buscador de marcas:** nombre.
2. **Filtros:** rango de precios, tipo de prenda.
3. **Listado de resultados:** mostrar tarjetas con:
   - Nombre de la marca  
   - Descripción breve  
   - opcion de compra dentro de la app  
   - Redes sociales (si existen)
4. **Página de detalles (opcional):** información ampliada de cada marca.

---

## 💾 Datos necesarios
Cada marca debería tener los siguientes campos:
- `nombre`: Nombre de la marca.
- `descripcion`: Breve resumen de lo que ofrece.
- `ubicacion`: lugar de origen.
- `Enlace de compra`: Enlace de compra.
- `precio`: precio exacto.
- `categoria`: remeras, pantalones, buzos, polleras, vestidos, accesorios.

---

## 🎨 Interfaz (Streamlit)
- Un título con el nombre de la app.
- Un campo de búsqueda.
- Una lista de resultados en tarjetas.
- Filtros (selectores desplegables).
- Posible página de detalles o pop-up con más info.

---

## 🚀 Futuras mejoras
- Sistema de favoritos.
- Registro de usuarios.
- Recomendaciones automáticas.
- Integración con APIs de moda.

