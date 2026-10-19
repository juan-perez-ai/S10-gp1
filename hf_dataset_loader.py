"""Clase para obtener un dataset de Hugging Face como DataFrame de pandas."""
import pandas as pd
from datasets import load_dataset


class HFDatasetLoader:
    """Se conecta a Hugging Face Datasets y devuelve los datos como DataFrame.

    Args:
        dataset_id: Identificador del dataset en Hugging Face,
            por ejemplo "scikit-learn/iris".
        split: División que se desea cargar (por defecto "train").
        max_rows: Cantidad máxima de filas a cargar (opcional). Si se indica,
            el dataset se lee en modo streaming y solo se descargan las filas
            necesarias. Es útil para datasets muy grandes.

    Ejemplo:
        loader = HFDatasetLoader("scikit-learn/iris")
        df = loader.load()
    """

    def __init__(self, dataset_id, split="train", max_rows=None):
        self.dataset_id = dataset_id
        self.split = split
        self.max_rows = max_rows

    def load(self):
        """Descarga el split indicado y lo retorna como DataFrame de pandas."""
        if self.max_rows is None:
            dataset = load_dataset(self.dataset_id, split=self.split)
            return dataset.to_pandas()

        # Modo streaming: se leen solo las primeras max_rows filas.
        dataset = load_dataset(self.dataset_id, split=self.split, streaming=True)
        return pd.DataFrame(list(dataset.take(self.max_rows)))
