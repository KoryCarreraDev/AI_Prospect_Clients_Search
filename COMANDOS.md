# Comandos

Archivo generado por `scripts/sync_comandos.py`. No lo edites: edita `comandos/<nombre>.md` y vuelve a ejecutar el script.

En una IA sin atajos, pídele que lea `AGENTS.md` y escribe la orden como frase ("hazme el borrador de la empresa X").

| Comando | Argumentos | Qué hace |
|---|---|---|
| `/asesor` |  | Definir quién firma y atiende los mensajes |
| `/baja` | `prospecto [motivo]` | Registrar una baja o rechazo en la lista de exclusión |
| `/borrador` | `prospecto [canal]` | Preparar el borrador de un prospecto (por id o nombre) |
| `/buscar` | `[segmento] [ciudad]` | Buscar prospectos nuevos (ej: /buscar cafeterías Bogotá) |
| `/certificados` |  | Registrar las certificaciones del producto |
| `/claims` | `[producto]` | Listar las claims (afirmaciones sobre el producto) y su estado |
| `/comandos` |  | Listar todos los comandos con una línea cada uno |
| `/crear_privacidad` |  | Generar la política de privacidad y el aviso corto para los mensajes |
| `/empezar` |  | Guiar la configuración inicial paso a paso (marca, empresa, productos, asesor, voz, región, ley, fuentes) |
| `/enviado` | `prospecto canal [fecha]` | Registrar que enviaste un mensaje (ej: /enviado Empresa X correo) |
| `/estado` |  | Resumen: sin contactar, borradores pendientes, respuestas sin atender y chequeo de configuración |
| `/exitoso` | `prospecto "mensaje enviado"` | Guardar un mensaje que funcionó en modelos_exitosos.md |
| `/fracaso` | `prospecto "mensaje enviado"` | Guardar un mensaje que no funcionó en modelos_fracaso.md |
| `/fuentes` |  | Definir dónde busca prospectos el agente |
| `/guia_mensaje` |  | Mostrar la guía de mensajes vigente (solo consulta) |
| `/historias_exito` |  | Guardar clientes satisfechos que se pueden mencionar |
| `/law_sensitive` | `completo | minimo` | Definir el modo legal: completo o minimo |
| `/marca` | `[nombre]` | Definir una marca de la empresa (puede haber varias) |
| `/nueva_claim` |  | Crear una claim o registrar una frase prohibida |
| `/nueva_politica` | `[tipo]` | Crear otra política (datos, términos, cookies, devoluciones...) |
| `/nuevo_comando` | `nombre` | Crear un comando nuevo a partir de los existentes |
| `/perfil` |  | Describir la empresa: qué hace, a quién le vende y a quién no |
| `/politicas` |  | Listar las políticas creadas (tipo, fecha, estado) |
| `/productos` |  | Definir los productos con los que se quiere entrar al mercado |
| `/region` |  | Definir el alcance geográfico y el módulo legal que aplica |
| `/respondio` | `prospecto "texto de la respuesta"` | Un prospecto respondió: clasificar y proponer respuesta |
| `/switch` | `nombre_de_la_marca` | Cambiar la marca activa |
| `/venta` | `prospecto` | Registrar una venta y pasar el prospecto a cliente |
| `/voz` |  | Guardar mensajes de ejemplo para que la IA suene como tú |

Los pasos de cada uno están en `comandos/<nombre>.md`.
