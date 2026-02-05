# 📖 Guia do Usuário – Gerenciador de Tarefas

Este manual orienta como utilizar o sistema **Gerenciador de Tarefas** para criação, acompanhamento e conclusão de tarefas, com visualização de métricas e gráficos de progresso.

---

## 🛠️ Primeiros Passos
Ao abrir o sistema, você verá uma interface dividida em quatro partes principais: **Cadastro de Tarefas**, **Dashboard**, **Lista de Tarefas** e **Gráfico de Progresso**.

---

### 1. Cadastro de Tarefas
No topo da tela, localize o campo **Nova tarefa**.

- Digite a descrição da tarefa que deseja adicionar.
- Clique no botão **Adicionar** ou pressione **Enter**.

⚠️ O sistema não permite o cadastro de tarefas vazias.

---

### 2. Visualizando as Tarefas
As tarefas cadastradas aparecem na **Lista de Tarefas**, exibindo:

- **Descrição da tarefa**
- **Status atual**:
  - Pendente
  - Concluída
- **Botão de exclusão (🗑️)**

As tarefas pendentes são exibidas com destaque visual diferente das concluídas.

---

### 3. Alterando o Status
Para atualizar o andamento de uma tarefa:

- Utilize o seletor de status abaixo da tarefa.
- Escolha entre **Pendente** ou **Concluída**.
- A alteração é salva automaticamente no sistema.

---

### 4. Excluindo uma Tarefa
Caso deseje remover uma tarefa:

- Clique no ícone de **lixeira (🗑️)**.
- A tarefa será excluída permanentemente do sistema.

---

### 5. Dashboard de Métricas
O painel **Dashboard** exibe um resumo geral:

- 📌 Total de tarefas cadastradas
- ⏳ Quantidade de tarefas pendentes
- ✅ Quantidade de tarefas concluídas

Os valores são atualizados automaticamente a cada ação do usuário.

---

### 6. Gráfico de Progresso
O **Gráfico de Progresso**, exibido à direita da tela, apresenta visualmente:

- A proporção de tarefas pendentes
- A proporção de tarefas concluídas

Esse gráfico facilita o acompanhamento da produtividade ao longo do tempo.

---

## 💾 Salvamento de Dados
- O sistema utiliza **SQLite** para armazenar as tarefas.
- Os dados são salvos automaticamente.
- As tarefas permanecem disponíveis mesmo após fechar a aplicação.

---

## ▶️ Execução do Sistema
Para executar o sistema localmente, utilize o comando:

```bash
streamlit run src/app.py
