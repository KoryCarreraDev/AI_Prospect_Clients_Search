---
nombre: buscar
descripcion: Buscar prospectos nuevos (ej: /buscar cafeterías Bogotá)
argumentos: [segmento] [ciudad]
---

1. Aplica la **validación previa** de `AGENTS.md`.
2. Lee `guias/busqueda_prospectos.md`, `config/fuentes.md`, `config/empresa.md` y `config/region.md`.
3. Con segmento y ciudad, busca solo eso; sin argumentos, usa los clientes ideales de `config/empresa.md`.
4. Antes de extraer datos de una fuente, revisa sus términos de uso y `robots.txt` y regístrala en `datos_usuario/fuentes_registro.csv`. Si prohíbe la extracción, no la uses.
5. Verifica en la página de cada empresa su ubicación y los canales publicados. Nunca deduzcas correos ni teléfonos. Quita duplicados contra `prospectos.csv` y `exclusion.csv`.
6. Registra cada prospecto en `datos_usuario/prospectos.csv` con `base_origen`, `fuente_dato`, `fecha_encontrado` y estado `por revisar`. Máximo 15 por corrida.
7. Informa cuántos entraron, cuántos quedan sin contactar y cuáles tienen dudas. No redactes borradores de los nuevos hasta que el usuario los apruebe.

Al terminar, di qué archivos leíste, cuáles escribiste y qué quedó pendiente de aprobación. No envíes nada ni toques archivos fuera de los indicados.
