import pandas as pd
import os
from src.decorations.decorators import timeit, logit
import tkinter as tk
from tkinter import scrolledtext

# Decorador logit para registrar información sobre la función
# Decorador timeit para medir el tiempo de ejecución de la función
@logit
@timeit
def load_data(data_path):
    """
    Carga los datos desde un archivo CSV o Excel.
    
    Args:
        data_path (str): La ruta del archivo de datos.
    
    Returns:
        pd.DataFrame: DataFrame con los datos cargados.
    """
    if data_path.endswith(".csv"):
        df = pd.read_csv(data_path)
    elif data_path.endswith(".xlsx"):
        df = pd.read_excel(data_path)
    else:
        raise ValueError("Unsupported file format")
    
    print("Data loaded successfully")
    return df

@logit
@timeit
def clean_data(df):
    """
    Limpia los datos eliminando caracteres no deseados y convirtiendo la columna 'price' a tipo float.
    
    Args:
        df (pd.DataFrame): El DataFrame de pandas con los datos.
    
    Returns:
        pd.DataFrame: DataFrame con los datos limpios.
    """
    df["price"] = df["price"].replace(r"[\$,]", "", regex=True).astype(float)
    print("Data cleaned successfully")
    return df

@logit
@timeit
def analyze_data(df):
    """
    Realiza un análisis de los datos mostrando estadísticas descriptivas, los productos con los precios más altos,
    la matriz de correlación entre las variables numéricas, precios mínimos, precios máximos, rango de precios,
    desviación estándar de precios y coeficiente de variación de precios.
    
    Args:
        df (pd.DataFrame): El DataFrame de pandas con los datos.
    
    Returns:
        dict: Diccionario con los resultados del análisis en diferentes categorías.
    """
    analysis_results = {}

    analysis_results["Basic Data Analysis"] = df.describe().to_string()
    
    highest_prices = df.nlargest(5, "price")
    analysis_results["Products with highest prices"] = highest_prices.to_string()
    
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    correlation_matrix = numeric_df.corr()
    analysis_results["Correlation Matrix"] = correlation_matrix.to_string()
    
    min_price = df["price"].min()
    max_price = df["price"].max()
    analysis_results["Minimum and Maximum Prices"] = f"Minimum Price: {min_price}\nMaximum Price: {max_price}"
    
    price_range = max_price - min_price
    analysis_results["Price Range"] = f"Price Range: {price_range}"
    
    std_dev_price = df["price"].std()
    analysis_results["Standard Deviation of Prices"] = f"Standard Deviation of Prices: {std_dev_price}"
    
    coeff_var_price = std_dev_price / df["price"].mean()
    analysis_results["Coefficient of Variation of Prices"] = f"Coefficient of Variation of Prices: {coeff_var_price}"
    
    analysis_results["Datos"]= df
    
    return analysis_results

@logit
@timeit
def save_clean_data(df, output_path):
    """
    Guarda los datos limpios en un archivo CSV o Excel.
    
    Args:
        df (pd.DataFrame): El DataFrame de pandas con los datos limpios.
        output_path (str): La ruta del archivo de salida.
    """
    if output_path.endswith(".csv"):
        df.to_csv(output_path, index=False)
    elif output_path.endswith(".xlsx"):
        df.to_excel(output_path, index=False)
    else:
        raise ValueError("Unsupported file format")
    
    print(f"Clean data saved to {output_path}")

def show_analysis_results(result_key):
    """
    Muestra los resultados del análisis seleccionados en el Text widget.
    
    Args:
        result_key (str): La clave del análisis a mostrar.
    """
    text_area.config(state=tk.NORMAL)
    text_area.delete(1.0, tk.END)
    
    text_area.insert(tk.END, f"\n{'*'*10} {result_key} {'*'*10}\n")
    text_area.insert(tk.END, analysis_results[result_key])
    text_area.insert(tk.END, f"\n{'*'*60}\n")
    text_area.config(state=tk.DISABLED)
    
def obtener_seleccion():
    global analysis_results, variable
    
    seleccion = variable.get()
    if seleccion == 1:
        print("Opción 1 seleccionada")
        data_path = "data/raw/products.csv"
        output_path = "data/processed/cleaned_products.csv"
        if not os.path.exists("data/raw"):
            os.makedirs("data/raw")
        
        df = load_data(data_path)
        df = clean_data(df)
        analysis_results = analyze_data(df)
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        save_clean_data(df, output_path)
    elif seleccion == 2:
        print("Opción 2 seleccionada")
        data_path = "data/raw/productstablets.csv"
        output_path = "data/processed/cleaned_productstablets.csv"
        if not os.path.exists("data/raw"):
            os.makedirs("data/raw")
        
        df = load_data(data_path)
        df = clean_data(df)
        analysis_results = analyze_data(df)
        
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        save_clean_data(df, output_path)
    
    # Actualizar los botones con los nuevos análisis
    update_buttons()

def update_buttons():
    # Limpiar los botones anteriores
    for widget in button_frame.winfo_children():
        widget.destroy()

    # Crear botones para cada tipo de análisis
    for key in analysis_results.keys():
        button = tk.Button(button_frame, text=key, command=lambda k=key: show_analysis_results(k), bg="yellow", font=("Arial", 12), width=30)
        button.pack(pady=10)

if __name__ == "__main__":   
    
    # Crear la interfaz gráfica de Tkinter
    ventana = tk.Tk()
    ventana.title("Datos Scrapper")
    ventana.geometry("700x600")
    ventana.config(bg="cyan", cursor='pirate')
    
    
          # Escoger opciones:
    global variable
    variable = tk.IntVar()

    opcion1 = tk.Radiobutton(ventana, text="Opción 1: Laptops", bg="White", font=("Arial", 12), variable=variable, value=1, command= obtener_seleccion )
    opcion1.pack(side=tk.TOP, fill=tk.Y, padx=10, pady=10)

    opcion2 = tk.Radiobutton(ventana, text="Opción 2: Tablets", bg="White", font=("Arial", 12),  variable=variable, value=2, command= obtener_seleccion)
    opcion2.pack(side=tk.TOP, fill=tk.Y, padx=10, pady=10)

    # Frame para los botones a la izquierda
    button_frame = tk.Frame(ventana, bg="LimeGreen")
    button_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10, pady=10)
 

   
    # Frame para el área de texto a la derecha
    text_frame = tk.Frame(ventana, bg="cyan")
    text_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    text_area = scrolledtext.ScrolledText(text_frame, width=60, height=30, font=("Arial", 14), bg="white", fg="blue")
    text_area.pack(fill=tk.BOTH, expand=True)
    text_area.config(state=tk.DISABLED)

    ventana.mainloop()
