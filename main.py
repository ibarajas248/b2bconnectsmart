import streamlit as st
from streamlit_option_menu import option_menu
import pagina1
import pagina2
import pagina3

# Configurar el menú de navegación en la barra lateral con un tema claro
with st.sidebar:
    selected = option_menu(
        "Menú Principal",
        ["API SECOP II", "RUES", "Buscar proveedor"],
        icons=['house', 'file-earmark', 'search'],
        menu_icon="cast",
        default_index=0,
        styles={
            "container": {
                "padding": "5px",
                "background-color": "#f8f9fa",  # Fondo blanco claro para el contenedor
                "border-radius": "10px"  # Bordes redondeados para el contenedor
            },
            "icon": {
                "color": "#007bff",  # Color azul claro para los íconos
                "font-size": "25px"
            },
            "nav-link": {
                "background-color": "#e9ecef",  # Fondo gris muy claro para los botones
                "color": "#495057",  # Texto gris oscuro para los botones
                "border-radius": "8px",  # Bordes redondeados en los botones
                "font-weight": "bold",  # Negrita en el texto
                "padding": "12px",  # Espaciado dentro de los botones
                "transition": "background-color 0.3s ease",  # Transición suave al pasar el mouse
            },
            "nav-link-selected": {
                "background-color": "#007bff",  # Fondo azul brillante cuando está seleccionado
                "color": "#ffffff",  # Texto blanco cuando está seleccionado
                "border-radius": "8px",  # Bordes redondeados para el botón seleccionado
                "font-weight": "bold",
            },
            "nav-link:hover": {
                "background-color": "#d6d8db",  # Fondo gris más oscuro cuando se pasa el mouse
            }
        }
    )

# Lógica para cargar la página seleccionada
if selected == "API SECOP II":
    pagina1.mostrar_estadisticas()
elif selected == "RUES":
    pagina2.mostrar_estadisticas()
elif selected == "Buscar proveedor":
    pagina3.mostrar_estadisticas()
