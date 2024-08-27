# imeXHS

Test python imeXHS

# Punto1 Script

## Descripción

El script `punto1.py` es una herramienta en Python que permite realizar operaciones básicas sobre archivos y directorios. Ofrece funcionalidades para:

1. Listar el contenido de una carpeta.
2. Leer un archivo CSV y mostrar información sobre columnas y datos numéricos.
3. Leer un archivo DICOM y mostrar información de metadatos.

Este script utiliza las bibliotecas `pandas`, `pydicom`, y `logging` para realizar estas tareas.

## Requisitos

Para ejecutar este script, asegúrate de tener instaladas las siguientes bibliotecas:

- `pandas`
- `pydicom`

Puedes instalar estas bibliotecas utilizando `pip`:

```sh
python punto1.py <number[1-3]> <path> <filename> [<tag> ...]

```

## Ejemplo

si el archivo se encuentra en la misma ruta.

```sh
python punto1.py 3 ./ sample-01-dicom.dcm 0x0008 0x0016
```
