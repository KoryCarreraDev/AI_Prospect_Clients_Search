---
nombre: empezar
descripcion: Guiar la configuración inicial paso a paso (marca, empresa, productos, asesor, voz, región, ley, fuentes)
argumentos: 
---

1. Si `config/` no tiene archivos, copia las plantillas de `plantillas/config/` a `config/` y las de `plantillas/datos_usuario/` a `datos_usuario/` (sin pisar nada existente). Ofrece también cargar la configuración de ejemplo de `ejemplos/empresa_ejemplo/` si el usuario quiere probar la herramienta (solo si `config/` y `datos_usuario/` están vacías).
2. Revisa qué falta y retoma donde se quedó; esto se puede interrumpir y retomar.
3. Guía en este orden, ejecutando el flujo de cada comando: `/marca`, `/perfil` (empresa), `/productos`, `/asesor`, `/voz`, `/region`, `/law_sensitive`, `/fuentes`.
4. Al final, muestra el chequeo de `/estado` y qué sigue (`/crear_privacidad`, `/nueva_claim`, `/certificados`, `/buscar`).
Haz las preguntas de a una o dos. Guarda las respuestas en el archivo indicado y muestra el resultado para que el usuario lo confirme. Si ya hay datos (campos distintos de PENDIENTE), pregunta si quiere editar, agregar o dejarlo como está. No inventes respuestas.

Al terminar, di qué archivos leíste, cuáles escribiste y qué quedó pendiente de aprobación. No envíes nada ni toques archivos fuera de los indicados.
