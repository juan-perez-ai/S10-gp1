"""Clase para importar, modificar y guardar un archivo JSON."""
import json


class ManejadorJSON:
    """Importa un JSON con json.load, lo modifica y lo guarda con json.dump.

    El JSON debe contener una lista de registros (diccionarios).

    Args:
        ruta: Ruta relativa del JSON original, por ejemplo "datos/train.json".

    Ejemplo:
        manejador = ManejadorJSON("datos/train.json")
        manejador.importar()
        manejador.actualizar_valor(0, "instruction", "Da tres consejos para mantenerse saludable.")
        manejador.guardar("datos/train_modificado.json")
    """

    def __init__(self, ruta):
        self.ruta = ruta
        self.registros = []
        self.registros_importados = 0
        self.modificaciones = []
        self.ruta_guardado = None
        self.metodos_usados = []

    def importar(self):
        """Lee el JSON y retorna la lista de registros."""
        self.metodos_usados.append("importar")
        with open(self.ruta, encoding="utf-8") as archivo:
            self.registros = json.load(archivo)
        self.registros_importados = len(self.registros)
        return self.registros

    def actualizar_valor(self, indice, campo, valor):
        """Cambia el valor de un campo en el registro indicado."""
        self.metodos_usados.append("actualizar_valor")
        anterior = self.registros[indice][campo]
        self.registros[indice][campo] = valor
        self.modificaciones.append(
            f"Registro {indice}: el campo '{campo}' cambió de {anterior!r} a {valor!r}"
        )

    def guardar(self, ruta):
        """Escribe los registros en un nuevo JSON y retorna su ruta."""
        self.metodos_usados.append("guardar")
        with open(ruta, "w", encoding="utf-8") as archivo:
            json.dump(self.registros, archivo, ensure_ascii=False, indent=2)
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
            "registros_guardados": len(self.registros),
            "metodos": self.metodos_usados,
        }
