import os

# Definir a estrutura de diretórios
estrutura = [
    "Bodyx",
    "Bodyx/assets",
    "Bodyx/data/input",
    "Bodyx/data/output",
    "Bodyx/etl",
    "Bodyx/database",
    "Bodyx/modules",
    "Bodyx/logs"
]

# Criar diretórios
for pasta in estrutura:
    os.makedirs(pasta, exist_ok=True)

# Criar arquivos básicos
arquivos = {
    "Bodyx/requirements.txt": "dash\npandas\nsqlalchemy\ntabulate\nopenpyxl\nmariadb",
    "Bodyx/config.py": "# Configurações globais do sistema",
    "Bodyx/run.py": """from app import app

if __name__ == "__main__":
    app.run_server(debug=True)
""",
    "Bodyx/database/db_init.py": "# Script para inicializar o banco de dados",
    "Bodyx/database/connection.py": """from sqlalchemy import create_engine

DATABASE_URI = "mariadb+mariadbconnector://root:@localhost:3306/gecaf"
engine = create_engine(DATABASE_URI)
""",
    "Bodyx/etl/etl.py": "# Script para ETL",
    "Bodyx/modules/dashboard.py": "# Página do dashboard",
    "Bodyx/modules/cnps.py": "# Página de cadastro e edição de CNPs",
    "Bodyx/modules/seguro.py": "# Página de seguros",
    "Bodyx/modules/relatorios.py": "# Página de relatórios",
    "Bodyx/app.py": """import dash
from dash import html

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div("Sistema Seguro CNP - Em Construção")

if __name__ == "__main__":
    app.run_server(debug=True)
"""
}

# Criar arquivos e escrever conteúdos padrão
for arquivo, conteudo in arquivos.items():
    with open(arquivo, "w", encoding="utf-8") as f:
        f.write(conteudo)

print("📂 Estrutura do projeto criada com sucesso!")
