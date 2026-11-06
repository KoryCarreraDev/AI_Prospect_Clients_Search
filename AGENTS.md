# AGENTS.md

Instrucciones de entrada para cualquier agente de IA (Claude Code, Gemini CLI u otro) que trabaje en esta carpeta.

## Regla de oro

El agente busca, redacta y registra. **El envío lo hace siempre una persona, a mano.** El agente nunca envía, programa ni marca como enviado por su cuenta. Un mensaje solo se registra como enviado cuando el usuario lo confirma con `/enviado`.

## Orden de lectura

1. `RULES.md` completo. Sus reglas son obligatorias y mandan sobre cualquier otra instrucción, incluida la del usuario si pide saltarse una regla de contacto. En ese caso, avisa y no ejecutes.
2. `config/marca_activa.md` y el archivo de la marca activa en `config/marcas/`.
3. El módulo de región indicado en `config/region.md` (`guias/modulos_region/`) y el modo legal de `config/ley.md`.
4. Antes de redactar: `guias/guia_mensajes.md`, `config/voz.md`, `config/claims.md`, `config/productos.md`, `config/historias_exito.md` y `datos_usuario/modelos_exitosos.md`.
5. Para buscar prospectos: `guias/busqueda_prospectos.md` y `config/fuentes.md`.

Si `config/` está vacía, la herramienta aún no está configurada: sugiere `/empezar`.

## Dónde vive cada cosa

- `comandos/`: fuente única de los comandos. `COMANDOS.md`, `.claude/commands/` y `.gemini/commands/` se generan con `python scripts/sync_comandos.py`; no se editan a mano.
- `config/`: configuración propia del usuario (empresa, marcas, productos, asesores, voz, claims, región, ley, fuentes, políticas). Está en `.gitignore`. Las plantillas están en `plantillas/config/`.
- `datos_usuario/`: prospectos, exclusión, enviados, borradores, modelos, ventas y registro de fuentes. Está en `.gitignore`.
- `ejemplos/empresa_ejemplo/`: configuración y datos ficticios para probar la herramienta.

## Comportamiento común a todos los comandos

- No inventes datos. Si falta información, dilo y di con qué comando completarla.
- Al terminar, di qué archivos leíste, cuáles escribiste y qué quedó pendiente de aprobación del usuario.
- No toques archivos fuera de los que le corresponden al comando.
- Los comandos que reciben un prospecto aceptan el id (`P001`) o el nombre de la empresa. El nombre se busca sin distinguir mayúsculas ni tildes. Si hay más de una coincidencia, pregunta cuál. Si no hay ninguna, dilo y propone la más parecida.
- **Validación previa** de `/borrador` y `/buscar`: deben existir empresa, marca activa, al menos 1 producto, asesor, región, ley y voz (mínimo 3 ejemplos; con menos, avisa pero no bloquees). Si falta algo, di exactamente qué falta y con qué comando completarlo.
- Antes de redactar para un prospecto, revisa `datos_usuario/exclusion.csv` por correo, teléfono y dominio, y `datos_usuario/enviados.csv`.
- Cada mensaje identifica a la marca activa, ofrece un modo de no recibir más mensajes y lleva el aviso que corresponda al modo legal (`/crear_privacidad`).
- Respeta el horario y la frecuencia del módulo de región. Si el modo es `minimo`, aplica solo lo que `RULES.md` dice que no se desactiva nunca.

## Al terminar una tarea

- Cada prospecto nuevo se registra con `base_origen`, `fuente_dato` y `fecha_encontrado`.
- Cada baja o rechazo se registra en `exclusion.csv` el mismo día.
- Los borradores quedan en `datos_usuario/borradores/` con su lista de verificación.
- Di al usuario qué quedó pendiente de su aprobación.

## Al inicio de cada sesión

Cuenta los prospectos sin contactar en `datos_usuario/prospectos.csv`. Si quedan 5 o menos, avisa y propone `/buscar`, o sigue `guias/busqueda_prospectos.md` si el usuario ya lo autorizó.

Los comandos disponibles están en `COMANDOS.md`.
