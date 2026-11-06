# Módulo de región: Colombia

> **Estado:** resumen de trabajo, SIN revisión legal formal. Se elaboró a partir de resúmenes de los textos oficiales, no del texto literal completo. Antes de citar un artículo o de basar una decisión en este módulo, verifícalo en la fuente oficial y revísalo con un abogado en Colombia. La herramienta no da asesoría legal.

## Idioma
Español. Por defecto, tuteo en singular; se pasa a usted si la marca es claramente formal, y se mantiene en todo el mensaje.

## Normas aplicables

- **Ley 1581 de 2012**, protección de datos personales: https://cancilleria.gov.co/sites/default/files/Normograma/docs/ley_1581_2012.htm
- **Ley 2300 de 2023**, protección del consumidor frente a comunicaciones comerciales no deseadas (conocida como "Dejen de fregar"): https://normograma.mintic.gov.co/docs/pdf/ley_2300_2023.pdf

## Datos personales (Ley 1581 de 2012)

- Un dato personal (nombre de una persona, correo nominal, teléfono asociado a una persona) requiere autorización previa, expresa e informada del titular, salvo excepciones de la ley. Por eso la herramienta usa solo contactos de empresa publicados por la propia empresa.
- **Finalidad:** los datos se usan solo para la prospección comercial descrita en `config/empresa.md`. No se venden ni se comparten.
- **Veracidad:** verificar que el correo o el número pertenecen a esa empresa.
- **Seguridad:** los datos de `datos_usuario/` no salen de la carpeta ni se suben a terceros sin aprobación del usuario.
- **Derechos del titular:** conocer, corregir, suprimir los datos y revocar la autorización. Si alguien lo pide, se borra su fila de `prospectos.csv` y se agrega a `exclusion.csv` con motivo "solicitud de supresión".
- **Aviso al titular (modo `completo`):** el primer mensaje identifica al responsable (razón social, dirección, teléfono), explica para qué se usan los datos y cómo ejercer los derechos. Lo genera `/crear_privacidad` con los datos de la marca activa.
- No se recolectan datos sensibles ni de menores.
- La Superintendencia de Industria y Comercio vigila el cumplimiento y puede sancionar.

## Comunicaciones comerciales (Ley 2300 de 2023)

Aplica a correo, mensajería de aplicaciones (incluido WhatsApp) y llamadas.

- **Canales:** solo los que la empresa publica para contacto comercial. Nunca uno deducido.
- **Horario:** lunes a viernes de 7:00 a. m. a 7:00 p. m.; sábados de 8:00 a. m. a 3:00 p. m. No domingos ni festivos. Pendiente de verificar en el texto oficial.
- **Frecuencia:** máximo un contacto por día. Después de un contacto directo, no se contacta por varios canales en la misma semana. El seguimiento a los 7 días es por el mismo canal y solo si no hubo otro contacto esa semana. Pendiente de verificar en el texto oficial.
- **Cancelación:** cada mensaje ofrece la forma de dejar de recibirlos, que debe funcionar en cualquier momento. Si la persona responde "no" o "baja", se registra en `exclusion.csv` el mismo día hábil.
- **No contactar** a personas de referencia, familiares ni terceros.
- **WhatsApp:** primer mensaje corto, sin adjuntos ni enlaces acortados. Se envía a mano, nunca en masa.
- **Llamadas comerciales:** no las hace la herramienta.

## Qué cambia en modo `minimo`

El modo `minimo` no exige el aviso largo ni las políticas documentadas, pero la ley colombiana sigue aplicando. La herramienta conserva siempre: una línea para pedir no recibir más mensajes, respeto inmediato de la exclusión, ningún contacto deducido o personal, y envío manual. Los horarios y la frecuencia de este módulo se siguen sugiriendo como buena práctica.

## Tipos de fuentes de búsqueda

- Sitios web de empresas, perfiles comerciales públicos y directorios públicos cuyos términos permitan la consulta.
- Listas que aporte el usuario.
- Antes de extraer datos, revisa los términos de uso y `robots.txt` y regístralos en `datos_usuario/fuentes_registro.csv`.

## Pendiente de verificación

- Texto literal de los artículos citados.
- Si el contacto manual de un canal publicado por la empresa cuenta o no como extracción cuando sus términos prohíben la extracción de datos.
- Detalle de sanciones aplicables.
