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
   python punto2.py ruta/al/archivo_dicom.dcm

   ```

3. **Salida**: El script cargará el archivo DICOM, extraerá la información relevante y la imprimirá en la consola. La salida incluye la información del paciente y los detalles del estudio.

# Punto 3 a

# Hilos para Imprimir Números Pares e Impares

Este script en Python utiliza hilos para imprimir números pares e impares entre 1 y 200. Utiliza la biblioteca `threading` para manejar la concurrencia y sincronización de los hilos.

## Características

- **print_even_numbers**: Función que imprime números pares del 1 al 200, esperando 0.5 segundos entre cada impresión.
- **print_odd_numbers**: Función que imprime números impares del 1 al 200 mientras el hilo de números pares está activo.

## Uso

1. **Ejecutar el Script**: Simplemente ejecuta el script para ver la salida en la consola.

   ```bash
   python punto3a.py

   ```

2. **Salida**: El script imprimirá números pares e impares en la consola. Los números impares se imprimirán mientras el hilo de números pares esté activo. Ambos hilos se sincronizan de manera que el hilo de números impares espera hasta que el hilo de números pares haya terminado.

# punto 3 b

# Procesador de Datos JSON con Hilos

Este script en Python lee un archivo JSON que contiene información de datos, valida y procesa los datos en paralelo utilizando hilos. Usa Pydantic para la validación de datos y `concurrent.futures.ThreadPoolExecutor` para gestionar múltiples hilos.

## Características

- **DataItem**: Modelo de datos definido con Pydantic para validar la estructura de los datos JSON.
- **Validación de JSON**: Lee y valida el archivo JSON, asegurando que cumpla con el modelo `DataItem`.
- **Procesamiento Multihilo**: Utiliza hilos para procesar los datos en paralelo, limitando el número de hilos activos a 4.
- **Normalización de Datos**: Normaliza los datos de 0 a 1 y calcula estadísticas antes y después de la normalización.
- **Registro de Actividades**: Registra información relevante y errores en un archivo de log y en la consola.

## Uso

1. **Instalación de Dependencias**: Asegúrate de tener instaladas las bibliotecas necesarias. Puedes instalarlas usando pip:

   ```bash
   pip install pydantic

   ```

2. **Ejecutar el Script**: Proporciona la ruta a un archivo JSON como argumento de línea de comandos al ejecutar el script.

   ```bash
   python punto3b.py ruta/al/archivo.json
   ```
