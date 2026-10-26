"""Clase para generar el resumen .txt con los resultados de las clases CSV y JSON."""


class GeneradorResumenTXT:
    """Recibe las URL de origen y los resultados de ManejadorCSV y ManejadorJSON,
    y escribe un resumen en un archivo .txt.

    Args:
        urls: Diccionario con la URL de origen de cada archivo,
            por ejemplo {"CSV": "https://...", "JSON": "https://..."}.
        resultados_csv: Diccionario que retorna ManejadorCSV.resultados().
        resultados_json: Diccionario que retorna ManejadorJSON.resultados().

    Ejemplo:
        generador = GeneradorResumenTXT(
            urls, manejador_csv.resultados(), manejador_json.resultados()
        )
        generador.generar("resumen.txt")
    """

    def __init__(self, urls, resultados_csv, resultados_json):
        self.urls = urls
        self.resultados = {"CSV": resultados_csv, "JSON": resultados_json}

    def generar(self, ruta="resumen.txt"):
        """Escribe el resumen en un archivo .txt y retorna su ruta."""
        titulo = "Resumen AE2: manejo de archivos CSV, JSON y TXT"
        lineas = [titulo, "=" * len(titulo), ""]

        for formato, resultado in self.resultados.items():
            lineas += [
                f"Archivo {formato}",
                f"  URL de origen: {self.urls[formato]}",
                f"  Archivo importado: {resultado['archivo_importado']}",
                f"  Registros importados: {resultado['registros_importados']}",
                "  Modificaciones realizadas:",
            ]
            lineas += [f"    - {cambio}" for cambio in resultado["modificaciones"]]
            lineas += [
                f"  Nuevo archivo guardado: {resultado['archivo_guardado']}",
                f"  Registros guardados: {resultado['registros_guardados']}",
                "",
            ]

        lineas.append("Clases y métodos utilizados")
        for resultado in self.resultados.values():
            lineas.append(f"  - {resultado['clase']}: {', '.join(resultado['metodos'])}")
        lineas.append(f"  - {type(self).__name__}: generar")

        with open(ruta, "w", encoding="utf-8") as archivo:
            archivo.write("\n".join(lineas) + "\n")
        return ruta
