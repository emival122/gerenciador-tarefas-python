# 📄 Documentação Técnica  
## Gerenciador de Tarefas – Python & Streamlit

---

## 📌 Visão Técnica Geral
O **Gerenciador de Tarefas** é uma aplicação web desenvolvida em Python utilizando o framework **Streamlit**.  
O projeto foi estruturado de forma modular, separando interface, lógica de aplicação e persistência de dados, facilitando manutenção, escalabilidade e leitura do código.

---

## 🧱 Arquitetura do Projeto

A arquitetura segue um padrão simples de separação de responsabilidades:

```text
src/
├── app.py        # Ponto de entrada da aplicação
├── ui.py         # Interface, CSS e gráficos
├── db.py         # Persistência de dados (SQLite)
└── __init__.py
