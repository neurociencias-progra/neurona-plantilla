# 🔑 Tu token de GitHub — guía de 10 minutos

**Para qué:** en la clase del martes, tu código le va a hablar a GitHub por su **API** (le
pedirá tus issues, en JSON). Sin identificarse, GitHub atiende **60 peticiones por hora POR
RED** — veinte laptops en el mismo wifi se lo acaban en minutos. Con un token personal,
**5 000 por hora cada quien**. El token es tu gafete.

> ⚠️ **Un token es una contraseña.** No se manda al grupo, no se pega en el código, no se
> sube a git. En clase lo guardaremos en un archivo `.env` que git ignora a propósito.
> Si un token se te escapa a un lugar público, no pasa nada grave: se **revoca** y se crea
> otro (y GitHub suele revocarlo solo si lo detecta).

## Crear el token (versión de permisos mínimos)

1. Entra a GitHub y ve a **Settings** (tu foto, arriba a la derecha → Settings).
2. Hasta abajo del menú izquierdo: **Developer settings**.
3. **Personal access tokens → Fine-grained tokens → Generate new token**.
4. Llena así:
   * **Token name:** `curso-neurona`
   * **Expiration:** 30 días (para cuando caduque, el curso ya terminó)
   * **Repository access:** **Public repositories (read-only)** — la primera opción.
     *No* marques repositorios ni permisos extra: para leer lo público no hace falta nada más.
5. **Generate token**, y en la pantalla siguiente **cópialo YA**: empieza con
   `github_pat_…` y **solo se muestra esa única vez**.
6. Guárdalo donde tú lo encuentres el martes (tus notas del teléfono, un correo a ti
   mismo…). En clase lo mudamos a su casa definitiva, el `.env`.

**Quedó si:** tienes un texto largo que empieza con `github_pat_` guardado en tus notas, y
en Settings → Developer settings → Fine-grained tokens aparece `curso-neurona`.

## Si algo no cuadra

* **¿No aparece «Fine-grained tokens»?** Usa la otra pestaña, **Tokens (classic)** →
  Generate new token (classic) → nombre `curso-neurona`, expiración 30 días, y **sin marcar
  ninguna casilla** de permisos (un classic sin permisos también lee lo público). Sirve igual.
* **¿Lo copiaste incompleto o lo perdiste?** No hay drama: borra ese token (Delete) y
  genera otro. Crear y revocar tokens es rutina, no error.
* **¿Te pide confirmar con contraseña o 2FA?** Es normal: estás creando una llave.

Cuando lo tengas: **✅ al grupo** (el ✅, no el token 🙈).
