import streamlit as st

st.set_page_config(
    page_title="ANMAT — Cosméticos y Perfumes",
    page_icon="🧴",
    layout="centered"
)

NOTEBOOK_URL = "https://notebooklm.google.com/notebook/f410bdf4-992a-40e7-8f20-4ac2d7c8beec"

st.title("🧴 ANMAT — Cosméticos y Perfumes")
st.markdown("---")
st.markdown(
    """
    Consultá normativa y procedimientos de **ANMAT** para la importación de 
    cosméticos y perfumes, en base a fuentes oficiales verificadas.
    """
)
st.markdown("### ¿Qué podés consultar?")
col1, col2 = st.columns(2)
with col1:
    st.markdown(
        """
        - 📄 Resolución 155/98 — norma base  
        - 📋 Aviso de importación en TAD (Disp. 4033/2025)  
        - 🏗️ Habilitación de establecimientos (Disp. 7939/2025)  
        - 🏷️ Rotulado y nomenclatura INCI  
        """
    )
with col2:
    st.markdown(
        """
        - ⚗️ Sustancias permitidas, restringidas y prohibidas  
        - ⚖️ Cosmético vs. medicamento — criterios ANMAT  
        - 📦 Exportación y Certificado de Libre Venta  
        - 🌎 Marco normativo MERCOSUR  
        """
    )
st.markdown("---")
st.info(
    "💡 **Tip:** Podés hacer preguntas concretas como: "
    "*¿Cuánto tiempo tengo para presentar el Aviso TAD tras nacionalizar la mercadería?*, "
    "*¿Qué documentos exige ANMAT para importar cosméticos?*, "
    "*¿Cuándo un cosmético pasa a ser medicamento?*"
)
st.markdown("### Acceder al asistente")
st.markdown(
    """
    El asistente se abre en una nueva pestaña. 
    Necesitás una cuenta de **Google (Gmail)** para acceder.
    """
)
st.link_button(
    label="🚀 Abrir asistente ANMAT",
    url=NOTEBOOK_URL,
    use_container_width=True,
    type="primary",
)
st.markdown("---")
st.caption("Fuentes: Res. 155/98 · Disp. 4033/2025 · Disp. 7939/2025 · Instructivos ANMAT · Resoluciones GMC MERCOSUR · Normativa de sustancias e ingredientes")
