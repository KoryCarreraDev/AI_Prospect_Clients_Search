# ai-prospect-search

Herramienta de prospección comercial asistida por IA, genérica y configurable. El agente busca empresas que encajan con tu negocio, redacta borradores de correo o WhatsApp con tu voz y lleva el registro. **Tú apruebas cada mensaje y lo envías a mano.**

## Para quién es

Para negocios pequeños y medianos que venden a otras empresas y quieren prospectar con orden: saber a quién escribieron, por qué canal, qué funcionó y a quién no volver a escribir. Funciona con Claude Code, Gemini CLI y cualquier otra IA que pueda leer archivos de una carpeta.

## Principio no negociable

El agente **busca, redacta y registra**. El envío lo hace siempre una persona, a mano. El agente nunca envía, programa ni marca como enviado por su cuenta.

## Advertencia legal

Esta herramienta **no es asesoría legal**. Las políticas, avisos y módulos de región que genera o incluye son puntos de partida: revísalos con un abogado de tu país antes de usarlos. Los módulos de región reflejan solo lo que se revisó; para una región sin módulo, la herramienta no afirma nada sobre su ley. La ley de tu región sigue aplicando aunque elijas el modo legal `minimo`.

## Instalación

Necesitas Git, Python 3.8+ y una IA con acceso a archivos (por ejemplo, Claude Code o Gemini CLI).

```bash
git clone <url-del-repositorio> ai-prospect-search
cd ai-prospect-search
python scripts/sync_comandos.py
```

Tus datos y tu configuración viven en `config/` y `datos_usuario/`, que están en `.gitignore`: nunca se suben al repositorio.

## Inicio rápido

1. Abre la carpeta con tu IA.
2. Escribe `/empezar`. Te hará preguntas cortas para configurar, en orden: marca, empresa, productos, asesor, voz, región, ley y fuentes. Puedes interrumpir y retomar.
3. `/crear_privacidad` genera el aviso para tus mensajes.
4. `/buscar` encuentra prospectos. `/borrador <empresa>` prepara el mensaje. Tú lo revisas y lo envías.
5. `/enviado <empresa> <canal>` registra que lo enviaste.

¿Quieres probarla antes? `/empezar` ofrece cargar `ejemplos/empresa_ejemplo/`, una empresa ficticia completa.

## Comandos

Todos aceptan el id del prospecto (`P001`) o el nombre de la empresa (sin distinguir mayúsculas ni tildes). Ninguno envía mensajes.

| Comando | Para qué sirve | Ejemplo |
|---|---|---|
| `/empezar` | Guía la configuración inicial | `/empezar` |
| `/estado` | Sin contactar, borradores pendientes, respuestas sin atender y chequeo de configuración | `/estado` |
| `/borrador` | Prepara el borrador de un prospecto leyendo antes su página | `/borrador Librería Ejemplo Uno correo` |
| `/buscar` | Busca prospectos nuevos y los registra como `por revisar` | `/buscar papelerías Ciudad Ejemplo` |
| `/respondio` | Un prospecto respondió: clasifica y propone respuesta | `/respondio P001 "me interesa"` |
| `/enviado` | Registra que enviaste un mensaje | `/enviado P001 correo` |
| `/baja` | Registra una baja o rechazo en la lista de exclusión | `/baja P001 "pidió salir"` |
| `/exitoso` | Guarda un mensaje que funcionó | `/exitoso P001 "Hola, buen día…"` |
| `/fracaso` | Guarda un mensaje que no funcionó | `/fracaso P002 "Hola…"` |
| `/venta` | Registra una venta y pasa el prospecto a cliente | `/venta P001` |
| `/perfil` | Describe tu empresa | `/perfil` |
| `/marca` | Define una marca (puede haber varias) | `/marca marca_demo` |
| `/switch` | Cambia la marca activa | `/switch marca_demo` |
| `/productos` | Define tus productos (principal y segunda opción) | `/productos` |
| `/asesor` | Define quién firma y atiende | `/asesor` |
| `/voz` | Guarda mensajes tuyos para que la IA suene como tú | `/voz` |
| `/certificados` | Registra certificaciones (solo se nombran las registradas) | `/certificados` |
| `/historias_exito` | Guarda clientes que se pueden nombrar | `/historias_exito` |
| `/guia_mensaje` | Muestra la guía de mensajes (solo consulta) | `/guia_mensaje` |
| `/claims` | Lista las afirmaciones sobre el producto | `/claims` |
| `/nueva_claim` | Crea una afirmación o registra una frase prohibida | `/nueva_claim` |
| `/law_sensitive` | Define el modo legal: `completo` o `minimo` | `/law_sensitive minimo` |
| `/politicas` | Lista las políticas creadas | `/politicas` |
| `/crear_privacidad` | Genera el aviso corto y la política de privacidad | `/crear_privacidad` |
| `/nueva_politica` | Crea otra política (términos, cookies, devoluciones…) | `/nueva_politica términos` |
| `/region` | Define el alcance y el módulo legal que aplica | `/region` |
| `/fuentes` | Define dónde busca prospectos el agente | `/fuentes` |
| `/comandos` | Lista los comandos | `/comandos` |
| `/nuevo_comando` | Crea un comando nuevo | `/nuevo_comando resumen_semanal` |

La definición de cada comando está en `comandos/<nombre>.md`. Esa es la única fuente: los atajos de cada IA se generan con `python scripts/sync_comandos.py`.

## Cómo se usa con cada IA

- **Claude Code:** abre la carpeta y escribe el comando. Los atajos están en `.claude/commands/`.
- **Gemini CLI:** igual, desde la carpeta. Los atajos están en `.gemini/commands/`.
- **Otras IA:** no hay atajos. Pídele que lea `AGENTS.md` y escribe la orden como frase ("hazme el borrador de Librería Ejemplo Uno"). `COMANDOS.md` le dice qué hacer.

## Estructura

```
AGENTS.md  CLAUDE.md  RULES.md  COMANDOS.md   entrada para la IA y reglas del núcleo
comandos/                  fuente única de los comandos
scripts/                   sync_comandos.py, verificar_limpieza.py
guias/                     guía de mensajes, búsqueda y módulos de región
plantillas/                plantillas vacías de config/ y datos_usuario/
config/                    tu configuración (ignorada por git)
datos_usuario/             tus datos (ignorados por git)
ejemplos/empresa_ejemplo/  empresa ficticia para probar
```

## Verificar que el repo no tenga datos reales

```bash
python scripts/verificar_limpieza.py --terminos ruta/a/tu/lista_de_terminos.txt
```

Sin `--terminos` aplica solo reglas genéricas (correos, teléfonos y URLs que no sean de ejemplo). La lista de términos se guarda fuera del repositorio.

## Licencia

GNU General Public License v3.0 o posterior (GPL-3.0-or-later). Ver `LICENSE`. Puedes usar, estudiar, modificar y compartir la herramienta; los derivados que distribuyas deben mantener la misma licencia.

## Cómo contribuir

Abre un issue o un pull request. Antes de enviar cambios, ejecuta `python scripts/sync_comandos.py` y `python scripts/verificar_limpieza.py`. No incluyas datos reales de empresas, personas ni prospectos, ni siquiera como ejemplo. Respeta el principio de envío manual.
