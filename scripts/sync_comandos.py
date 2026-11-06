#!/usr/bin/env python3
"""Genera los adaptadores de cada IA a partir de comandos/*.md.

Fuente única: comandos/<nombre>.md, con frontmatter:
    ---
    nombre: borrador
    descripcion: Preparar el borrador de un prospecto
    argumentos: ID_o_nombre [canal]
    ---
    (pasos que debe seguir el agente)

Genera:
  .claude/commands/<nombre>.md    (usa $ARGUMENTS)
  .gemini/commands/<nombre>.toml  (usa {{args}})
  COMANDOS.md                     (lista para IA sin atajos)

Uso: python scripts/sync_comandos.py
"""
import os
import re
import sys

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FUENTE = os.path.join(RAIZ, "comandos")
CLAUDE = os.path.join(RAIZ, ".claude", "commands")
GEMINI = os.path.join(RAIZ, ".gemini", "commands")


def leer_comando(ruta):
    with open(ruta, encoding="utf-8") as fh:
        txt = fh.read()
    m = re.match(r"---\n(.*?)\n---\n(.*)", txt, re.S)
    if not m:
        raise ValueError(f"{ruta}: falta el frontmatter")
    meta = {}
    for linea in m.group(1).splitlines():
        if ":" in linea:
            k, v = linea.split(":", 1)
            meta[k.strip()] = v.strip()
    for campo in ("nombre", "descripcion"):
        if not meta.get(campo):
            raise ValueError(f"{ruta}: falta '{campo}' en el frontmatter")
    nombre = os.path.splitext(os.path.basename(ruta))[0]
    if meta["nombre"] != nombre:
        raise ValueError(f"{ruta}: 'nombre' ({meta['nombre']}) no coincide con el archivo")
    meta.setdefault("argumentos", "")
    meta["cuerpo"] = m.group(2).strip()
    return meta


def esc_toml(s):
    return s.replace("\\", "\\\\").replace('"', '\\"')


def main():
    if not os.path.isdir(FUENTE):
        print("No existe comandos/")
        return 1
    os.makedirs(CLAUDE, exist_ok=True)
    os.makedirs(GEMINI, exist_ok=True)

    cmds = []
    for f in sorted(os.listdir(FUENTE)):
        if f.endswith(".md") and not f.startswith("_"):
            cmds.append(leer_comando(os.path.join(FUENTE, f)))

    nombres = {c["nombre"] for c in cmds}
    # Borrar adaptadores de comandos que ya no existen.
    for carpeta, ext in ((CLAUDE, ".md"), (GEMINI, ".toml")):
        for f in os.listdir(carpeta):
            if f.endswith(ext) and f[: -len(ext)] not in nombres:
                os.remove(os.path.join(carpeta, f))

    for c in cmds:
        n = c["nombre"]
        instr = (
            f"Lee `AGENTS.md` y ejecuta el comando `/{n}` tal como lo define "
            f"`comandos/{n}.md`."
        )
        with open(os.path.join(CLAUDE, f"{n}.md"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write("---\n")
            fh.write(f"description: {c['descripcion']}\n")
            if c["argumentos"]:
                fh.write(f"argument-hint: {c['argumentos']}\n")
            fh.write("---\n\n")
            fh.write(f"{instr}\n\nArgumentos: $ARGUMENTS\n")
        with open(os.path.join(GEMINI, f"{n}.toml"), "w", encoding="utf-8", newline="\n") as fh:
            fh.write(f'description = "{esc_toml(c["descripcion"])}"\n')
            fh.write('prompt = """\n')
            fh.write(f"{instr}\n\nArgumentos: {{{{args}}}}\n")
            fh.write('"""\n')

    with open(os.path.join(RAIZ, "COMANDOS.md"), "w", encoding="utf-8", newline="\n") as fh:
        fh.write("# Comandos\n\n")
        fh.write("Archivo generado por `scripts/sync_comandos.py`. No lo edites: edita `comandos/<nombre>.md` y vuelve a ejecutar el script.\n\n")
        fh.write("En una IA sin atajos, pídele que lea `AGENTS.md` y escribe la orden como frase (\"hazme el borrador de la empresa X\").\n\n")
        fh.write("| Comando | Argumentos | Qué hace |\n|---|---|---|\n")
        for c in cmds:
            arg = f"`{c['argumentos']}`" if c["argumentos"] else ""
            fh.write(f"| `/{c['nombre']}` | {arg} | {c['descripcion']} |\n")
        fh.write("\nLos pasos de cada uno están en `comandos/<nombre>.md`.\n")

    print(f"OK: {len(cmds)} comandos sincronizados (Claude Code, Gemini CLI, COMANDOS.md).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
