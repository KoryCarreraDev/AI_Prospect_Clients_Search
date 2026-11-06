---
nombre: estado
descripcion: Resumen: sin contactar, borradores pendientes, respuestas sin atender y chequeo de configuración
argumentos: 
---

1. Lee `AGENTS.md`.
2. **Chequeo de configuración.** Revisa que existan y estén completos (sin PENDIENTE): `config/empresa.md`, marca activa, al menos 1 producto, un asesor, `config/region.md`, `config/ley.md` y `config/voz.md` (mínimo 3 ejemplos; con menos, avisa). Por cada faltante di qué falta y con qué comando completarlo (`/perfil`, `/marca`, `/productos`, `/asesor`, `/region`, `/law_sensitive`, `/voz`).
3. Cuenta en `datos_usuario/prospectos.csv`: prospectos sin contactar (canal publicado, no excluidos, no en `enviados.csv`), contactados, con respuesta, clientes.
4. Cuenta los borradores en `datos_usuario/borradores/` que aún no figuran en `enviados.csv`.
5. Cuenta las respuestas sin atender (prospectos con respuesta registrada y sin borrador de respuesta pendiente de envío).
6. Si quedan 5 o menos sin contactar, avisa que toca buscar (`/buscar`, `guias/busqueda_prospectos.md`).
7. Lista los seguimientos que ya tocan (7 días después de un envío sin respuesta, si el módulo de región lo permite).
Solo lee: no modifica nada.

Al terminar, di qué archivos leíste, cuáles escribiste y qué quedó pendiente de aprobación. No envíes nada ni toques archivos fuera de los indicados.
