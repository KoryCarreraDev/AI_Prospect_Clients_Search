---
nombre: nuevo_comando
descripcion: Crear un comando nuevo a partir de los existentes
argumentos: nombre
---

1. Pregunta nombre, descripción, argumentos y pasos. Revisa un comando existente de `comandos/` como modelo.
2. Verifica que el nombre no exista ya.
3. Crea `comandos/<nombre>.md` con frontmatter (`nombre`, `descripcion`, `argumentos`) y los pasos.
4. Ejecuta `python scripts/sync_comandos.py` para generar los adaptadores de Claude Code (`.claude/commands/`) y Gemini CLI (`.gemini/commands/`) y `COMANDOS.md`.
5. Avisa que hay que reiniciar la sesión si la herramienta no recarga los comandos.
No edites a mano los adaptadores.

Al terminar, di qué archivos leíste, cuáles escribiste y qué quedó pendiente de aprobación. No envíes nada ni toques archivos fuera de los indicados.
