# Los tres issues que vas a abrir

> **Por qué esto no viene hecho.** Cuando creas un repositorio «desde plantilla», GitHub
> copia los **archivos**, pero **no copia los issues**. Así que los tuyos los abres tú — y
> está bien, porque escribir la tarea antes de programarla es parte del oficio.

En tu repositorio, pestaña **Issues** → **New issue**. Uno por cada worker.

Un issue útil responde tres preguntas, y ninguna es «qué código escribir»:

| | |
|---|---|
| **Qué hay que producir** | el resultado, no los pasos |
| **Cómo sé que está listo** | algo comprobable: un comando, una prueba en verde |
| **Qué puede salir mal** | la trampa que ya conoces |

---

## Issue #1

**Título:** `Worker 1 · El Cargador lee el CSV`

Escribe el cuerpo tú. Para que no arranques en blanco, esto es lo que hay que cubrir:

- qué tres métodos hay que rellenar en `neurona/cargador.py`;
- con qué comando se comprueba (`pytest tests/test_cargador.py`);
- **la trampa**: una línea vacía es un ensayo vacío, no se salta. Explica **por qué** —
  ¿qué pasaría exactamente si la saltaras?

## Issue #2

**Título:** `Worker 2 · El CalculadorDeTasas convierte espigas en hercios`

- qué tres métodos hay que rellenar en `neurona/tasas.py`;
- con qué comando se comprueba;
- **la trampa**: una ventana invertida no debe reventar. ¿Qué debería devolver, y por qué
  eso no es «tragarse un error»?

## Issue #3

**Título:** `Worker 3 · El Graficador dibuja el ráster y las curvas`

- qué dos métodos hay que rellenar en `neurona/graficos.py`;
- **cómo se comprueba esto, si no hay prueba automática.** Piénsalo: ¿cómo demuestras que
  una figura está bien?

---

## Y después, al hacer commit

```bash
git commit -m "Closes #1 — el Cargador lee el CSV"
```

Escribir `Closes #1` en el mensaje **cierra el issue solo** cuando subes el commit. Esa es
la liga entre lo que planeaste y lo que hiciste: dentro de seis meses, cualquiera podrá
preguntarle al historial *por qué* existe cada línea de código.
