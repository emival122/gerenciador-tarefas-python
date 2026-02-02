# ui.py
import streamlit as st
import plotly.graph_objects as go
from db import atualizar_status_db, excluir_tarefa_db


def aplicar_css():
    st.markdown("""
    <style>
    .stApp { background:#0f172a; }

    h1, h3, label, span, p {
        color:#e5e7eb !important;
    }

    input, select {
        background:#020617 !important;
        color:#e5e7eb !important;
        border:1px solid #334155 !important;
        border-radius:8px;
        padding:6px;
    }

    .stButton > button {
        background:#2563eb;
        color:white;
        border-radius:8px;
        padding:10px 20px;
        font-weight:600;
        border:none;
    }

    .stButton > button:hover {
        background:#1e40af;
    }

    .task {
        background:#020617;
        padding:14px;
        border-radius:12px;
        border-left:5px solid #2563eb;
        margin-bottom:10px;
        transition: all .25s ease;
    }

    .task:hover {
        transform: translateX(4px);
    }

    .task.done {
        border-left-color:#22c55e;
        opacity:.85;
    }

    .badge {
        padding:4px 10px;
        border-radius:20px;
        font-size:13px;
        font-weight:600;
    }

    .badge.pendente {
        background:#7f1d1d;
        color:#fecaca;
    }

    .badge.concluida {
        background:#14532d;
        color:#bbf7d0;
    }

    .js-plotly-plot {
        background:#020617;
        border-radius:14px;
        padding:10px;
    }
    </style>
    """, unsafe_allow_html=True)


def excluir_tarefa(id):
    excluir_tarefa_db(id)
    # sem mensagem, sem rerun (Streamlit já atualiza)


def render_lista_tarefas(df):
    st.subheader("📋 Lista de Tarefas")

    for _, r in df.iterrows():
        concluida = r.status == "Concluída"

        st.markdown(
            f"""
            <div class="task {'done' if concluida else ''}">
                <b>{r.tarefa}</b><br>
                <span class="badge {'concluida' if concluida else 'pendente'}">
                    {r.status}
                </span>
            </div>
            """,
            unsafe_allow_html=True
        )

        c1, c2 = st.columns([4, 1])

        with c1:
            novo_status = st.selectbox(
                "Status",
                ["Pendente", "Concluída"],
                index=0 if r.status == "Pendente" else 1,
                key=f"status_{r.id}",
                label_visibility="collapsed"
            )

            if novo_status != r.status:
                atualizar_status_db(r.id, novo_status)

        with c2:
            st.button(
                "🗑️",
                key=f"delete_{r.id}",
                on_click=lambda i=r.id: excluir_tarefa(i)
            )


def render_dashboard(df):
    total = len(df)
    pendentes = len(df[df.status == "Pendente"])
    concluidas = len(df[df.status == "Concluída"])

    c1, c2, c3 = st.columns(3)
    c1.metric("📌 Total", total)
    c2.metric("⏳ Pendentes", pendentes)
    c3.metric("✅ Concluídas", concluidas)


def render_grafico(df):
    if df.empty:
        st.info("Nenhuma tarefa cadastrada.")
        return

    pendentes = len(df[df.status == "Pendente"])
    concluidas = len(df[df.status == "Concluída"])

    fig = go.Figure(go.Pie(
        labels=["Pendente", "Concluída"],
        values=[pendentes, concluidas],
        hole=.65,
        marker=dict(colors=["#ef4444", "#22c55e"]),
        textinfo="percent+label"
    ))

    fig.update_layout(
        height=300,
        showlegend=False,
        paper_bgcolor="#020617",
        plot_bgcolor="#020617",
        font=dict(color="#e5e7eb")
    )

    st.plotly_chart(fig, use_container_width=True)
