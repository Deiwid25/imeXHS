# Test Python imeXHS

Este repositorio tiene como funcionalidad establecer los codigos para la prueba tecnica de imexHS

## Recomendaciones

Es recomendable crear un entorno virtual e inicializarlo antes de ejecutar el archivo, para instalar dependencias independientes del sistema operativo. Si estás en Linux, puedes crear el entorno virtual en el repositorio imeXHS:

```bash
 python3 -m venv venv
 source venv/bin/activate
```

Una vez instalado y activado el entorno virtual, puedes iniciar los scripts.

## punto 1 - script

El script `punto1.py` es una herramienta en Python que permite realizar operaciones básicas sobre archivos y directorios. Ofrece funcionalidades para:

1. Listar el contenido de una carpeta.
2. Leer un archivo CSV y mostrar información sobre columnas y datos numéricos.
3. Leer un archivo DICOM y mostrar información de metadatos.

Este script utiliza las bibliotecas `pandas`, `pydicom`, y `logging` para realizar estas tareas.

### Requisitos

Para ejecutar este script, asegúrate de tener instaladas las siguientes bibliotecas:

- `pandas`
- `pydicom`

Puedes instalar estas bibliotecas utilizando `pip`:

### Uso

para correr el script necesitas el sigueinte comando una vez las librerias esten instaladas

```sh
python punto1.py <number[1-3]> <path> <filename> [<tag> ...]
```

### Ejemplo

si el archivo se encuentra en la misma ruta. (de lo contrario ingrese la ruta)

```sh
python punto1.py 3 ./ sample-01-dicom.dcm 0x0008 0x0016
```

## punto 2 - script

El script `punto2.py` permite cargar y procesar información de estudios DICOM utilizando Pydantic para modelado y validación de datos. El script lee la información del paciente y del estudio desde un archivo DICOM y la imprime de manera formateada.

### Características

- **PatientRecord**: Modelo para almacenar información del paciente.
- **Diagnosis**: Hereda de `PatientRecord` e incluye funcionalidades para actualizar y registrar diagnósticos.
- **StudyRecord**: Hereda de `PatientRecord` e incluye campos específicos para registros de estudios.
- **DICOMStudyLoader**: Hereda de `StudyRecord` y proporciona funcionalidad para cargar datos desde un archivo DICOM.

### Uso

1. **Configuración**: Asegúrate de tener `pydicom` y `pydantic` instalados. Puedes instalarlos usando pip:

   ```bash
   pip install pydicom pydantic
   ```

2. **Ejecutar el Script**: Proporciona la ruta a un archivo DICOM como argumento de línea de comandos al ejecutar el script.

   ```bash
   python punto2.py ruta/al/archivo_dicom.dcm
   ```

3. **Salida**: El script cargará el archivo DICOM, extraerá la información relevante y la imprimirá en la consola. La salida incluye la información del paciente y los detalles del estudio.

## punto 3

### punto 3a script

Este script en Python utiliza hilos para imprimir números pares e impares entre 1 y 200. Utiliza la biblioteca `threading` para manejar la concurrencia y sincronización de los hilos.

#### Características

- **print_even_numbers**: Función que imprime números pares del 1 al 200, esperando 0.5 segundos entre cada impresión.
- **print_odd_numbers**: Función que imprime números impares del 1 al 200 mientras el hilo de números pares está activo.

#### Uso

1. **Ejecutar el Script**: Simplemente ejecuta el script para ver la salida en la consola.

   ```bash
   python punto3a.py
   ```

2. **Salida**: El script imprimirá números pares e impares en la consola. Los números impares se imprimirán mientras el hilo de números pares esté activo. Ambos hilos se sincronizan de manera que el hilo de números impares espera hasta que el hilo de números pares haya terminado.

### punto 3b script

Este script en Python lee un archivo JSON que contiene información de datos, valida y procesa los datos en paralelo utilizando hilos. Usa Pydantic para la validación de datos y `concurrent.futures.ThreadPoolExecutor` para gestionar múltiples hilos.

#### Características

- **DataItem**: Modelo de datos definido con Pydantic para validar la estructura de los datos JSON.
- **Validación de JSON**: Lee y valida el archivo JSON, asegurando que cumpla con el modelo `DataItem`.
- **Procesamiento Multihilo**: Utiliza hilos para procesar los datos en paralelo, limitando el número de hilos activos a 4.
- **Normalización de Datos**: Normaliza los datos de 0 a 1 y calcula estadísticas antes y después de la normalización.
- **Registro de Actividades**: Registra información relevante y errores en un archivo de log y en la consola.

#### Uso

1. **Instalación de Dependencias**: Asegúrate de tener instaladas las bibliotecas necesarias. Puedes instalarlas usando pip:

   ```bash
   pip install pydantic
   ```

2. **Ejecutar el Script**: Proporciona la ruta a un archivo JSON como argumento de línea de comandos al ejecutar el script.

   ```bash
   python punto3b.py ruta/al/archivo.json
   ```

## punto 4

El punto 4 es una API RESTful basada en Django que realiza operaciones CRUD (Crear, Leer, Actualizar, Eliminar) para administrar los resultados del procesamiento de imágenes médicas, los cuales se almacenarán en una base de datos PostgreSQL.

### Inicio

Lo primero es ingresar al repositorio punto4:

```bash
cd punto4/
```

Una vez en el repositorio, asigna permisos al script y ejecútalo:

```bash
chmod +x init_api_punto5.sh
./init_api_punto5.sh
```

Este script permite crear la base de datos en PostgreSQL, así como un usuario para conectarse a ella. En caso de que el motor de base de datos no esté instalado en el PC, se creará una base de datos SQLite para probar la aplicación. Si la base de datos es PostgreSQL, el script pedirá la contraseña del usuario PostgreSQL y luego la creación de la contraseña para el usuario django_user que crea el script. Este script también instala las dependencias necesarias, realiza las migraciones y, por último, ejecuta el servidor para usar la aplicación.

Una vez que esté en funcionamiento, puedes dirigirte a:

http://localhost:8000/api/swagger/

Donde podrás consultar la documentación de la API en detalle.

Una vez creada, la próxima vez que necesites iniciar la aplicación, simplemente usa el comando:

```bash
 python manage.py runserver
```
