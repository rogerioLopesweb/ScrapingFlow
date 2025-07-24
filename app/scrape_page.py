import requests
from bs4 import BeautifulSoup

# Função principal que realiza o scraping de uma página HTML
def scrape_page(url: str):
    """
    Realiza a extração (scraping) de uma página web.
    
    Parâmetros:
        url (str): URL da página que será raspada.
    
    Retorna:
        dict: Um dicionário contendo o título da página,
              lista de parágrafos, links encontrados e a própria URL.
    """
    
    # Define cabeçalhos para simular um navegador real
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    # Faz a requisição HTTP para obter o HTML da página
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Lança exceção se houver erro na resposta
     # ⚠️ Força a decodificação correta para evitar caracteres quebrados
    response.encoding = 'utf-8'

    # Faz o parsing do HTML com BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Extrai o título da página, se existir
    title_tag = soup.find("title")
    title = title_tag.get_text(strip=True) if title_tag else "Sem título"

    # Coleta o texto de todos os parágrafos <p>
    paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]

    # Coleta todos os links <a> com atributo href
    links = [a.get("href") for a in soup.find_all("a", href=True)]

    # Retorna os dados estruturados em formato dicionário
    return {
        "title": title,
        "paragraphs": paragraphs,
        "links": links,
        "url": url
    }
