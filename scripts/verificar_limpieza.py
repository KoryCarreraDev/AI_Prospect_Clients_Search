#!/usr/bin/env python3
"""Verifica que el repo no contenga datos reales.

Uso:
    python scripts/verificar_limpieza.py [--terminos RUTA] [--sin-git]

Revisiones:
  1. Reglas genéricas (siempre): correos, teléfonos y URLs que no sean de ejemplo.
  2. Términos prohibidos (opcional): un archivo de texto FUERA del repo, uno por línea.
     Una línea que empieza con "tel:" se compara solo con los dígitos del texto.
     La comparación no distingue mayúsculas ni tildes.
  3. Historial de git: mensajes de commit y todos los cambios (git log -p --all).
     El nombre y el correo del autor de los commits no se revisan.

Devuelve código 1 si encuentra algo.
"""
import argparse
import os
import re
import subprocess
import sys
import unicodedata

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SALTAR_DIRS = {".git"}
EXT_BINARIAS = {".png", ".jpg", ".jpeg", ".gif", ".pdf", ".ico", ".zip", ".woff", ".woff2"}

# Dominios que sí pueden aparecer (ejemplos reservados y documentación pública).
DOMINIOS_OK = (
    "example.com", "example.org", "example.net", "ejemplo.test", "ejemplo.example",
    "github.com", "raw.githubusercontent.com", "opensource.org", "apache.org",
    "gnu.org", "choosealicense.com", "creativecommons.org", "spdx.org",
    "claude.com", "anthropic.com", "geminicli.com", "google.com",
    "gov.co", "wa.me", "api.whatsapp.com", "whatsapp.com",
)
RE_CORREO = re.compile(r"[\w.+-]+@([\w-]+(?:\.[\w-]+)+)")
RE_URL = re.compile(r"https?://([\w.-]+)", re.I)
RE_TEL = re.compile(r"(?<![\w/.-])\+?\d[\d ()-]{7,}\d")


def norm(s):
    s = unicodedata.normalize("NFD", s)
    return "".join(c for c in s if unicodedata.category(c) != "Mn").lower()


def dominio_ok(d):
    d = d.lower().rstrip(".")
    return any(d == ok or d.endswith("." + ok) for ok in DOMINIOS_OK) or d.endswith(".example") or d.endswith(".test")


def tel_ok(digitos):
    # Números de ejemplo: contienen una racha de 6 ceros (ej. 300 000 0001).
    return "000000" in digitos


def archivos():
    for base, dirs, files in os.walk(RAIZ):
        dirs[:] = [d for d in dirs if d not in SALTAR_DIRS]
        for f in files:
            if os.path.splitext(f)[1].lower() in EXT_BINARIAS:
                continue
            yield os.path.join(base, f)


def leer(ruta):
    try:
        with open(ruta, encoding="utf-8") as fh:
            return fh.read()
    except (UnicodeDecodeError, OSError):
        return None


def cargar_terminos(ruta):
    txt, tels = [], []
    with open(ruta, encoding="utf-8") as fh:
        for linea in fh:
            t = linea.strip()
            if not t or t.startswith("#"):
                continue
            if t.startswith("tel:"):
                tels.append(re.sub(r"\D", "", t[4:]))
            else:
                txt.append(norm(t))
    return txt, tels


def revisar_texto(nombre, texto, terminos, tels, hallazgos):
    for m in RE_CORREO.finditer(texto):
        if not dominio_ok(m.group(1)):
            hallazgos.append(f"{nombre}: correo no permitido: {m.group(0)}")
    for m in RE_URL.finditer(texto):
        if not dominio_ok(m.group(1)):
            hallazgos.append(f"{nombre}: URL no permitida: {m.group(0)}")
    for m in RE_TEL.finditer(texto):
        digitos = re.sub(r"\D", "", m.group(0))
        if 9 <= len(digitos) <= 13 and not tel_ok(digitos):
            hallazgos.append(f"{nombre}: posible teléfono real: {m.group(0).strip()}")
    n = norm(texto)
    for t in terminos:
        if t in n:
            hallazgos.append(f"{nombre}: contiene un término prohibido (línea del archivo de términos: {t[:3]}…)")
    if tels:
        solo = re.sub(r"\D", "", texto)
        for t in tels:
            if t and t in solo:
                hallazgos.append(f"{nombre}: contiene un teléfono prohibido ({t[:3]}…)")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--terminos", help="archivo de términos prohibidos (fuera del repo)")
    ap.add_argument("--sin-git", action="store_true", help="no revisar el historial de git")
    a = ap.parse_args()

    terminos, tels = ([], [])
    if a.terminos:
        terminos, tels = cargar_terminos(a.terminos)
    else:
        print("AVISO: sin --terminos solo se aplican las reglas genéricas.")

    hallazgos = []
    for ruta in archivos():
        rel = os.path.relpath(ruta, RAIZ)
        revisar_texto(rel, rel, terminos, tels, hallazgos)  # el nombre del archivo también cuenta
        texto = leer(ruta)
        if texto is not None:
            revisar_texto(rel, texto, terminos, tels, hallazgos)

    if not a.sin_git and os.path.isdir(os.path.join(RAIZ, ".git")):
        for nombre, cmd in (
            ("git:mensajes", ["git", "log", "--all", "--format=%s%n%b"]),
            ("git:cambios", ["git", "log", "--all", "-p", "--format=%s"]),
        ):
            r = subprocess.run(cmd, cwd=RAIZ, capture_output=True, text=True, encoding="utf-8", errors="replace")
            if r.stdout:
                revisar_texto(nombre, r.stdout, terminos, tels, hallazgos)

    hallazgos = sorted(set(hallazgos))
    if hallazgos:
        print(f"FALLA: {len(hallazgos)} hallazgo(s)")
        for h in hallazgos:
            print("  -", h)
        return 1
    print("OK: sin datos reales detectados.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
