from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from app.scrape_page import scrape_page  # Importa função de scraping genérico
from app.scrape_news import scrape_news  # Importa função de scraping específico de notícia

# Cria a instância principal do aplicativo FastAPI
app = FastAPI()

# Define o modelo de dados que a API espera no corpo da requisição
class URLRequest(BaseModel):
    url: str  # A URL a ser processada

# Endpoint para scraping genérico de qualquer página HTML
@app.post("/scrape/page")
def extract_content(request: URLRequest):
    """
    Endpoint que extrai título, parágrafos e links de qualquer página.
    
    Exemplo de entrada:
    {
        "url": "https://exemplo.com"
    }
    """
    try:
        content = scrape_page(request.url)
        return content
    except Exception as e:
        # Se ocorrer algum erro, retorna um erro HTTP 500 com detalhe
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint para scraping específico de notícias
@app.post("/scrape/news")
def extract_news(request: URLRequest):
    """
    Endpoint que extrai título e corpo do texto de uma notícia.
    
    Exemplo de entrada:
    {
        "url": "https://g1.globo.com/tecnologia/noticia/2025/07/23/exemplo.html"
    }
    """
    try:
        content = scrape_news(request.url)
        return content
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
