# db.py
import sqlite3
import pandas as pd

DB_NAME = "tarefas.db"


def conectar_bd():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tarefa TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)
    conn.commit()
    return conn


def carregar_tarefas():
    with conectar_bd() as conn:
        df = pd.read_sql_query("""
            SELECT *
            FROM tarefas
            ORDER BY
                CASE status
                    WHEN 'Pendente' THEN 0
                    ELSE 1
                END,
                id DESC
        """, conn)
    return df


def adicionar_tarefa_db(tarefa: str):
    if not tarefa.strip():
        return
    with conectar_bd() as conn:
        conn.execute(
            "INSERT INTO tarefas (tarefa, status) VALUES (?, ?)",
            (tarefa.strip(), "Pendente")
        )


def atualizar_status_db(id: int, status: str):
    with conectar_bd() as conn:
        conn.execute(
            "UPDATE tarefas SET status=? WHERE id=?",
            (status, id)
        )


def excluir_tarefa_db(id: int):
    with conectar_bd() as conn:
        conn.execute(
            "DELETE FROM tarefas WHERE id=?",
            (id,)
        )
