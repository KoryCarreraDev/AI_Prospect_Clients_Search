# RULES.md: reglas del núcleo

Reglas obligatorias para el agente y para el usuario. Se leen al inicio de cada sesión (ver `AGENTS.md`).

Estas reglas son comunes a cualquier empresa y a cualquier región. Las reglas legales (horarios, frecuencia, aviso, derechos del titular) **no están aquí**: viven en `guias/modulos_region/` y se activan según `/region` y `/law_sensitive`. Esta herramienta no da asesoría legal.

## 1. Envío y aprobación

- **R1.1** Ningún mensaje sale sin aprobación del usuario. El agente solo redacta en `datos_usuario/borradores/`.
- **R1.2** El agente nunca envía mensajes, nunca los programa, nunca los marca como enviados y no usa herramientas de envío automático. El registro en `datos_usuario/enviados.csv` se hace solo cuando el usuario confirma que envió.
- **R1.3** Cada prospecto recibe mensajes por un solo canal, el elegido en `canal_elegido`. Nunca por dos canales a la vez.
- **R1.4** Si la empresa responde que no quiere más mensajes por cualquier canal, se registra en `exclusion.csv` y no se le escribe por ningún canal.

## 2. Contactos

- **R2.1** Solo contactos de empresa, publicados por la propia empresa (su sitio, su perfil comercial, su página de contacto). Nunca correos ni teléfonos personales, redes personales ni datos de la vida privada.
- **R2.2** Nunca se deduce, se construye ni se adivina un correo o un teléfono a partir de un dominio, un patrón o un directorio de terceros.
- **R2.3** Un canal de WhatsApp solo cuenta si la empresa publica el número como WhatsApp (enlace, etiqueta o perfil comercial).
- **R2.4** Antes de escribir, verifica que el correo o el número pertenecen a esa empresa. No mezcles datos de dos empresas en una misma fila.
- **R2.5** No se recolectan datos sensibles ni de menores de edad.
- **R2.6** Si hay duda sobre si un contacto es de empresa o personal, no se usa y se anota en `notas`.

## 3. Exclusión

- **R3.1** Antes de cada borrador se revisa `exclusion.csv` por correo, teléfono y dominio. Si aparece, no se redacta.
- **R3.2** Toda baja, rechazo, rebote o solicitud de supresión se registra en `exclusion.csv` con motivo y fecha **el mismo día**. La exclusión se mantiene aunque se borren los demás datos, para no volver a escribir.
- **R3.3** La exclusión aplica a todos los canales al mismo tiempo.

## 4. Lo que el modo legal `minimo` nunca desactiva

`/law_sensitive` permite elegir entre `completo` y `minimo`. Nunca existe un apagado total. Siempre se conserva:

1. Una línea en cada mensaje para que el destinatario pueda pedir no recibir más.
2. Respeto inmediato de la lista de exclusión.
3. Ningún contacto deducido, dato sensible ni correo o teléfono personal.
4. Envío siempre manual.

## 5. Registro y trazabilidad

- **R5.1** Cada fila de `prospectos.csv` tiene `base_origen`, `fuente_dato` y `fecha_encontrado`.
- **R5.2** Antes de extraer prospectos de una fuente, se registra en `fuentes_registro.csv` con la fecha y el resultado de revisar sus términos de uso. Si prohíben la extracción, esa fuente no se usa.
- **R5.3** Se respetan `robots.txt` y los términos de uso. No se evade ningún bloqueo. Un sitio que bloquea el acceso automatizado se registra y no se lee.
- **R5.4** No se usan LinkedIn ni redes personales por defecto: sus términos suelen prohibir la extracción. El usuario puede aportar sus propias listas.
- **R5.5** `datos_usuario/enviados.csv` guarda fecha, canal, id del prospecto y borrador usado.
- **R5.6** Los datos de `datos_usuario/` y `config/` no salen de la carpeta ni se suben a herramientas de terceros sin aprobación del usuario.

## 6. Borradores

- **R6.1** Todo mensaje se redacta con `guias/guia_mensajes.md` y la voz del usuario, e incluye la identificación de la marca activa y el mecanismo para no recibir más mensajes.
- **R6.2** Cada borrador incluye: id del prospecto, canal, asesor, marca, fecha propuesta dentro del horario del módulo de región, resultado de la revisión de exclusión, claims y certificados usados, qué leyó en la página de la empresa y una lista de verificación para el usuario.
- **R6.3** El tono no promete resultados ("garantizamos", ahorros, ventas).
- **R6.4** El agente solo menciona lo que esté configurado: productos de `config/productos.md`, claims habilitadas de `config/claims.md`, certificados de `config/certificados.md` solo si la claim lo activa, y clientes de `config/historias_exito.md` solo con `autorizado_a_nombrar: sí`. No inventa resultados, citas ni certificaciones.
- **R6.5** Por defecto no se mencionan precios en los mensajes.

## 7. Comandos

- **R7.1** Cada comando dice qué archivos leyó y cuáles escribió, y no toca nada fuera de los que le corresponden.
- **R7.2** Si el usuario pide algo que viola estas reglas, el agente avisa y no lo ejecuta.
