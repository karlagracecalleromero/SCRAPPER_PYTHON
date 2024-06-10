# Scraping Web de Productos.

Este proyecto realiza scraping de datos de productos de un sitio web, limpia y analiza loo datos, y los guarda en archivos CSV.

## Requisitos.

- Python 3.7+
- pandas
- beautifulsoup4
- requests
- matplotlib
- time
- logging

## Instalacion.

Para instalar las dependencias creamos un archivo "txt" el cual guardamos todas las dependecias para una rapida instalacion.
Su metodo de uso es utilizando PIP y es con el comando siguiente.

````bash
pip install -r .\dep.txt
````

## Estructura de las carpetas.

````bash
final-boss
|-- data/
|    |- raw/
|    |    |__ products.csv
|    |- processed/
|        |__ cleaned_products.csv    
|
|-- notebooks/
|    |__ exploration.ipynb
|
|-- src/
|    |- analysis/
|        |__ __init__.py
|        |__ analysis.py
|    |- decorators/
|        |__ __init__.py
|        |__ decorators.py
|    |- scraping/
|        |__ __init__.py
|        |__ scraper.py
|__ dep.txt
|__ README.md
|__ requirements.txt    
````

## Ejecucion del Scraper.

Para ejecutar el scraper lo que hay que realizar es.

````bash
python .\src\scraping\scraper.py
````

Esto nos va a generar un CSV en la carpeta "RAW" dentro de la carpeta "DATA" llamado "products.csv"

## Ejecucion para el analisis de datos.

Para ejecutar el script para analisis de datos lo que hay que realizar es.

````bash
python .\src\analisis\analisys.py
 python -m src.analisis.analisys

````

## Realiza análisis de los datos mostrando:
- Estadísticas descriptivas
- Productos con los precios más altos
- Matriz de correlación entre variables numéricas
- Precios mínimos y máximos
- Rango de precios
- Desviación estándar de precios
- Coeficiente de variación de precios
## Permite seleccionar diferentes tipos de análisis para visualizar los resultados en una interfaz gráfica.

Corre el programa con la siguiente linea del codigo donde se te abre una interfaz gráfica: 
````bash
 python -m src.analisis.analisys

````

Esto nos va a generar un CSV en la carpeta "PROCESSED" dentro de la carpeta "DATA" llamado "cleaned_products.csv" o "cleaned_products_tablets.csv"

Dependiendo a la opción que se escoga "Opcio 1: Laptops" o "Opcion 2: Tablets"
!["Interfaz gráfica"]("EntornoGui.png")

## Notebooks
Además, el proyecto cuenta con dos archivos de Jupyter Notebook (exploration.ipynb y explorationplotly.ipynb), que permiten visualizar los datos obtenidos de la página scrapeada. En estos notebooks, se utilizan gráficos de Plotly para mostrar histogramas y estadísticas como máximo, mínimo y porcentajes.

#### Karla Grace Calle Romero
#### karlagracecalleromero@hotmail.com