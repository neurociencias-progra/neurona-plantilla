"""WORKER 2 — Calcular tasas de disparo. Solo eso.

No lee archivos, no dibuja. Recibe tiempos de espiga y devuelve números en hercios.

No importa a ningún otro worker: esa es la regla.
"""

from __future__ import annotations

import numpy as np


class CalculadorDeTasas:
    """Convierte tiempos de espiga en tasas de disparo (Hz).

    Args:
        ventana: anchura de la ventana deslizante, en segundos.
        paso: cada cuánto se evalúa la ventana, en segundos.
    """

    def __init__(self, ventana: float = 0.2, paso: float = 0.02):
        if ventana <= 0 or paso <= 0:
            raise ValueError("ventana y paso tienen que ser positivos")
        self.ventana = ventana
        self.paso = paso

    def __repr__(self) -> str:
        return f"CalculadorDeTasas(ventana={self.ventana}, paso={self.paso})"

    def en_ventana(self, tiempos: np.ndarray, t_inicio: float, t_fin: float) -> float:
        """Tasa media (Hz) dentro de [t_inicio, t_fin). Una sola cifra."""
        # ──────── TU CÓDIGO AQUÍ ────────
        raise NotImplementedError(
            "Cuenta las espigas dentro de la ventana y divide entre su duracion. Cuidado con t_fin <= t_inicio."
        )


    def curva(self, tiempos: np.ndarray, t_min: float, t_max: float):
        """Tasa a lo largo del tiempo, con la ventana deslizándose.

        Returns:
            (centros, tasas): dos arreglos del mismo largo. `centros` son los
            instantes en que se evaluó la ventana; `tasas`, los hercios en cada uno.
        """
        # ──────── TU CÓDIGO AQUÍ ────────
        raise NotImplementedError(
            "np.arange para los centros, y en_ventana() centrada en cada uno."
        )


    def curva_media(self, lista_de_tiempos, t_min: float, t_max: float):
        """La curva promediada sobre varios ensayos — el PSTH de toda la vida."""
        # ──────── TU CÓDIGO AQUÍ ────────
        raise NotImplementedError(
            "Una curva por ensayo, y np.mean sobre el eje 0. Ojo con la lista vacia."
        )

