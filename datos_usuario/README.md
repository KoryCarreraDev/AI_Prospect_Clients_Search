# datos_usuario/

Datos de trabajo de quien usa la herramienta. Esta carpeta está en `.gitignore`: nada de lo que escribas aquí se sube al repositorio.

El agente crea estos archivos la primera vez que los necesita:

- `prospectos.csv`: empresas encontradas, con su origen, canal y estado.
- `exclusion.csv`: correos, teléfonos y dominios a los que no se debe escribir.
- `enviados.csv`: lo que realmente enviaste, con fecha y canal.
- `borradores/`: mensajes listos para revisar.
- `modelos_exitosos.md` y `modelos_fracaso.md`: mensajes que funcionaron y que no.
- `ventas.csv`: ventas registradas.
- `fuentes_registro.csv`: fuentes de búsqueda y los términos de uso revisados.
