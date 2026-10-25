"""Clase para importar, modificar y guardar un archivo CSV."""
import csv


class ManejadorCSV:
    """Importa un CSV con csv.reader, lo modifica y lo guarda con csv.writer.

    Se usa la codificación "utf-8-sig" para leer bien los CSV que empiezan
    con BOM (una marca invisible que agregan algunos programas, como Excel).

    Args:
        ruta: Ruta relativa del CSV original, por ejemplo "datos/pixar_movies.csv".

    Ejemplo:
        manejador = ManejadorCSV("datos/pixar_movies.csv")
        manejador.importar()
        manejador.actualizar_valor(4, "movie", "Buscando a Nemo")
        manejador.guardar("datos/pixar_movies_modificado.csv")
    """

    def __init__(self, ruta):
        self.ruta = ruta
        self.encabezados = []
        self.filas = []
        self.registros_importados = 0
        self.modificaciones = []
        self.ruta_guardado = None
        self.metodos_usados = []

    def importar(self):
        """Lee el CSV: la primera fila son los encabezados y el resto los registros."""
        self.metodos_usados.append("importar")
        with open(self.ruta, encoding="utf-8-sig", newline="") as archivo:
            lector = csv.reader(archivo)
            self.encabezados = next(lector)
            self.filas = list(lector)
        self.registros_importados = len(self.filas)
        return self.filas

    def actualizar_valor(self, indice, columna, valor):
        """Cambia el valor de una columna en la fila indicada."""
        self.metodos_usados.append("actualizar_valor")
        posicion = self.encabezados.index(columna)
        anterior = self.filas[indice][posicion]
        self.filas[indice][posicion] = valor
        self.modificaciones.append(
            f"Fila {indice}: la columna '{columna}' cambió de {anterior!r} a {valor!r}"
        )

    def guardar(self, ruta):
        """Escribe los encabezados y los registros en un nuevo CSV y retorna su ruta."""
        self.metodos_usados.append("guardar")
        with open(ruta, "w", encoding="utf-8-sig", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(self.encabezados)
            escritor.writerows(self.filas)
        self.ruta_guardado = ruta
        return ruta

    def resultados(self):
        """Retorna un diccionario con lo realizado, para generar el resumen TXT."""
        self.metodos_usados.append("resultados")
        return {
            "clase": type(self).__name__,
            "archivo_importado": self.ruta,
            "registros_importados": self.registros_importados,
            "modificaciones": self.modificaciones,
            "archivo_guardado": self.ruta_guardado,
            "registros_guardados": len(self.filas),
            "metodos": self.metodos_usados,
        }
