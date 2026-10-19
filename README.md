# Actividad: dataset de Hugging Face → DataFrame → resumen .txt

Se carga un dataset de Hugging Face como DataFrame de pandas, se le aplica una transformación mínima y se genera un resumen en un archivo `.txt`.

```
HFDatasetLoader → DataFrame → transformación mínima → DatasetSummarizer → archivo .txt
```

Dataset usado: [PixelPulse64/canadian_addresses](https://huggingface.co/datasets/PixelPulse64/canadian_addresses) (direcciones de Canadá).

## Archivos

| Archivo | Descripción |
|---|---|
| `hf_dataset_loader.py` | Clase `HFDatasetLoader`: se conecta a Hugging Face y devuelve el dataset como DataFrame. |
| `dataset_summarizer.py` | Clase `DatasetSummarizer`: recibe un DataFrame y genera un `.txt` con su resumen. |
| `actividad_hf_dataset.ipynb` | Notebook que ejecuta el flujo completo. |
| `resumen_canadian_addresses.txt` | Resumen generado por el notebook (datos transformados). |
| `requirements.txt` | Librerías necesarias. |

## Instalación

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## Uso

Abrir `actividad_hf_dataset.ipynb` con Jupyter (o VS Code), elegir el kernel de `.venv` y ejecutar las celdas en orden.

Ejemplo de uso de las clases:

```python
from hf_dataset_loader import HFDatasetLoader
from dataset_summarizer import DatasetSummarizer

df = HFDatasetLoader("scikit-learn/iris", split="train").load()
DatasetSummarizer(df, title="Resumen de iris").save("resumen_iris.txt")
```

Para datasets muy grandes se puede limitar la cantidad de filas con `max_rows`:

```python
df = HFDatasetLoader("PixelPulse64/canadian_addresses", max_rows=50000).load()
```

## Transformación aplicada

En el notebook se seleccionan 5 de las 7 columnas: se descartan `__index_level_0__` (índice técnico) y `postal_code` (vacía en las filas cargadas). El resumen `.txt` se genera con ese DataFrame transformado.
