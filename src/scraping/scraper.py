import requests  # Importación del módulo requests para hacer las solicitudes HTTP
from bs4 import BeautifulSoup  # Importación de BeautifulSoup para el análisis HTML
import pandas as pd  # Importación de pandas para trabajar con datos tabulares


def fetch_page(url):
    """
    Función para obtener el contenido de una página web.

    Args:
        url (str): La URL de la página.

    Returns:
        bytes: El contenido de la página en bytes.
    """
    # Realizar la solicitud GET a la URL
    response = requests.get(url)
    # Verificar si la solicitud fue exitosa (código de estado 200)
    if response.status_code == 200:
        # Devolver el contenido de la página
        return response.content
    else:
        # Si la solicitud falla, lanzar una excepción
        raise Exception(f"Failed to fetch page: {url}")


def parse_product(product):
    """
    Función para analizar la información de un producto de la página web.

    Args:
        product (bs4.element.Tag): La etiqueta que contiene la información del producto.

    Returns:
        dict: Un diccionario con la información del producto.
    """
    # Extraer el título del producto
    title = product.find("a", class_="title").text.strip()
    # Extraer la descripción del producto
    description = product.find("p", class_="description").text.strip()
    # Extraer el precio del producto
    price = product.find("h4", class_="price").text.strip()
    # Devolver un diccionario con la información del producto
    return {
        "title": title,
        "description": description,
        "price": price
    }


def scrape(url):
    """
    Función principal para hacer web scraping.

    Args:
        url (str): La URL de la página a scrapear.

    Returns:
        pd.DataFrame: Un DataFrame de pandas con los datos de los productos.
    """
    # Obtener el contenido de la página
    page_content = fetch_page(url)
    # Crear un objeto BeautifulSoup para analizar el contenido HTML
    soup = BeautifulSoup(page_content, "html.parser")
    # Encontrar todos los productos en la página
    products = soup.find_all("div", class_="thumbnail")
    
    # Lista para almacenar la información de los productos
    products_data = []
    # Iterar sobre cada producto encontrado
    for product in products:
        # Analizar la información del producto y agregarla a la lista
        product_info = parse_product(product)
        products_data.append(product_info)
    
    # Convertir la lista de productos a un DataFrame de pandas
    return pd.DataFrame(products_data)


# URL de la página web a scrapear
base_url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/laptops"
# Llamar a la función scrape para obtener los datos de los productos
df = scrape(base_url)
# Imprimir el DataFrame resultante
print(df)
# Guardar los datos en un archivo CSV sin incluir el índice
df.to_csv('data/raw/products.csv', index=False)



# URL de la página web a scrapear
base_url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
# Llamar a la función scrape para obtener los datos de los productos
df = scrape(base_url)
# Imprimir el DataFrame resultante
print(df)
# Guardar los datos en un archivo CSV sin incluir el índice
df.to_csv('data/raw/productstablets.csv', index=False)