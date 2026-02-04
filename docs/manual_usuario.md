# 📘 Manual do Usuário  
## Gerenciador de Tarefas – Python & Streamlit

---

## 📌 Visão Geral
O **Gerenciador de Tarefas** é uma aplicação web desenvolvida em Python com Streamlit, criada para auxiliar na organização e acompanhamento de tarefas do dia a dia.

A aplicação permite cadastrar tarefas, alterar seus status, excluir registros e visualizar métricas e gráficos de progresso em tempo real.

---

## 🖥️ Interface do Sistema
A tela principal do sistema é composta por:

1. Campo de entrada para novas tarefas  
2. Dashboard com métricas gerais  
3. Lista de tarefas cadastradas  
4. Gráfico de progresso (pendentes x concluídas)

A interface utiliza tema escuro para melhor conforto visual.

---

## ➕ Adicionando uma Nova Tarefa

1. Digite a tarefa no campo **“Nova tarefa”**
2. Clique em **Adicionar** ou pressione **Enter**
3. A tarefa será salva automaticamente

⚠️ Tarefas vazias não são permitidas.

---

## 📋 Lista de Tarefas

Cada tarefa exibe:
- Descrição
- Status atual (Pendente ou Concluída)
- Botão de exclusão (🗑️)

### 🔄 Alterar Status
- Utilize o seletor de status abaixo da tarefa
- A atualização é salva automaticamente

### 🗑️ Excluir Tarefa
- Clique no ícone de lixeira
- A tarefa será removida permanentemente

---

## 📊 Dashboard

O dashboard apresenta:
- 📌 Total de tarefas
- ⏳ Tarefas pendentes
- ✅ Tarefas concluídas

Os dados são atualizados em tempo real.

---

## 🥧 Gráfico de Progresso
O gráfico em formato de rosca representa visualmente o progresso geral das tarefas, facilitando o acompanhamento da produtividade.

---

## 💾 Armazenamento de Dados
- Os dados são armazenados localmente utilizando SQLite
- O salvamento é automático
- As tarefas permanecem após reiniciar o sistema

---

## 🚀 Execução do Sistema

```bash
streamlit run src/app.py
