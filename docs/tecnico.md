# 💻 Documentação Técnica (Developer Docs)

Manual destinado a desenvolvedores para manutenção, entendimento da arquitetura e evolução do software **Gerenciador de Tarefas**.

---

## 🏗️ Arquitetura
O projeto utiliza um padrão de separação de responsabilidades entre interface, lógica de aplicação e persistência de dados.

1. **`src/app.py`**  
   Contém o fluxo principal da aplicação Streamlit, configuração da página e orquestração dos componentes.

2. **`src/ui.py`**  
   Responsável pela interface do usuário, estilização com CSS e renderização de gráficos e componentes visuais.

3. **`src/db.py`**  
   Camada de persistência, responsável pelo acesso ao banco de dados SQLite e pelas operações CRUD.

---

## 🧩 Detalhes dos Módulos

### Módulo de Aplicação (`app.py`)
- Inicializa a aplicação Streamlit (`st.set_page_config`).
- Controla o estado da aplicação via `st.session_state`.
- Integra os módulos de interface e banco de dados.
- Gerencia eventos de criação de tarefas.

---

### Módulo de Interface (`ui.py`)
- Aplica CSS customizado utilizando `st.markdown`.
- Renderiza a lista de tarefas com HTML embutido.
- Exibe métricas gerais através de `st.metric`.
- Gera gráficos interativos com **Plotly**.

#### Gráfico de Progresso
- Implementado com `plotly.graph_objects.Pie`.
- Utiliza gráfico de rosca (`hole=0.65`).
- Atualizado dinamicamente conforme o estado das tarefas.

---

### Módulo de Persistência (`db.py`)
Utiliza **SQLite** como banco de dados local.

Funções principais:
- Criação automática da tabela de tarefas.
- Inserção de novas tarefas.
- Atualização do status.
- Exclusão de registros.
- Consulta ordenada por status e ID.

Estrutura da tabela:

```sql
tarefas (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  tarefa TEXT NOT NULL,
  status TEXT NOT NULL
)
