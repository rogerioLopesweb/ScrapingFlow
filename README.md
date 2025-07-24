# 🌀 ScrapingFlow

**ScrapingFlow** é uma API moderna e leve desenvolvida com **FastAPI** que permite realizar web scraping estruturado de páginas da web, com foco inicial em **notícias de tecnologia**. O projeto foi criado com o objetivo de oferecer uma base extensível para extração de dados HTML de forma eficiente, leve e compatível com serviços cloud como **Azure App Service** (sem necessidade de Docker).

---

## 🚀 Funcionalidades

- 📄 `/scrape/page` — Extrai o título, todos os parágrafos e links de qualquer página HTML.
- 📰 `/scrape/news` — Extrai o título e o corpo da matéria de notícias online.
- 🔤 Retorno em JSON estruturado e limpo.
- ⚡ Baseado em `requests` + `BeautifulSoup` (sem Selenium).
- 🌐 Compatível com deploy direto em nuvem (ex: Azure App Service, Heroku).

---

## 📦 Tecnologias usadas

- [FastAPI](https://fastapi.tiangolo.com/) — Framework leve e rápido para APIs REST.
- [Pydantic](https://docs.pydantic.dev/) — Validação de dados.
- [Requests](https://docs.python-requests.org/) — Requisições HTTP.
- [BeautifulSoup4](https://www.crummy.com/software/BeautifulSoup/) — Extração de conteúdo HTML.

---

## ⚙️ Como usar

### 1. Instale as dependências

```bash
pip install -r requirements.txt
Ou
pip install fastapi uvicorn requests beautifulsoup4 pydantic

### 2. Inicie o servidor
python -m uvicorn app.main:app --reload
Acesse:
http://localhost:8000/

### 3. Estrutura

ScrapingFlow/
├── app/
│   ├── main.py              # Entrypoint da API
│   ├── scrape_page.py       # Scraper genérico de páginas
│   └── scrape_news.py       # Scraper específico para notícias
├── requirements.txt
├── README.md
└── .gitignore

