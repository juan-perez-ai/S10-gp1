"""Clase para generar un resumen en .txt del contenido de un DataFrame."""
from pathlib import Path


class DatasetSummarizer:
    """Recibe un DataFrame y genera un archivo .txt con un resumen de sus datos.

    Args:
        df: DataFrame que se va a resumir.
        title: Título que aparece al inicio del resumen.

    Ejemplo:
        summarizer = DatasetSummarizer(df, title="Resumen de iris")
        summarizer.save("resumen.txt")
    """

    def __init__(self, df, title="Resumen del dataset"):
        self.df = df
        self.title = title

    def build(self):
        """Construye el texto del resumen y lo retorna como string."""
        df = self.df
        lines = [
            self.title,
            "=" * len(self.title),
            "",
            f"Cantidad de filas: {df.shape[0]}",
            f"Cantidad de columnas: {df.shape[1]}",
            "",
            "Nombres y tipos de columnas:",
        ]
        for column, dtype in df.dtypes.items():
            lines.append(f"  - {column}: {dtype}")

        lines += ["", "Valores nulos por columna:"]
        nulls = df.isnull().sum()
        for column, count in nulls.items():
            percent = count / len(df) * 100 if len(df) > 0 else 0
            lines.append(f"  - {column}: {count} ({percent:.1f} %)")
        lines.append(f"Total de valores nulos: {nulls.sum()}")

        lines += [
            "",
            "Estadísticas descriptivas:",
            df.describe(include="all").to_string(),
            "",
            "Primeras 5 filas:",
            df.head().to_string(),
        ]
        return "\n".join(lines)

    def save(self, path="resumen.txt"):
        """Escribe el resumen en un archivo .txt y retorna su ruta."""
        path = Path(path)
        path.write_text(self.build(), encoding="utf-8")
        return path
