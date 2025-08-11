# Banco de Dados Simples

Este projeto implementa uma base de dados simples utilizando estruturas de dados como **Tabela de Hash**, **Árvore B** (parcialmente implementada) e **Merge Sort**. É possível manipular registros diretamente pela **linha de comando**.

## Funcionalidades

- Inserção, busca, atualização e remoção de registros (`id`, `nome`, `idade`)
- Ordenação de registros por qualquer campo usando Merge Sort
- Armazenamento persistente em arquivo JSON
- Interface de linha de comando com comandos diretos

- ##  Estrutura do Projeto
- .
├── data/
│ └── db_file.json # Armazena os registros inseridos
├── app.py # Código principal (interface + lógica)
├── README.md
└── .gitignore

## ▶️ Como Usar
### 1. Executar o programa

```bash
python app.py <COMANDO> [ARGUMENTOS]
Inserir
python app.py INSERT <id> <nome> <idade>
Buscar
python app.py SELECT <id>
Atualizar
python app.py UPDATE <id> <campo> <novo_valor>
Exemplo:
python app.py UPDATE 1 idade 35
Deletar
python app.py DELETE <id>
Ordenar
python app.py SORT <campo>
Exemplo:
python app.py SORT idade

