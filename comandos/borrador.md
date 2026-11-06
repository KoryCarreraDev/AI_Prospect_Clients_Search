---
nombre: borrador
descripcion: Preparar el borrador de un prospecto (por id o nombre)
argumentos: prospecto [canal]
---

1. Aplica la **validación previa** de `AGENTS.md` (empresa, marca activa, producto, asesor, región, ley, voz). Si falta algo, di qué y con qué comando, y para.
2. Resuelve el prospecto por id o por nombre (sin distinguir mayúsculas ni tildes; pregunta si hay varias coincidencias).
3. Revisa que no esté en `exclusion.csv` (correo, teléfono y dominio) ni en `enviados.csv`. Si está en exclusión, no redactes y dilo. Si ya está en `enviados.csv`, es un seguimiento, no un primer contacto.
4. Elige el canal: el pedido, o `canal_elegido`. Solo canales publicados por la empresa. Si hay varios asesores, pregunta cuál firma.
5. Lee la página o el perfil público del prospecto. Si no puedes, dilo arriba del borrador y entrega solo una versión mínima marcada "sin gancho".
6. Lee `guias/guia_mensajes.md`, `config/voz.md`, `config/claims.md`, `config/productos.md`, `config/historias_exito.md`, `datos_usuario/modelos_exitosos.md` y `datos_usuario/modelos_fracaso.md`. Ofrece solo lo configurado.
7. Redacta con la marca activa y el asesor. Incluye el mecanismo para no recibir más mensajes y, si el modo legal es `completo`, el aviso corto de `config/politicas/` (si no existe, avisa y propone `/crear_privacidad`). Propón una fecha dentro del horario del módulo de región.
8. Guarda `datos_usuario/borradores/<id>_<nombre>_<canal>.md` con: tabla de datos (id, canal, asesor, marca, fecha propuesta, exclusión, claims y certificados usados), el mensaje, el aviso, lo que leíste en su página (con enlace) y la lista de verificación de `RULES.md` R6.2.

Al terminar, di qué archivos leíste, cuáles escribiste y qué quedó pendiente de aprobación. No envíes nada ni toques archivos fuera de los indicados.
