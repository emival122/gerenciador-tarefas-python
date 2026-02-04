# main.py
import streamlit as st
from db import carregar_tarefas, adicionar_tarefa_db
from ui import aplicar_css, render_lista_tarefas, render_dashboard, render_grafico

st.set_page_config(
    page_title="Gerenciamento de Tarefas",
    page_icon="📋",
    layout="wide"
)

aplicar_css()

z
def adicionar():
    texto = st.session_state.entrada.strip()

    if not texto:
        st.toast("⚠️ Digite uma tarefa antes de adicionar.", icon="⚠️")
        return

    adicionar_tarefa_db(texto)
    st.session_state.entrada = ""


st.title("📋 Gerenciamento de Tarefas")

col_i, col_b = st.columns([5, 1])

with col_i:
    st.text_input(
        "Nova tarefa",
        key="entrada",
        placeholder="Digite a tarefa e pressione Enter"
    )

with col_b:
    st.button("Adicionar", on_click=adicionar)


dados = carregar_tarefas()

render_dashboard(dados)

col_esq, col_dir = st.columns([1.8, 1])
with col_esq:
    render_lista_tarefas(dados)

with col_dir:
    st.subheader("📊 Progresso")
    render_grafico(dados)
