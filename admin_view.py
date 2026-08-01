
import streamlit as st
from config import TEMPLATE_TXT
from services import extrair_texto_de_arquivo, gerar_template_word_bytes

st.title("Painel de Administração - Base de Conhecimento")

st.subheader("Baixar Modelos de Template")
col1, col2 = st.columns(2)
with col1:
    st.download_button("Baixar Modelo (.txt)", data=TEMPLATE_TXT, file_name="template_cursos.txt", use_container_width=True)
with col2:
    buffer_docx = gerar_template_word_bytes()
    st.download_button(" Baixar Modelo (.docx)", data=buffer_docx, file_name="template_cursos.docx", use_container_width=True)

st.divider()

arquivo_enviado = st.file_uploader("Envie o edital/arquivo oficial (.pdf, .txt ou .docx):", type=["txt", "pdf", "docx"])

if arquivo_enviado:
    texto_extraido = extrair_texto_de_arquivo(arquivo_enviado)
    st.session_state["base_conhecimento_extra"] = texto_extraido
    st.success(f"Arquivo **'{arquivo_enviado.name}'** carregado na memória!")
    st.info(f"Caracteres extraídos: {len(texto_extraido)}")

if "base_conhecimento_extra" in st.session_state:
    if st.button("Remover Base Adicional"):
        del st.session_state["base_conhecimento_extra"]
        st.success("Base removida.")
        st.rerun()