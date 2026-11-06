# Guía de mensajes

Para cualquier agente de IA que redacte un primer contacto o un seguimiento. Es una guía, no una plantilla: el mensaje se escribe de nuevo para cada empresa.

Manda siempre `RULES.md`. Después, el módulo de región y el modo legal (horario, frecuencia y aviso). Después, esta guía.

**Datos que se leen de `config/`:** marca activa (`marca_activa.md` y `marcas/`), asesor (`asesores.md`), productos (`productos.md`), voz (`voz.md`), claims (`claims.md`), certificados (`certificados.md`), historias de éxito (`historias_exito.md`). El aviso de privacidad lo genera `/crear_privacidad`; no está escrito aquí.

## 1. Lo que no cambia

- Se identifica la marca activa y quien escribe (asesor elegido).
- Cada mensaje ofrece una forma de no recibir más mensajes. Con modo legal `completo`, además lleva el aviso corto de `config/politicas/`.
- Sin precios, salvo que `productos.md` diga lo contrario.
- Sin promesas de resultados ni de ahorro.
- Solo se mencionan productos, claims, certificados y clientes que estén configurados y autorizados.
- No se inventa nada del prospecto: solo lo que se vio en su página o perfil público.

## 2. Cómo se arma el mensaje

Antes de escribir una palabra, se lee la página o el perfil público de la empresa. Sin eso no hay mensaje: si no se puede abrir, se dice arriba del borrador y se entrega solo una versión mínima marcada "sin gancho".

Tres movimientos, en tres o cuatro frases:

1. **Algo concreto que viste de ellos.** Un detalle verificable de su página. Si esta frase serviría para cualquier otra empresa, no sirve.
2. **Quién eres y qué ofreces, en una frase.** Tu nombre, la marca y un solo producto que encaje con lo que viste. No se explica todo el catálogo.
3. **Una sola pregunta.** Concreta, sobre algo que ellos conocen de primera mano, que se pueda contestar en una línea. No es una encuesta ni una petición de reunión.

Después van la firma y el aviso.

## 3. Cómo acoplar la propuesta a cada empresa

Anota tres cosas de su sitio. Si no encuentras alguna, no la inventes: dile al usuario que falta información.

- **Qué venden y a quién**, su escala y el tono de la marca.
- **Cómo trabajan o entregan** lo que sea relevante para tu producto.
- **Qué valores dicen públicamente.** Se menciona como observación ("vi que trabajan con…"), no como halago.

Antes de escribir se revisa si ya hubo contacto (`prospectos.csv`, `exclusion.csv`, `enviados.csv`). Si ya se le escribió, no es un primer contacto sino un seguimiento. Si está en exclusión, no se escribe.

Del sitio se sacan uno o dos ganchos concretos. Lo que sale de una inferencia se marca como inferencia. Lo que no se pudo verificar se dice, no se adivina.

**Qué producto abrir.** Si hay varios productos, `productos.md` marca uno como principal y otro como segunda opción. Se abre con el que más encaja con lo que viste. Si hay señales de que los clientes del prospecto se quejan del precio (reseñas, comentarios), la segunda opción entra desde el primer mensaje en una frase, sin hablar de precios.

## 4. Que no suene a IA

Los mensajes de un modelo se reconocen por tres cosas: son demasiado completos, anuncian lo que están haciendo y suenan igual para cualquiera. Un mensaje humano a un desconocido es corto, un poco imperfecto y va directo.

**Escribe así:**
- Un registro por mensaje (tuteo o usted) y se mantiene. Lo define `voz.md`.
- Frases de largo desigual, algunas muy cortas. Palabras de todos los días.
- Saludo simple. Sin "estimados", sin "cordial saludo".
- Dices lo que viste y lo que tienes, y preguntas. Nada más.
- Si algo no aporta, se corta. 45 palabras suelen ser mejor que 90.

**Evita:**
- **Anunciar el mensaje:** "Antes de proponerles nada…", "Me gustaría contarte…", "Te escribo para…".
- **Preguntas de encuesta:** dos preguntas en una, o "cuáles son sus necesidades de…".
- **Catálogo:** enumerar productos en el primer mensaje.
- **Un dato de ellos que no es dato:** "estamos cerca" por estar en la misma región.
- Relleno de apertura, halagos genéricos y lenguaje de folleto ("soluciones", "sinergias", "comprometidos con…").
- Listas de tres, "no solo X sino también Y", rayas largas, exclamaciones, emojis, negritas y viñetas.
- Cierres de manual ("Quedo atento", "Cualquier duda, con gusto"), urgencia falsa y promesas.
- Suponer cosas del prospecto que no viste.

**Prueba antes de entregar:**
1. ¿Alguien sin contexto entiende en cinco segundos quién escribe y qué quiere?
2. ¿Esta apertura podría ir a otra empresa? Si sí, se reescribe.
3. ¿Hay una frase que se puede quitar sin perder nada? Se quita.
4. ¿Cuántas preguntas hay? Si hay más de una, se deja una.

## 5. La voz del usuario

El mensaje debe sonar a quien lo firma. La voz se lee de `config/voz.md`: saludo, manera de preguntar, manera de cerrar, frases que "le suenan" y frases que descarta. El agente imita la manera, no copia frases enteras. Se recomiendan al menos 3 o 4 ejemplos propios; con menos el agente avisa, pero no bloquea.

También se leen `datos_usuario/modelos_exitosos.md` (se imita la estructura y el tono, no el texto) y `datos_usuario/modelos_fracaso.md` (se evitan esos patrones).

## 6. Largo y canal

- **Correo:** asunto de 4 a 7 palabras que apunta a algo de ellos, no a tu producto. Cuerpo de 40 a 70 palabras, sin contar firma ni aviso.
- **WhatsApp:** 25 a 40 palabras, sin contar el aviso. Sin adjuntos ni enlaces acortados.
- **Seguimiento** (solo si no respondió y el módulo de región lo permite): una o dos frases. No se repite la pregunta ni la oferta; se retoma por otra puerta (por ejemplo, el producto de segunda opción) o se pregunta si el mensaje llegó. Siempre con salida fácil.
- **Línea de ventas o atención** (único canal publicado): la primera frase aclara que es una oferta de producto y no un pedido ni una consulta.

## 7. La pregunta del cierre

Se elige una según lo que se vio.

| Lo que viste | Pregunta posible |
|---|---|
| Que venden en línea y despachan | "¿Con qué proveedor trabajan hoy el [insumo]?" |
| Tienda física | "¿Qué [producto] tienen hoy en el mostrador?" |
| Un producto con detalle muy cuidado | "¿Lo hacen ustedes o lo mandan hacer?" |
| No se ve nada del tema | "¿Qué usan hoy para [necesidad]?" |

## 8. Ejemplos (empresa ficticia)

Ejemplos con "Marca Demo" (cuadernos con papel reciclado) y empresas inventadas.

**Bueno: correo a una librería ficticia.**
Asunto: Los cuadernos de Librería Ejemplo Uno

Hola, buen día.

Vi que en Librería Ejemplo Uno los cuadernos artesanales son lo primero en la portada. Soy Ana, de Marca Demo: hacemos cuadernos con papel reciclado y tapa de cartón.

¿Qué cuadernos tienen hoy de papel reciclado?

Ana Demo
Asesora comercial · Marca Demo

[aviso]

**Bueno: WhatsApp a una papelería ficticia.**
Hola, buen día. Soy Ana, de Marca Demo. Vi que Papelería Ejemplo Dos vende útiles escolares por línea en su sitio. Hacemos cuadernos de papel reciclado. ¿Con qué marca de cuadernos trabajan hoy?

[aviso]

**Malo (de manual):**
Estimados señores, espero que se encuentren muy bien. En Marca Demo somos líderes en soluciones innovadoras y comprometidas con el planeta. Nuestros cuadernos, certificados, ayudarán a su negocio a ahorrar costos. ¡No pierdan esta oportunidad! Quedo atento a cualquier inquietud.

Por qué falla: relleno, lenguaje de folleto, "certificados" sin certificado registrado, promete ahorro, mete urgencia y no menciona nada de ellos.

**Malo (anuncia y hace encuesta):**
Hola, equipo de Librería Ejemplo Uno. Antes de proponerles nada, ¿me cuentan qué cuadernos usan hoy y qué les ha costado con ellos? En Marca Demo fabricamos cuadernos de varios tamaños, con tapa dura, con espiral o cosidos.

Por qué falla: no dice nada que el agente haya visto de ellos, anuncia el mensaje, enumera el catálogo y hace una pregunta de encuesta con dos preguntas dentro.

## 9. Lo que el borrador entrega al usuario

Además del mensaje, cada borrador en `datos_usuario/borradores/` trae:
- **Qué leí en su página**, con el enlace, y qué detalle usé como gancho. Si no se pudo leer, se dice primero.
- **Qué producto mencioné y por qué.**
- **Lista de verificación** de `RULES.md` R6.2.

## 10. Entender lo que necesitan

El primer mensaje abre con una sola pregunta. Las siguientes se hacen de a una o dos, según lo que contesten, con curiosidad y no como interrogatorio. Escucha antes de proponer.

Lo que interesa saber, en orden de utilidad:
- Qué usan hoy para la necesidad que cubre tu producto.
- Cuánto consumen, aunque sea aproximado.
- Qué les ha dado problemas (calidad, disponibilidad, mínimos, tiempos, precio).
- Si necesitan personalización.
- Si sus clientes han pedido una alternativa. Se pregunta; no se da por hecho.
- Cada cuánto compran y cómo deciden.

No se critica al proveedor actual ni se pregunta por precios que pagan.

## 11. Objeciones frecuentes

Antes de responder, se distingue entre una **objeción** (una razón para no comprar) y una **negociación** (una razón para comprar más barato). Siempre se empieza reconociendo lo que dijeron, se responde con lo que ellos contaron y se termina con una pregunta que avance. Respuestas de dos a cuatro frases.

No se hace: discutir, ofrecer descuentos para cerrar, volcar características, hablar mal de otro proveedor, prometer precios.

| Dicen | Qué suele significar | Cómo responder |
|---|---|---|
| "Ya tenemos proveedor" | Comodidad o miedo a cambiar | Reconocerlo. Preguntar qué les gusta y qué mejorarían. Ofrecer ser segunda opción para un producto puntual |
| "Es muy caro" / "¿cuánto vale?" | Negociación o falta de información | No dar precios por mensaje salvo que estén configurados. Pedir cantidad y personalización para que el asesor responda |
| "Ahora no" | Mal momento o poco interés | Agradecer, preguntar cuándo retomar y anotarlo. No insistir |
| "Envíame información" | Quiere conocer, sin compromiso | Responder con una pregunta de qué necesitan y avisar al usuario: él decide qué material enviar |
| "No me interesa" / pide salir | Decisión tomada | Agradecer en una línea. Registrar en `exclusion.csv` el mismo día. No volver a escribir |

Las respuestas a objeciones se entregan como borrador; no se envían.

## 12. Cuando responden

1. **Avisar al usuario** de inmediato, en una o dos líneas.
2. **Clasificar** la respuesta: interés, pregunta, objeción, "ahora no" o baja.
3. **Proponer un borrador** de respuesta por el mismo canal, con la misma voz. Una pregunta a la vez.
4. **Guardar lo que contaron** de sus necesidades en `notas` del prospecto.
5. **Pasar la conversación al humano** cuando ya haya suficiente para decidir: se entiende qué necesitan y cuánto. Desde ahí el usuario define muestras, precios, plazos y cotizaciones. El agente no promete nada de eso.
6. **Baja:** se registra el mismo día.

## 13. Señales de queja de precio

Si hay reseñas o comentarios públicos donde los clientes del prospecto se quejan de lo que cuesta algo relacionado con tu producto, se anota en `notas` como observación con su fuente. En el primer mensaje, la opción más económica del catálogo (si `productos.md` la marca) entra como segunda opción, en una frase y sin hablar de precios.
