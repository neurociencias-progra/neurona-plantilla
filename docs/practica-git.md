# 🖐️ Práctica de git — tu primer commit (sin una línea de Python)

Hoy el objetivo es **el ciclo de git completo**, con un cambio diminuto a propósito.
El resto del repositorio (`neurona/`, `tests/`, los cuadernos) es **el proyecto del
curso**: hoy solo se admira — su día llegará.

## Los siete pasos

1. **Tu repositorio** (si no lo has hecho): en la web,
   `github.com/neurociencias-progra/neurona-plantilla` → **Use this template** →
   nombre **`neurona`** → **Public** → Create.
2. **Tu clon**: en VSCode, `Ctrl+Shift+P` → **`Git: Clone`** → pega la URL de TU repo →
   elige una carpeta de tu home **sin acentos ni espacios** → **Open**.
3. **Las tareas antes que el código**: en la web, pestaña **Issues** → **New issue**.
   Abre **cuatro**, en este orden:
   * los **tres del proyecto** — títulos y cuerpos listos para copiar en
     `docs/issues-por-abrir.md` (ábrelo en VSCode). Hoy **no se resuelven**: solo quedan
     registrados, esperando su clase. Serán los #1–#3.
   * un cuarto, tuyo: título `Inaugurar la bitácora`. Será el **#4** — el de hoy.
4. **El cambio**: abre `README.md` en VSCode y agrega al final una línea:
   `Bitácora: [tu nombre] tomó el control — 30-sep-2026`. Guarda.
5. **El ciclo**, en la terminal (`Terminal → New Terminal`):
   ```
   git status        # tu archivo en rojo: modificado
   git diff          # 👀 exactamente qué cambiaste, línea por línea
   git add README.md
   git status        # ahora en verde: preparado
   git commit -m "Closes #4: bitácora inaugurada"
   git log --oneline # tu historia: dos commits
   git push          # ⚠ el navegador pedirá autorizar: dile que sí
   ```
6. **El momento**: recarga la pestaña **Issues** → el **#4 está CERRADO**, con tu commit
   enlazado. Eso hizo `Closes #4:` por ti.
7. **Compruébalo en grande**: en la página de tu repo, tu línea nueva ya está en el
   README, y en *Commits* vive tu foto con autor y fecha.

## Para valientes (si sobra tiempo)

* `git switch -c juego` → agrega OTRA línea al README → `add` + `commit` → `git switch main`
  (¡tu línea desapareció! está en la rama) → `git switch juego` (¡volvió!) → `git switch main`.
  Acabas de tocar una rama. Se quedan ahí: las fusionaremos el día del proyecto.
* Rompe algo a propósito: borra media README → `git restore README.md` → todo vuelve.
  Esa es la red de seguridad.

**¿Algo truena?** Copia el mensaje COMPLETO de error al grupo. Los errores de git también
se coleccionan. 🗂️
