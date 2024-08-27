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

# Punto2 Script

# Cargador de Estudios DICOM

Este script en Python demuestra cómo cargar y procesar información de estudios DICOM utilizando Pydantic para modelado y validación de datos. El script lee la información del paciente y del estudio desde un archivo DICOM y la imprime de manera formateada.

## Características

- **PatientRecord**: Modelo para almacenar información del paciente.
- **Diagnosis**: Hereda de `PatientRecord` e incluye funcionalidades para actualizar y registrar diagnósticos.
- **StudyRecord**: Hereda de `PatientRecord` e incluye campos específicos para registros de estudios.
- **DICOMStudyLoader**: Hereda de `StudyRecord` y proporciona funcionalidad para cargar datos desde un archivo DICOM.

## Uso

1. **Configuración**: Asegúrate de tener `pydicom` y `pydantic` instalados. Puedes instalarlos usando pip:

   ```bash
   pip install pydicom pydantic

   ```

2. **Ejecutar el Script**: Proporciona la ruta a un archivo DICOM como argumento de línea de comandos al ejecutar el script.

   ```bash
   python script.py ruta/al/archivo_dicom.dcm

   ```

3. **Salida**: El script cargará el archivo DICOM, extraerá la información relevante y la imprimirá en la consola. La salida incluye la información del paciente y los detalles del estudio.
