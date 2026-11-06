# Búsqueda de prospectos

Procedimiento para cualquier agente de IA. Se lee junto con `RULES.md`, `config/fuentes.md`, `config/region.md` y `config/empresa.md`.

## Cuándo se activa

Al inicio de cada sesión, cuenta los prospectos **sin contactar** de `datos_usuario/prospectos.csv`. Cuando queden **5 o menos**, avisa y propone buscar (o busca si el usuario ya lo autorizó).

Un prospecto cuenta como **sin contactar** si cumple todo esto:
- tiene un canal publicado por la empresa (correo o WhatsApp);
- su `estado` no es de exclusión;
- no aparece en `exclusion.csv`;
- no aparece en `enviados.csv`.

Antes de buscar, di al usuario el conteo y que se va a buscar.

## Validación previa

Deben existir `empresa.md`, marca activa, al menos 1 producto, asesor, región, ley y voz. Si falta algo, dilo y para (ver `AGENTS.md`).

## Qué hace y qué no hace el agente

- Busca, verifica y registra. Nada más.
- No envía ni programa ni marca nada como enviado.
- No redacta borradores de los prospectos nuevos hasta que el usuario los apruebe.
- Los prospectos nuevos entran con estado `por revisar`.

## Pasos

1. **Buscar** según los segmentos y las ubicaciones de `config/empresa.md` (clientes ideales) y los tipos de fuente de `config/fuentes.md`. Con `/buscar [segmento] [ciudad]`, solo eso. La búsqueda amplia suele devolver prensa y directorios; usa un modo de búsqueda más profundo si la primera pasada trae ruido.
2. **Registrar la fuente** en `datos_usuario/fuentes_registro.csv` con la fecha y el resultado de revisar sus términos de uso, antes de extraer nada (R5.2).
3. **Abrir el sitio de cada empresa** y verificar, en la propia página:
   - país y ciudad;
   - correo publicado por la empresa (preferiblemente con el dominio del sitio);
   - WhatsApp publicado como tal;
   - si hay términos o política de privacidad enlazados.
4. **Quitar duplicados** contra `prospectos.csv` y `exclusion.csv`, por dominio, correo y teléfono.
5. **Registrar el prospecto** en `prospectos.csv` con `base_origen`, `fuente_dato` y `fecha_encontrado`, y estado `por revisar`.
6. **Informar al usuario:** cuántos entraron, cuántos quedan sin contactar y cuáles tienen dudas.

## Marcar dudas

Se registra igual y se explica en `notas` cuando ocurre alguno de estos casos: sitio que bloquea el acceso automatizado, sin términos ni política de privacidad, correo con dominio distinto al del sitio, correo que parece personal, posible competidor, país no verificado o captura parcial de la página.

## Qué no se usa

- LinkedIn ni redes personales por defecto. Sus términos suelen prohibir la extracción. El usuario puede aportar sus propias listas.
- Nombres de personas o representantes legales como contacto.
- Correos o teléfonos deducidos o construidos a partir de un dominio.
- Datos que solo aparecen en prensa o en directorios de terceros.
- Sitios que bloquean el acceso automatizado: no se rodea el bloqueo; se registran y no se leen.

## Límites por corrida

- Máximo 15 prospectos nuevos por corrida.
- Si después de dos rondas salen menos de 5 con canal publicado, para y dilo.
- Si el usuario no está presente, no preguntes: sigue el procedimiento y deja lo dudoso marcado.
