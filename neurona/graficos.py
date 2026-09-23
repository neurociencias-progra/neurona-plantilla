"""WORKER 3 — Dibujar. Solo eso.

No lee archivos, no calcula tasas. Recibe datos ya listos y los pinta.

No importa a ningún otro worker: esa es la regla.
"""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np


class Graficador:
    """Dibuja las dos figuras clásicas de una neurona: el ráster y las tasas.

    Args:
        colores: nombre de un mapa de color de Matplotlib para distinguir clases.
    """

    def __init__(self, colores: str = "tab20"):
        self.colores = colores

    def __repr__(self) -> str:
        return f"Graficador(colores={self.colores!r})"

    def _paleta(self, n: int):
        mapa = plt.get_cmap(self.colores)
        return [mapa(i % mapa.N) for i in range(n)]

    def raster(self, lista_de_tiempos, etiquetas=None, titulo: str = "Ráster", ax=None):
        """Un punto por espiga, una fila por ensayo.

        Args:
            lista_de_tiempos: una entrada por ensayo, con sus tiempos de espiga.
            etiquetas: opcional, la clase de cada ensayo. Si se da, los ensayos se
                agrupan por clase y cada clase recibe un color.
            titulo: el título de la figura.
            ax: un eje de Matplotlib donde dibujar. Si es None, se crea uno.

        Returns:
            El eje donde se dibujó, por si quieres seguir retocándolo.
        """
        # ──────── TU CÓDIGO AQUÍ ────────
        raise NotImplementedError(
            "plt.subplots si ax es None, y ax.eventplot(). Si hay etiquetas, agrupa por clase y da un color a cada una."
        )


    def curvas(self, centros, curvas_por_clase: dict, titulo: str = "Tasa de disparo", ax=None):
        """Una curva de tasa por clase, todas en el mismo lienzo.

        Args:
            centros: el eje temporal, compartido por todas las curvas.
            curvas_por_clase: diccionario `clase -> arreglo de tasas`.
        """
        # ──────── TU CÓDIGO AQUÍ ────────
        raise NotImplementedError(
            "Un ax.plot() por clase, con su color y su label. Y no olvides ax.legend()."
        )

