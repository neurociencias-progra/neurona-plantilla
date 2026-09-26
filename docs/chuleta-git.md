# 📋 Chuleta de git — referencia rápida

**No se memoriza: se consulta.** Con la primera sección haces el 95 % del curso; el resto
está para cuando lo necesites. *(Adaptada de la guía «Git & GitHub — A Practical Guide»
que el profe dio en Cornell, julio 2026.)*

---

## El ciclo de todos los días (esto es el curso)

```
git status                          ¿qué cambió?
git add .                           prepara TODO lo cambiado (el "staging")
git commit -m "Closes #1: ..."      la foto, con mensaje — y cierra el issue #1
git push                            súbelo a GitHub
```

**El mensaje de commit en este curso:** `Closes #N: qué hiciste` — en español, y el
`Closes #N` cierra solo el issue al hacer push. Ejemplo:
`git commit -m "Closes #2: el CalculadorDeTasas convierte espigas en hercios"`

**Los cuatro lugares donde vive tu código:**

```
tus archivos ──add──▶ staging ──commit──▶ historia local (.git) ──push──▶ GitHub
     ◀────────────────────── pull (baja lo de otros) ──────────────────────
```

---

## Vocabulario mínimo

| palabra | qué es |
|---|---|
| **repositorio** | la carpeta del proyecto que git vigila, con TODA su historia |
| **commit** | una foto del proyecto: qué cambió, quién y cuándo, con su hash (`d9fc673`) |
| **rama** (*branch*) | una línea de trabajo aparte, para no tocar `main` mientras construyes |
| **PR** (*pull request*) | la propuesta de fusionar tu rama; ahí ocurre la revisión |
| **merge** | fusionar una rama en otra; si dos personas tocaron la misma línea: conflicto |
| **clone / fork** | clonar = copia local de un repo; fork = TU copia de un repo ajeno en GitHub |

---

## Configuración (una sola vez por máquina)

| comando | qué hace |
|---|---|
| `git config --global user.name "Tu Nombre"` | quién firma tus commits |
| `git config --global user.email "tu@correo"` | usa el correo de tu cuenta de GitHub, para que salgan con tu foto |
| `git config --list` | ver tu configuración |

## Empezar

| comando | qué hace |
|---|---|
| `git clone <url>` | copia local de un repo remoto (lo que hiciste hoy) |
| `git init` | convertir una carpeta cualquiera en repo (lo verás en demo) |

## Las fotos de cada día

| comando | qué hace |
|---|---|
| `git status` | qué está cambiado y qué está preparado |
| `git add <archivo>` · `git add .` | preparar uno · preparar todo |
| `git commit -m "mensaje"` | guardar la foto |
| `git diff` · `git diff --staged` | ver cambios sin preparar · ya preparados |

## Ramas y fusiones *(las usarás en la Clase 4)*

| comando | qué hace |
|---|---|
| `git branch` | listar ramas |
| `git switch -c feature/modelo` | crear una rama y cambiarte a ella |
| `git switch main` | volver a `main` |
| `git merge <rama>` | fusionar `<rama>` en la actual |
| `git branch -d <rama>` | borrar una rama ya fusionada |

> En este curso: ramas `feature/...` que salen de `main` y vuelven a `main` por PR, con
> **merge con commit de merge** (conserva la historia de la rama). En equipos verás
> variantes: *squash* (aplasta la rama en un commit) o Git Flow completo con `develop`,
> `release` y `hotfix` — misma idea, más ceremonia.

## Leer la historia

| comando | qué hace |
|---|---|
| `git log` · `git log --oneline` | historia completa · compacta |
| `git log --oneline --graph` | con el dibujo de las ramas |
| `git show <hash>` | el detalle de un commit |
| `git blame <archivo>` | quién tocó cada línea |

## Sincronizar con GitHub

| comando | qué hace |
|---|---|
| `git push` | subir tus commits |
| `git pull` | traer lo nuevo del remoto (baja + fusiona) |
| `git fetch` | solo enterarte de lo nuevo, sin tocar tus archivos |
| `git remote -v` | ver a qué remoto apunta tu repo |

## Deshacer (con cuidado)

| comando | qué hace |
|---|---|
| `git restore <archivo>` | descartar cambios no preparados de ese archivo |
| `git restore --staged <archivo>` | sacarlo del staging (la foto ya no lo incluirá) |
| `git revert <hash>` | deshacer un commit **creando otro** — la forma segura |
| `git stash` · `git stash pop` | guardar trabajo a medias · recuperarlo |
| `git reset --hard <hash>` | ⚠️ borra trabajo de verdad; si crees necesitarlo, pregunta primero |

---

## Un día típico en este curso

```
git pull → trabajas → pytest → git add . → git commit -m "Closes #N: ..." → git push
```

Y en la Clase 4 se le suma: `git switch -c feature/modelo → ... → push → PR en GitHub → merge`.

**¿Un error de git que no entiendes?** Copia el mensaje COMPLETO al grupo o pídele a la IA
que te lo explique (no que lo resuelva) — y anótalo: los errores de git también se
coleccionan. 🗂️
