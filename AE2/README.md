# AE2: manejo de archivos CSV, JSON y TXT

Continuación de la actividad 1: en lugar de cargar el dataset con la librería `datasets`, se descargan manualmente un CSV y un JSON de Hugging Face, se importan, modifican y guardan con dos clases, y una tercera clase genera un resumen `.txt`. Todo se coordina desde un notebook de Jupyter.

```
Descarga manual → importar → modificar → guardar nuevo CSV y JSON
                → GeneradorResumenTXT → resumen.txt con URL de origen
```

## Datos de origen (Hugging Face)

| Formato | URL de origen | Original | Modificado |
|---|---|---|---|
| CSV | https://huggingface.co/datasets/RummageLabs/pixar_movies/blob/main/pixar_movies.csv | `datos/pixar_movies.csv` (28 películas) | `datos/pixar_movies_modificado.csv` |
| JSON | https://huggingface.co/datasets/llamafactory/tiny-supervised-dataset/blob/main/train.json | `datos/train.json` (300 instrucciones) | `datos/train_modificado.json` |

Los originales se descargaron desde esas páginas de Hugging Face y no se modifican.

## Archivos

| Archivo | Descripción |
|---|---|
| `manejador_csv.py` | Clase `ManejadorCSV`: importa con `csv.reader`, actualiza un valor y guarda un nuevo CSV con encabezados usando `csv.writer`. |
| `manejador_json.py` | Clase `ManejadorJSON`: importa con `json.load`, actualiza un valor y guarda un nuevo JSON con `json.dump`. |
| `generador_resumen_txt.py` | Clase `GeneradorResumenTXT`: recibe las URL y los resultados de las otras dos clases y genera `resumen.txt`. |
| `ae2_manejo_archivos.ipynb` | Notebook (ejecutado) que coordina todo el flujo. |
| `resumen.txt` | Resumen generado por el notebook. |
| `datos/` | CSV y JSON originales y modificados. |

## Modificaciones realizadas

- **CSV:** `actualizar_valor` traduce al español el título de la fila 4: *Finding Nemo* → *Buscando a Nemo*.
- **JSON:** `actualizar_valor` traduce al español el campo `instruction` del registro 0.

## Pasos de ejecución

1. Entrar en la carpeta `AE2` (el notebook usa rutas relativas).
2. Crear un entorno virtual e instalar Jupyter (las clases solo usan `csv` y `json`, que vienen con Python):

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Abrir el notebook y ejecutar todas las celdas en orden:

   ```bash
   jupyter notebook ae2_manejo_archivos.ipynb
   ```

Al terminar se crean (o reemplazan) `datos/pixar_movies_modificado.csv`, `datos/train_modificado.json` y `resumen.txt`.

Ejemplo de uso de las clases sin el notebook:

```python
from manejador_csv import ManejadorCSV
from manejador_json import ManejadorJSON
from generador_resumen_txt import GeneradorResumenTXT

manejador_csv = ManejadorCSV("datos/pixar_movies.csv")
manejador_csv.importar()
manejador_csv.actualizar_valor(4, "movie", "Buscando a Nemo")
manejador_csv.guardar("datos/pixar_movies_modificado.csv")

manejador_json = ManejadorJSON("datos/train.json")
manejador_json.importar()
manejador_json.actualizar_valor(0, "instruction", "Da tres consejos para mantenerse saludable.")
manejador_json.guardar("datos/train_modificado.json")

urls = {"CSV": "https://...", "JSON": "https://..."}
GeneradorResumenTXT(urls, manejador_csv.resultados(), manejador_json.resultados()).generar("resumen.txt")
```
