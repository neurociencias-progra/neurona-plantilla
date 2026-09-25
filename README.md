# `Neurona` — tu proyecto

Vas a convertir el código que escribiste en los cuadernos en un **proyecto de verdad**:
con archivos, pruebas, e historial. Los datos son una **neurona real** registrada en la
corteza premotora ventral de un mono: 140 ensayos, 20 068 espigas, 14 clases de estímulo.

Al terminar, esto tiene que funcionar:

```python
from neurona import Neurona

n = Neurona("datos/neu_400_RR034075_002_OCPSLA_10_00_VPCizq.csv")
len(n)               # 140
n.raster()           # el ráster de los 140 ensayos
n.tasa_por_clase()   # una curva de tasa por clase
```

---

## 0 · Antes de la clase — lo que tienes que traer instalado

Cuatro cosas, más Python —que seguramente ya tienes—. Ninguna tarda más de diez minutos,
y **si llegas sin ellas te vas a perder la primera media hora**.

| Qué | Dónde | Cómo sabes que quedó |
|---|---|---|
| **Python** | Seguramente **ya lo tienes** (es con lo que has corrido los cuadernos). Si la comprobación de abajo dice que no: [python.org/downloads](https://www.python.org/downloads/) — y en Windows, **marca la casilla «Add Python to PATH»** en la primera pantalla del instalador | El comando de abajo responde |
| **VSCode** | [code.visualstudio.com](https://code.visualstudio.com) | Se abre |
| **La extensión de Python** | Dentro de VSCode: `Ctrl+Shift+X`, busca «Python» de **Microsoft**, *Install* | Dice *Installed* |
| **Git** | [git-scm.com/downloads](https://git-scm.com/downloads) | El comando de abajo responde |
| **Una cuenta de GitHub** | [github.com/signup](https://github.com/signup) | Puedes entrar |

**La comprobación.** Abre VSCode → menú `Terminal` → `Nueva terminal`, y pega estas dos
líneas, **una por una**:

```
python --version
git --version
```

Las dos tienen que responder con un número de versión. Si alguna dice *«command not
found»* o *«no se reconoce»*, esa pieza no quedó instalada.

<details>
<summary>⚠ Windows: si <code>python</code> no responde</summary>

Prueba con `py --version`. Si **esa sí** funciona, tu Python está bien pero no está en el
PATH: dilo en el grupo y lo resolvemos antes de la clase. Si **tampoco**, instala Python
desde [python.org](https://www.python.org/downloads/) y **marca «Add Python to PATH»** en
la primera pantalla.
</details>

<details>
<summary>⚠ Mac o Linux: si <code>python</code> no responde</summary>

Prueba con **`python3 --version`**. En Mac y en muchos Linux el comando se llama así, y es
perfectamente normal: **no te falta nada**. Cuando en clase veas `python`, tú escribe
`python3`.
</details>

---

## 1 · Prepara el entorno (tres clics, sin terminal)

En VSCode, con esta carpeta abierta:

1. `Ctrl+Shift+P` (en Mac, `Cmd+Shift+P`)
2. Escribe **`Python: Create Environment`**
3. Elige **Venv** o **Conda** —te ofrecerá lo que tengas— y marca **`requirements.txt`**

VSCode crea el entorno, lo selecciona e instala todo.

<details>
<summary>A mano, si lo prefieres</summary>

| | crear | activar |
|---|---|---|
| **venv · Windows** | `python -m venv .venv` | `.venv\Scripts\activate` |
| **venv · macOS/Linux** | `python3 -m venv .venv` | `source .venv/bin/activate` |
| **conda** | `conda create -n neurona python=3.12` | `conda activate neurona` |

Y después, en los cuatro casos: `pip install -r requirements.txt`

⚠ **Windows:** si sale *«running scripts is disabled on this system»*, corre una vez en
PowerShell `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`. No pide administrador.
</details>

---

## 2 · Mira el rojo antes de tocar nada

```bash
pytest
```

Verás **4 pruebas en rojo y 8 en verde**. Eso está bien: es tu lista de tareas. Las verdes
son el `TrenDeEspigas` que ya construiste en la clase anterior, ahora viviendo en un
archivo. Las rojas son lo que falta.

**Tu trabajo de hoy es pasar esas cuatro a verde.**

---

## 3 · Qué hay que rellenar

Busca `TU CÓDIGO AQUÍ` en el proyecto. Hay tres archivos, y cada uno es un **worker**: una
clase que hace **una sola cosa** y **no importa a ninguna otra**.

| # | Archivo | Qué tiene que hacer |
|---|---|---|
| 1 | `neurona/cargador.py` | Leer el CSV: metadatos y tiempos de espiga |
| 2 | `neurona/tasas.py` | Convertir tiempos en hercios |
| 3 | `neurona/graficos.py` | Dibujar el ráster y las curvas |

En cada hueco hay un `raise NotImplementedError("…")`. **Lee su mensaje antes que nada: es
una pista.** Luego borra el comentario `TU CÓDIGO AQUÍ` y el `raise` completo, y escribe tu
código en su lugar. Ese `raise` es justo lo que pone la prueba en rojo: si lo dejas y
escribes debajo, Python nunca llega a tu código.

Antes de escribir código, **abre un issue por cada uno**: `docs/issues-por-abrir.md` te
dice qué poner. (GitHub no copia los issues de la plantilla — los tuyos los abres tú.)

**Casi todo lo que necesitas ya lo escribiste** en los cuadernos de las clases de ficheros
y de tasa de disparo. No lo inventes de nuevo: búscalo y tráelo.

Lo que **no** tienes que tocar: `neurona/neurona.py` (el orquestador) ni
`neurona/tren.py`, que ya vienen completos. Léelos: son el ejemplo de hacia dónde va lo
tuyo.

---

## 4 · Por qué está partido así

```
                        Neurona          ← el ORQUESTADOR
                  (los crea y los conecta)
                            │
        ┌───────────────────┼───────────────────┐
    Cargador        CalculadorDeTasas       Graficador
   lee el archivo   calcula hercios        dibuja figuras
```

El `Cargador` no sabe qué es una tasa de disparo. El `Graficador` no sabe leer archivos.
Ninguno conoce a los otros. La única clase que los conoce a los tres es `Neurona`, que les
pasa datos de uno a otro.

¿Para qué tanto lío? Para que cuando algo falle sepas **dónde** mirar, y para poder
cambiar una pieza sin romper las demás. Es el mismo reparto que usa el pipeline de
registro neuronal del laboratorio, con nueve nodos y un orquestador. Aquí, a escala de una
clase.

---

## 5 · Guarda tu trabajo con git

Cada vez que pases una prueba a verde:

```bash
git add .
git commit -m "Closes #1 — el Cargador lee el CSV"
git push
```

Escribir `Closes #1` en el mensaje **cierra el issue #1 solo** cuando subas el commit.
Asómate a la pestaña *Issues* de tu repositorio y míralo tacharse.

---

## Estructura

```
neurona/
├── neurona/
│   ├── tren.py          ✅ ya está — lo hiciste en la clase anterior
│   ├── cargador.py      ⬜ WORKER 1 · tuyo
│   ├── tasas.py         ⬜ WORKER 2 · tuyo
│   ├── graficos.py      ⬜ WORKER 3 · tuyo
│   └── neurona.py       ✅ ya está — el orquestador
├── tests/               las pruebas: 4 en rojo esperándote
├── scripts/
│   └── construir_bd.py  Clase 3 · no lo toques todavía
├── docs/reporte.md      tus respuestas a las cajas 💬
├── datos/               el CSV de la neurona
└── requirements.txt
```

---

## Reglas de la casa

* **Lo regenerable no se versiona.** El `.sqlite` está en `.gitignore`; el script que lo
  crea, no. Se versiona la receta, no el pastel.
* **Los secretos nunca se suben.** El token de GitHub irá en `.env`, también ignorado.
* **Si usas una herramienta de IA, decláralo** en `docs/reporte.md`. Usarla está
  permitido; no decirlo, no. Pídele que te explique un error o que revise tu código —
  no que resuelva el ejercicio, porque entonces el que aprende es él.

¿Atorado? El proyecto terminado está en
**[neurociencias-progra/neurona](https://github.com/neurociencias-progra/neurona)**.
Míralo cuando ya lo hayas intentado.
