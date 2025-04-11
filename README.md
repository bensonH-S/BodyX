# BodyX - Sistema de Gerenciamento para Loja de Suplementos

## Visão Geral
**BodyX** é um sistema web desenvolvido para otimizar a gestão de lojas de suplementos. Com uma interface intuitiva e funcionalidades robustas, o BodyX ajuda a gerenciar vendas, estoque, clientes e relatórios, permitindo que você foque no crescimento do seu negócio.

O BodyX é uma aplicação construída com [Dash](https://dash.plotly.com/), uma biblioteca Python para criação de interfaces web interativas. Ele integra ferramentas de ETL (Extract, Transform, Load) para processamento de dados, conexão com banco de dados (MariaDB) e módulos personalizados para atender às necessidades específicas de uma loja de suplementos.

## Funcionalidades (Planejadas)
* **Dashboard**: Visualização de métricas-chave, como vendas, estoque e desempenho.
* **Gestão de CNPs**: Cadastro e edição de clientes ou parceiros (em desenvolvimento).
* **Seguros**: Gerenciamento de apólices ou garantias relacionadas (em desenvolvimento).
* **Relatórios**: Geração de relatórios personalizados para análise de negócios.
* **Processamento de Dados**: Importação e tratamento de dados via ETL para integração com planilhas ou outros sistemas.

## Estrutura do Projeto

```plaintext
BodyX/
├── app.py                  # Arquivo principal da aplicação Dash
├── requirements.txt        # Lista de dependências
├── config.py               # Configurações globais
├── run.py                  # Script para iniciar a aplicação
├── assets/                 # Arquivos estáticos (CSS, imagens, etc.)
├── data/                   # Dados de entrada e saída
│   ├── input/             # Arquivos de entrada (Excel, CSV)
│   ├── output/            # Arquivos gerados (logs, exportações)
├── etl/                    # Processamento de dados
│   ├── etl.py             # Script ETL principal
├── database/               # Banco de dados
│   ├── db_init.py         # Inicialização do banco
│   ├── connection.py      # Conexão com o banco
├── modules/                # Componentes modulares
│   ├── dashboard.py       # Página do dashboard
│   ├── cnps.py           # Cadastro e edição de CNPs
│   ├── seguro.py         # Gestão de seguros
│   ├── relatorios.py     # Relatórios
├── logs/                   # Logs da aplicação
└── venv/                   # Ambiente virtual
