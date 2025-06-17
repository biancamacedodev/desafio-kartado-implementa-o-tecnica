# 💼 Desafio Técnico – Kartado (Implementação Técnica)

Solução desenvolvida para o processo seletivo da Kartado — vaga de Estágio em Implementação Técnica.

---

## 📌 Descrição

O desafio foi dividido em **duas partes**:

### ✅ Parte 1 – Estrutura de Formulário em JSON

Criação de um formulário técnico com os seguintes campos:
- Código de Identificação
- Comprimento (m)
- Largura (m)
- Espessura (cm)
- Área (m²) → calculada automaticamente com JSONLogic
- Volume (m³) → calculado automaticamente com JSONLogic
- Observações

A estrutura foi organizada em JSON, seguindo o padrão:
```json
{
  "id": 1,
  "displayName": "Nome do Campo",
  "apiName": "nome_api",
  "dataType": "string" | "float",
  "logic": { ... } // opcional, usado nos cálculos
}
```

### ✅ Parte 2 – Função Python para Adicionar Campos

Função desenvolvida em Python que:
- Recebe um dicionário com o formulário e um campo novo
- Insere o campo **no início da lista**
- Atribui um `id` único e sequencial automaticamente
- Retorna o formulário atualizado

---

## 📁 Arquivos

| Nome do arquivo              | Descrição |
|-----------------------------|-----------|
| `formulario_kartado.json`   | Estrutura inicial do formulário |
| `adicionar_campo_kartado.py`| Script com a função para adicionar novos campos |
---

## 🛠️ Como executar

Requisitos: Python 3+

```bash
python3 adicionar_campo_kartado.py
```

O script exibirá no terminal o formulário atualizado com o novo campo inserido.

---

## 💡 Melhorias sugeridas

- Validação de campos obrigatórios antes de inserção
- Evolução para uma API com Flask/FastAPI
- Integração futura com interface gráfica para usuários
