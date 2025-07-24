import requests
from bs4 import BeautifulSoup

# Função que realiza o scraping de uma notícia online
def scrape_news(url: str) -> dict:
    """
    Realiza a raspagem de uma página de notícia (URL) e extrai:
    - Título principal (geralmente em uma tag <h1>)
    - Texto completo (todos os parágrafos <p>)
    - A URL original
    
    Parâmetros:
        url (str): URL da notícia a ser processada.
    
    Retorna:
        dict: Dicionário com título, texto da notícia e URL.
    """

    # Define cabeçalhos HTTP para simular um navegador real
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # Tenta fazer a requisição HTTP para obter o HTML da página
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Gera erro se o status HTTP for >= 400
         # ⚠️ Força a decodificação correta para evitar caracteres quebrados
        response.encoding = 'utf-8'
    except requests.RequestException:
        # Retorna erro estruturado caso a página esteja inacessível
        return {
            "title": "Erro ao acessar a URL",
            "text": "",
            "url": url
        }

    # Faz o parsing do conteúdo HTML usando BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Procura o título principal da notícia (geralmente está em uma tag <h1>)
    title_tag = soup.find("h1")
    title = title_tag.get_text(strip=True) if title_tag else "Título não encontrado"

    # Extrai o conteúdo de todos os parágrafos <p> da página
    paragraphs = soup.find_all("p")
    text = "\n".join(
        p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True)
    )

    # Retorna os dados estruturados
    return {
        "title": title,
        "text": text,
        "url": url
    }
